import xml.etree.ElementTree as ET

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


root = ET.Element('shop')
tree = ET.ElementTree(root)
category = ET.SubElement(root, 'category', {'name': 'Vegan Products'})
for item in products:
    product = ET.SubElement(category, 'product', {'name': item.get('name')})
    ET.SubElement(product, 'type').text = item.get('type')
    ET.SubElement(product, 'producer').text = item.get('producer')
    ET.SubElement(product, 'price').text = str(item.get('price'))
    ET.SubElement(product, 'currency').text = item.get('currency')

tree.write('shop.xml', 'UTF-8', True)
