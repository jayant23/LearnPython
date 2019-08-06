#import pandas
import pandas as pd
import csv
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt 
import random
import numpy as np

col_names = 'AGE_AT_ENROLLMENT,AGE_AT_TEST,HEIGHT_M,WEIGHT_KG,BMI,AST,ALT'
col_names = col_names.split(',')
# load dataset
def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
  
    return res 
Data = pd.read_csv('C:/Users/TechFerry/Downloads/ims_data_converted.csv',sep=',', usecols =col_names)
Datalength = len(Data)

randomData =[]

for i in range(Datalength):
	randomData.append(random.randint(0,1))

Data.insert(7,'Fibronestics',randomData)

print(Data.head())

feature_cols = ['AGE_AT_ENROLLMENT', 'AGE_AT_TEST', 'HEIGHT_M', 'WEIGHT_KG','BMI', 'AST','ALT']
X = Data[feature_cols] # Features
Y = Data["Fibronestics"]

# split X and y into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=0)


# instantiate the model (using the default parameters)
logreg = LogisticRegression()

# fit the model with data
logreg.fit(X_train,y_train)
print(logreg.coef_)
