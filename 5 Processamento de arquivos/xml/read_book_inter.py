import xml.etree.ElementTree as ET


tree = ET.parse('books.xml')
root = tree.getroot()
for autor in root.iter('author'):
    print(autor.text)
    