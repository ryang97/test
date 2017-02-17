try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='book_list.xml')

for element in tree.iter():
    if element.tag == 'book':
        print()
        print (element.tag, element.attrib)
    else:
        print(element.tag, element.text)

