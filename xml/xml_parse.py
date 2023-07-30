from lxml import etree
import xml.etree.ElementTree as ET
import os
import glob
import re
import json
from rich import print


def remove_child_elements(elem):
    for child in elem:
        if child.tag in ['pb', 'lb', 'figure']:
            elem.remove(child)
        else:
            remove_child_elements(child)


def create_files_from_xml(xml_book_path, export_dir="export"):
    """
    recieves the xml_file_path for one of the 13 books of Euclid's Elements
    breaks the file down into separate files
    then translates the xml to json and text
    """
    # Parse the XML file
    tree = etree.parse(xml_book_path)

    os.makedirs(export_dir, exist_ok=True)

    # Get the root element
    root = tree.getroot()

    json_merge = {}
    txt_merge = ""

    # Loop through each div2 element
    for div2 in root.xpath('//div2'):
        # Get the section type and name
        section_type = div2.get('type')
        section_name = div2.xpath('head/text()')[0]
        section_name = section_name.replace('.', '').lower()
        if section_name.endswith("s"):
            section_name = section_name[:-1]

        # Loop through each div3 element in the section
        for div3 in div2.xpath('div3'):
            div3.set('type', section_name)

            div3_id = div3.get('id')
            subsection_file = div3_id + '.xml'
            print(f'section: {div3_id}')

            del div3.attrib['org']
            del div3.attrib['sample']
            remove_child_elements(div3)

            for div4 in div3.findall('div4'):
                del div4.attrib['org']
                del div4.attrib['sample']

            with open(os.path.join(export_dir, subsection_file), 'w') as f:
                f.write(etree.tostring(div3, encoding='unicode', pretty_print=True))

            element_json = translate_xml_to_json(div3)
            json_file_path = f'{div3_id}.json'
            with open(json_file_path, "w") as outfile:
                json.dump(element_json, outfile, indent=4)
            json_merge.update(element_json)

            element_text = extract_text_from_json(element_json)
            txt_file_path = f'{div3_id}.txt'
            txt_merge += element_text
            with open(txt_file_path, "w") as outfile:
                outfile.write(element_text)

    json_merge_file = os.path.join(export_dir, xml_book_path + ".json")

    with open(json_merge_file, 'w') as outfile:
        json.dump(json_merge, outfile, indent=4)

    txt_merge_file = os.path.join(export_dir, xml_book_path + ".txt")

    with open(txt_merge_file, 'w') as outfile:
        outfile.write(txt_merge)


def translate_xml_to_json(element_xml):
    #  root = etree.fromstring(xml_text)
    root = element_xml

    element = {}

    element['id'] = root.get("id")
    element['n'] = int(root.get("n"))
    element['type'] = root.get("type")

    enunc_div = root.find(".//div4[@type='Enunc']")
    proof_div = root.find(".//div4[@type='Proof']")

    if enunc_div is not None and proof_div is not None:
        enunciation = get_text_with_emph(enunc_div.find("p"))
        proof_steps_elements = proof_div.findall("p")
    else:
        paragraphs = root.findall("p")
        enunciation = get_text_with_emph(paragraphs[0])
        proof_steps_elements = paragraphs[1:]

    if enunciation:
        element['enunciation'] = enunciation

    proof_steps = []
    for step in proof_steps_elements:
        text = get_text_with_emph(step)
        refs = [ref.get("target") for ref in step.findall("ref")]
        emphs = [emph.text for emph in step.findall("emph")]
        step = {
                'text': text,
                'refs': refs,
                'emphs': emphs
                }
        proof_steps.append(step)

    if proof_steps:
        element['proof'] = proof_steps

    elem = root.find(".//div4[@type='QED']/p")
    if elem:
        element['qed'] = elem.text

    #  return element
    return {element["id"]: element}


def get_text_with_emph(element):
    text_parts = [element.text or ""]
    for child in element.getchildren():
        if child.tag == "emph":
            text_parts.append(f'`{child.text}`')
        if child.tag == "ref":
            text_parts.append(f'{child.get("target")}')
        if child.tag == "term":
            text_parts.append(f'{{{child.text}}}')
        if child.tag == "hi":
            text_parts.append(f'> {get_text_with_emph(child)}')
        text_parts.append(child.tail or "")
    return "".join(text_parts).strip()


def extract_text_from_json(element_json):
    
    element_key = next(iter(element_json))
    json_data = element_json[element_key]

    text = f"# {element_key}\n\n"

    enunciation = json_data.get("enunciation", "")
    text += f"{enunciation}\n\n"

    for step in json_data.get("proof", []):
        text += f"- {step['text']}\n"

    text += "\n\n"

    return text


if __name__ == "__main__":
    files = glob.glob(os.path.join('.', f'*.xml'))
    for xml_file in files:
        create_files_from_xml(xml_file)

