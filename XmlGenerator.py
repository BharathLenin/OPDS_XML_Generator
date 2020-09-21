import xml.etree.cElementTree as ET
from xml.dom import minidom

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some value2"

#tree = ET.ElementTree(root, xml_declaration=True)
#tree.write("filename.xml")

print(ET.tostring(root, xml_declaration=True, encoding='UTF-8'))  #pretty_print=True))


""""
tree = ET.ElementTree(root)
tree.write("filename.xml", xml_declaration=True, encoding='UTF-8')
"""

#pretty print - attempt 1
xmlstr = minidom.parseString(ET.tostring(root, encoding='UTF-8', xml_declaration=True)).toprettyxml(indent="   ", )
with open("New_Database.xml", "w") as f:
    f.write(xmlstr)