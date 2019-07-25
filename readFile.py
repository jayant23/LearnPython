# from pathlib import Path

# path = Path()
# print(path.glob('*.py'))

# for file in path.glob('*.py'):
#     print(file)

# import  csv

# with open("ims_data_new.csv") as csv:
#     readCSV = csv.reader(csv, delimiter=',')
    # for row in readCSV:
    #      print(row)
         
    # reader = csv.DictReader(csvfile)
    # for row in reader:
    #     print(row)

# import csv
# with open('C:/Users/TechFerry/Downloads/ims_data_new.csv', 'r') as csvFile:
#     reader = csv.reader(csvFile)
#     for row in reader:
#         cell = row[1]
#         print(cell)
# csvFile.close()

# import csv

# with open('C:/Users/TechFerry/Downloads/ims_data_new.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row["ALPHA_2_MACROGLOBULIN"])

import numpy as np 
import csv
with open('C:/Users/TechFerry/Downloads/ims_data_new.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    average = 0
    sum = 0
    row_count = 0
    number_Arry = []
    limerick_line = []
    for row in reader:
        cell = row[10]
        if( cell !="NULL" and cell !="ALPHA_2_MACROGLOBULIN"):
            limerick_line.append(cell)
    for item in limerick_line:
        number_Arry.append( float(item))
    # print("List after removal of NULL values : " + str(limerick_line))       
    # print(np.median(float(limerick_line))) 
    print(np.median(number_Arry))
csvFile.close()

#  with open(csv):
#     reader = csv.reader(csvFile)
#     average = 0
#     Sum = 0
#     row_count = 0
#     for row in f:
#         for column in row[3]:
#             n = column
#             Sum += n
#         row_count += 1
#     average = Sum / len(column)
#     f.close()

# import csv

# mass_list = []
# with open("C:/Users/TechFerry/Downloads/ims_data_new.csv", "r") as f:
#     reader = csv.DictReader(f, delimiter="\t")
#     for row in reader:
#         print(row)
#         # mass = row["ALPHA_2_MACROGLOBULIN"]
#         # if mass is not None and mass is not "--":
#         #     mass_list.append(float(row["mass"]))

# avg_mass = sum(mass_list) / len(mass_list)

# import pandas as pd
# df = pd.read_csv (r'C:/Users/TechFerry/Downloads/ims_data_new.csv')
# print (df["ALPHA_2_MACROGLOBULIN"])