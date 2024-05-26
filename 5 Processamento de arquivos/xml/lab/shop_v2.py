import xml.etree.ElementTree as ET
from xml.dom import minidom


products = [
    {
        'name': 'Good Morning Sunshine',
        'type': 'cereals',
        'producer': 'OpenEDG Testing Service',
        'price': 9.90,
        'currency': 'USD'
    },
    {
        'name': 'Spaghetti Veganietto',
        'type': 'pasta',
        'producer': 'Programmers Eat Pasta',
        'price': 15.49,
        'currency': 'EUR'
    },
    {
        'name': 'Fantastic Almond Milk',
        'type': 'beverages',
        'producer': 'Drinks4Coders Inc.',
        'price': 19.75,
        'currency': 'USD'
    }
]


# Função para indentar o XML usando xml.dom.minidom
def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


root = ET.Element('shop')
tree = ET.ElementTree(root)
category = ET.SubElement(root, 'category', {'name': 'Vegan Products'})
for item in products:
    product = ET.SubElement(category, 'product', {'name': item.get('name')})
    ET.SubElement(product, 'type').text = item.get('type')
    ET.SubElement(product, 'producer').text = item.get('producer')
    ET.SubElement(product, 'price').text = str(item.get('price'))
    ET.SubElement(product, 'currency').text = item.get('currency')

formatted_xml = prettify(root)
with open("shop_v2.xml", "w", encoding="utf-8") as f:
    f.write(formatted_xml)
