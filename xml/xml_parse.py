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


def create_files_from_xml(xml_file_path):
    # Parse the XML file
    tree = etree.parse(xml_file_path)

    export_dir = 'export'
    os.makedirs(export_dir, exist_ok=True)

    # Get the root element
    root = tree.getroot()

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

            #  for tag in ['pb', 'lb', 'figure']:
                #  while div3.find(tag) is not None:
                    #  div3.remove(div3.find(tag))


            with open(os.path.join(export_dir, subsection_file), 'w') as f:
                # Write the subsection content to the file
                f.write(etree.tostring(div3, encoding='unicode', pretty_print=True))


def parse_xml(xml_string):
    # Parse the xml string into an ElementTree
    root = ET.fromstring(xml_string)

    element = {}

    #  elements = []
    element['id'] = root.get('id')

    enunc = root.find(".//div4[@type='Enunc']")
    if enunc:
        element['enunc'] = enunc.text
    proof = root.find(".//div4[@type='Proof']")
    if proof:
        element['proof'] = proof.text
    qed = root.find(".//div4[@type='QED']/p")
    if qed:
        element['qed'] = qed.text

    # Extract the note if present
    notes = root.findall("note")
    notes_text = []
    for note in notes:
        notes_text.append(note.text)
    element['notes'] = notes_text

    xml_string = ET.tostring(root, encoding='utf-8').decode('utf-8')

    #  return element
    return xmltodict.parse(xml_string)

def parse_element(xml_text):
    root = etree.fromstring(xml_text)

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

    return element


def get_text_with_emph(element):
    text_parts = [element.text or ""]
    for child in element.getchildren():
        if child.tag == "emph":
            text_parts.append(f'`{child.text}`')
        if child.tag == "ref":
            text_parts.append(f'{child.get("target")}')
        text_parts.append(child.tail or "")
    return "".join(text_parts).strip()


def convert_xml_to_json(folder='.'):
    files = glob.glob(os.path.join(folder, f'*.xml'))

    max = 50
    i = 1

    for file_path in files:
        print(file_path)

        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()

        parsed_data = parse_element(file_contents)

        print(parsed_data)
        with open(file_path + '.json', "w") as outfile:
            json.dump(parsed_data, outfile, indent=4)

        #  if i > max:
            #  break
        #  else:
            #  i += 1

if __name__ == "__main__":
    files = glob.glob(os.path.join('.', f'*.xml'))
    for xml_file in files:
        create_files_from_xml(xml_file)

    convert_xml_to_json('export')
    
    #  file_path = 'export/elem.1.1.xml'
    #  file_path = 'export/elem.1.def.1.xml'
    #  print(file_path)

    #  with open(file_path, 'r', encoding='utf-8') as file:
        #  file_contents = file.read()

    #  parsed_data = parse_element(file_contents)

    #  print(parsed_data)
