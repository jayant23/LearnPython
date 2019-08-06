import os 
import glob
import xml.dom.minidom
import xml.etree.ElementTree as ET
import pandas as pd
import xml.dom.minidom as minidom

doc = minidom.parse("C:/Users/TechFerry/AllPublicXML/NCT0000xxxx/NCT00000102.xml")

memoryElem = doc.getElementsByTagName('clinical_study')[0]
# print (''.join( [node.data for node in memoryElem.childNodes] ))
print (memoryElem.getAttribute('id_info'))



xml_files = glob.glob("C:/Users/TechFerry/AllPublicXML/NCT0000xxxx/*.xml")


for eachXMLfile in xml_files:
    doc = xml.dom.minidom.parse(eachXMLfile)
    expertise = doc.getElementsByTagName("clinical_study")

    # tree = ET.parse(expertise)
    tree = ET.parse(eachXMLfile)
    root = tree.getroot()
    root.tag
    root.attrib
    for child in root:
        if(child.tag == 'id_info'):
            for item in child.getchildren():
                if(item.tag == 'nct_id'):
                    print(item.text)
        if(child.tag =='study_type'):
            for item in child.getchildren():
                if(item.text =='observational'):
                    print(item.text)
        # if(child.tag =='location_countries'):
        #     for items in child.getchildren():
        #         if(items.tag =='country'):
        #             if(items.text ==str(input('United States')) | items.text ==str(input('US')) | items.text ==str(input('United States of America'))):
        #                 print(items.text)
    #     print(child.tag, child.attrib)
    # [elem.tag for elem in root.iter()]
    # print(ET.tostring(root, encoding='utf8').decode('utf8'))
    # for child in root.iter('id_info'):
    #     print(ET.tostring(root, encoding='utf8').decode('utf8'))
    #     print (child.tag, child.attrib )     

    # for id_info in root.iter('id_info'):
    #     print(id_info.attrib)

    # for i in expertise:
    #      print(i.childNodes.item.__self__)
    #     for elem in i.childNodes.item.__self__:
    #         print(elem)
        # for item in i.childNodes.item.__self__:
        #     print(item.childNodes.item.__self__)
# print(txt_files)
