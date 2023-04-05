import xml.etree.ElementTree as ET
from rich import print

# Read the XML file
tree = ET.parse('euclid-01.xml')
root = tree.getroot()

# Create an empty dictionary
result = {}

# Iterate over the elements
for child1 in root:
    if child1.tag == 'text':
        for child2 in child1:
            if child2.tag == 'body':
                for child3 in child2:
                    if child3.tag == 'div1':
                        # Check the attributes of div1
                        if 'type' in child3.attrib and 'n' in child3.attrib:
                            div1_type = child3.attrib['type']
                            div1_n = child3.attrib['n']

                            # Create an empty dictionary for div1
                            div1_dict = {}

                            for child4 in child3:
                                if child4.tag == 'pb':
                                    # Check the attributes of pb
                                    if 'n' in child4.attrib:
                                        pb_n = child4.attrib['n']

                                        # Add pb_n to the div1 dictionary
                                        div1_dict['pb_n'] = pb_n
                                elif child4.tag == 'head':
                                    # Add the head text to the div1 dictionary
                                    div1_dict['head'] = child4.text
                                elif child4.tag == 'div2':
                                    # Check the attributes of div2
                                    if 'type' in child4.attrib and 'n' in child4.attrib:
                                        div2_type = child4.attrib['type']
                                        div2_n = child4.attrib['n']

                                        # Create an empty dictionary for div2
                                        div2_dict = {}

                                        for child5 in child4:
                                            if child5.tag == 'head':
                                                # Add the head text to the div2 dictionary
                                                div2_dict['head'] = child5.text
                                            elif child5.tag == 'div3':
                                                # Check the attributes of div3
                                                if 'id' in child5.attrib and 'n' in child5.attrib:
                                                    div3_id = child5.attrib['id']
                                                    div3_n = child5.attrib['n']

                                                    # Create an empty dictionary for div3
                                                    div3_dict = {}

                                                    for child6 in child5:
                                                        if child6.tag == 'head':
                                                            # Add the head text to the div3 dictionary
                                                            div3_dict['head'] = child6.text
                                                        elif child6.tag == 'p':
                                                            # Add the p text to the div3 dictionary
                                                            div3_dict['p'] = child6.text
                                                        elif child6.tag == 'term':
                                                            # Add the term text to the div3 dictionary
                                                            div3_dict['term'] = child6.text

                                                    # Add the div3 dictionary to the div2 dictionary
                                                    div2_dict[div3_n] = div3_dict

                                        # Add the div2 dictionary to the div1 dictionary
                                        div1_dict[div2_type] = {div2_n: div2_dict}

                            # Add the div1 dictionary to the result dictionary
                            result[div1_type] = {div1_n: div1_dict}

# Print the result dictionary
print(result)

