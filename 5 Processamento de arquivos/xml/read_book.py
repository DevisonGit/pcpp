import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
print(f'The root tag is: {root.tag}')
print('The root has the following children:')
for child in root:
    print(child.tag, child.attrib)
