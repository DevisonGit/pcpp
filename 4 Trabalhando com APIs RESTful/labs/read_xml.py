import xml.etree.ElementTree as xmlTree

key_names = ['company', 'last', 'change', 'min', 'max']
key_widths = [50, 8, 8, 8, 8]
nyse = xmlTree.parse('nyse.xml').getroot()


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w).upper(), end='')
    print()
    print('-' * sum(key_widths))


def show_quote(quote):
    for (n, w) in zip(key_names, key_widths):
        if n == 'company':
            print(quote.text.ljust(w), end='')
        else:
            print(str(quote.attrib.get(n)).ljust(w), end='')
    print()


show_head()
for q in nyse.findall('quote'):
    show_quote(q)
