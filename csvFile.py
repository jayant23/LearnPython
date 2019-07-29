import pandas as pd

df = pd.read_csv('C:/Users/TechFerry/Downloads/ims_data_new.csv',sep=";")
dataframe = pd.DataFrame(df)
# Convert the dictionary into DataFrame 
df = pd.DataFrame(df, columns = ['ALPHA_2_MACROGLOBULIN'])
print("Given Dataframe :\n", df) 
print("\nIterating over rows using iterrows() method :\n") 

for index, row in df.iterrows():
    if(row["ALPHA_2_MACROGLOBULIN"] != "nan"):
        print(df.apply(lambda row: df['ALPHA_2_MACROGLOBULIN'].median(),axis = 1))
    print (row["ALPHA_2_MACROGLOBULIN"]) 
    
df['ALPHA_2_MACROGLOBULIN'] = df.apply(lambda row: df['ALPHA_2_MACROGLOBULIN'].median(),axis = 1)
print(df['ALPHA_2_MACROGLOBULIN'].median())














# # Import pandas package  
# import pandas as pd  
    
# # making data frame  
# data = pd.read_csv("C:/Users/TechFerry/Downloads/nba.csv")  
  
# # calling head() method   
# # storing in new variable  
# data_top = data.head()  
    
# print(list(data_top.index.values) )


# import pandas as pd

# df = pd.read_csv('C:/Users/TechFerry/Downloads/ims_data_new.csv',sep=";")
# dataframe = pd.DataFrame(df)
# # Convert the dictionary into DataFrame 
# df = pd.DataFrame(df, columns = ['ALPHA_2_MACROGLOBULIN'])
# print("Given Dataframe :\n", df) 
# print("\nIterating over rows using iterrows() method :\n") 
  
# # iterate through each row and select  
# # 'Name' and 'Age' column respectively. 
# for index, row in df.iterrows():
#     if(row["ALPHA_2_MACROGLOBULIN"] != "nan"):
#         print(df.apply(lambda row: df['ALPHA_2_MACROGLOBULIN'].median(),axis = 1))
#     print (row["ALPHA_2_MACROGLOBULIN"]) 
# # for item in df['ALPHA_2_MACROGLOBULIN']:
# #     for index, row in df.iterrows():
# #         if(row["ALPHA_2_MACROGLOBULIN"] =="nan"):
# #             print(row["ALPHA_2_MACROGLOBULIN"])

       
    
#     # print(item)
# df['ALPHA_2_MACROGLOBULIN'] = df.apply(lambda row: df['ALPHA_2_MACROGLOBULIN'].median(),axis = 1)
# # print(df['ALPHA_2_MACROGLOBULIN'])
# # print(df['ALPHA_2_MACROGLOBULIN'].head(20))
# # print(df['ALPHA_2_MACROGLOBULIN'].describe())
# # for index, row in df.iterrows():
# #     print(row['ALPHA_2_MACROGLOBULIN'])
# print(df['ALPHA_2_MACROGLOBULIN'].median())

