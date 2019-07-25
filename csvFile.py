
import pandas as pd

df = pd.read_csv (r'C:/Users/TechFerry/Downloads/ims_data_new.csv')
for i in df["ALPHA_2_MACROGLOBULIN"].fillna(0):
    print(i)

    dfObj = pd.DataFrame(i, columns=['median'])
    dfObj = dfObj.sort_values(by ='median' )
 
print("Contents of Sorted Dataframe based on a single column 'median' : ")
print(dfObj)