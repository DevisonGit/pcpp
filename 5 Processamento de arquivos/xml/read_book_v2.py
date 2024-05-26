import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
print(f'My books')
for child in root:
    print(f'Title: {child.attrib["title"]}')
    print(f'Author: {child[0].text}')
    print(f'Year: {child[1].text}\n')
