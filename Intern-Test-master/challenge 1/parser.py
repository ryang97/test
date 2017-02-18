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


table = ""
i = 1
for element in tree.iter():
    if element.tag == 'book':
        table += "</tr>\n<tr>"
        table += "<td>" + str(i) + "</td>"
        i = i + 1
    elif element.tag == 'catalog':
        i = i
    elif element.text:
        table += "<td>" + str(element.text) + "</td>"

table += "</tr>"
table = table[5:]
print(table)
