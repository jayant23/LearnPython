# Import pandas package 
import pandas as pd 
import numpy as np 
	
# making data frame 
df = pd.read_csv('C:/Users/TechFerry/Downloads/ims_data_new.csv',sep=";") 
df = df.set_index("PATIENT_ID")
df = df.fillna(df.median())
df = pd.DataFrame(df)
# df.to_csv('file5_ims_data.csv', sep =";") 

def showfullName(fname,lname):
    print(fname+lname) 
showfullName("jayant","sharma")    
# c = df.select_dtypes(np.number).columns
# j=0
# for i in c:
 
#     print(i)
#     df = df[i].fillna(df[i].median())
#     df = pd.DataFrame(df)
#     print(df)
#     j  +=1

    # df.to_csv('file4_ims_data.csv', sep =";")  

# df[c]= df[c].fillna(df['ALPHA_2_MACROGLOBULIN'].median())

# df = pd.DataFrame(df['ALPHA_2_MACROGLOBULIN']) 
  
# df.to_csv('file3_ims_data.csv', sep =";") 
