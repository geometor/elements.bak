import os
import glob
import re
from lxml import etree
from slugify import slugify
from rich import print

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


        # Loop through each div3 element in the section
        for div3 in div2.xpath('div3'):
            for tag in ['pb', 'lb', 'figure']:
                for el in div3.findall(tag):
                    div3.remove(el)

            div3_id = div3.get('id')
            # Get the subsection number and name
            #  subsection_number = div3.get('n')
            subsection_name = div3.xpath('head/text()')[0]

            # Create a file for the subsection
            subsection_file = div3_id + '-' + '.xml'
            with open(os.path.join(export_dir, subsection_file), 'w') as f:
                # Write the subsection content to the file
                f.write(etree.tostring(div3, encoding='unicode', pretty_print=True))


# Dictionary of keywords for each element type
element_keywords = {
    "point": ["point", "points", "spot", "spots"],
    "line": ["line", "lines", "segment", "segments"],
    "circle": ["circle", "circles", "arc", "arcs"],
    "triangle": ["triangle", "triangles"],
    "angle": ["angle", "angles"],
    "other": []
}


# Function to get the element type for an emph tag in a line
def get_element_type(line, emph):
    keywords = element_keywords["other"]
    for element, kw in element_keywords.items():
        for word in kw:
            if word in line and word in emph:
                keywords = kw
                break
        if keywords != element_keywords["other"]:
            break
    # Find the closest keyword to the emph tag
    closest = None
    min_dist = len(line)
    for keyword in keywords:
        idx = line.find(keyword)
        if idx != -1 and idx < emph.find(","):
            dist = len(emph) - len(keyword) - emph.find(keyword)
            if dist < min_dist:
                min_dist = dist
                closest = element
    return closest


def parse_xml(xml_string):
    # Parse the xml string into an ElementTree
    root = ET.fromstring(xml_string)

    elements = []

    # Loop through each div3 element
    for div3 in root.iter('div3'):
        # Check if this is a proposition
        if div3.find('head') is not None and div3.find('head').text.startswith('Proposition'):
            # Extract the proposition number from the head
            prop_num = int(div3.find('head').text.split()[1].rstrip('.'))
            # Extract the enunc and proof texts
            enunc_text = div3.find(".//div4[@type='Enunc']/p")
            proof_text = div3.find(".//div4[@type='Proof']/p")
            # Extract the note if present
            note_text = None
            note_elem = div3.find(".//note[@type='crit']")
            if note_elem is not None:
                note_text = note_elem.find('p').text
            # Extract the qed if present
            qed_text = None
            qed_elem = div3.find(".//div4[@type='QED']/p")
            if qed_elem is not None:
                qed_text = qed_elem.text
            # Create the Proposition object
            prop = Proposition(prop_num, enunc_text.text, proof_text.text, note_text, qed_text)
            elements.append(prop)

    return elements


def read_xml_files(folder='.'):
    # Create a directory for the section
    export_dir = 'export'
    os.makedirs(export_dir, exist_ok=True)
    files = glob.glob(os.path.join(folder, f'*.xml'))

    max = 10
    i = 1

    for file_path in files:
        print(file_path)

        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            parsed_data = parse_xml(file_contents)

        with open(file_path + '.json', "w") as outfile:
            json.dump(parsed_data, outfile, indent=4)
        if i > max:
            break
        else:
            i += 1

if __name__ == "__main__":
    files = glob.glob(os.path.join('.', f'*.xml'))
    for xml_file in files:
        create_files_from_xml(xml_file)

