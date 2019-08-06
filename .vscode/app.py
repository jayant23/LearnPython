import os
import xml.etree.ElementTree as ET
import glob
import csv
xml_files = glob.glob("C:/Users/TechFerry/AllPublicXML/NCT0000xxxx/*.xml")


# xml_data = open('C:/Users/TechFerry/xmldata.csv', 'w')
# csvwriter = csv.writer(xml_data)
# xmldata_head = []
# count = 0

# for xml_file in xml_files:
#     tree= et.parse(xml_file)
#     root = tree.getroot()
#     for child in root:
#         nct_id = []
#         country = []
#         for elem in child:
#             if(elem.tag =='nct_id'):
#             # if(country == "United States" and nct_id ):
#                 nct_id= elem.find('nct_id').tag
#                 xmldata_head.append(nct_id)
#                 country = elem.find('country').tag
#                 xmldata_head.append(country)
#                 csvwriter.writerow(xmldata_head)
#                 count = count+1
#                 xml_data.close()
           

#             print(elem,":", elem.tag,":", elem.text)




xml_csvData = open('C:/Users/TechFerry/NCT0000xxxx.csv', 'w')


for xml_file in xml_files:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    csvwriter = csv.writer(xml_csvData)
    csv_data_head = []
    count = 0
    nct_idArr = []
    study_type = []
    for member in root:
        nct_id = []        
        # if count ==0:
        if(member.tag == 'id_info'):
            for item in member.getchildren():
                if(item.tag == 'nct_id'):
                    # with open(r'C:/Users/TechFerry/NCT0000xxxx.csv', 'a') as f:
                        # f.write(item.text+',')
                        # f.close()
                    xml_csvData.write(item.text+'\n')
                    # xml_csvData.close()    
                    # count = count+1
        elif(member.tag=='study_type'):
            if(member.text=='Observational'):
                # with open(r'C:/Users/TechFerry/NCT0000xxxx.csv', 'a') as f:
                    # f.write(member.text + ',')
                    # f.close()
                xml_csvData.write(member.text + ',')    
                # count = count+1
        elif(member.tag == 'location_countries'):
            for item in member.getchildren():
                if(item.tag=='country'):
                    if(item.text=='United States'):
                        # with open(r'C:/Users/TechFerry/NCT0000xxxx.csv', 'a') as f:
                            # f.write(item.text + ',')
                            # f.close()
                        xml_csvData.write(item.text +',')    
                        # count = count+1
        elif(member.tag == 'enrollment'):
            # with open(r'C:/Users/TechFerry/NCT0000xxxx.csv', 'a') as f:
                # f.write(member.text + '\n')
                # f.close()
                xml_csvData.write(member.text + ',')    
            # count = count+1         
            # else(member.tag =='study_type'):
            #     with open(r'C:/Users/TechFerry/xml_csv_data.csv', 'a') as f:
            #         f.write(item.text + '\n')
            #         f.close()
            #         count = count+1       s             
xml_csvData.close()                 
         
