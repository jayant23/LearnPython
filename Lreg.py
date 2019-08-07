#import pandas
import pandas as pd
import csv
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt 
import random
import numpy as np
from sklearn import metrics

col_names = 'AGE_AT_ENROLLMENT,AGE_AT_TEST,HEIGHT_M,WEIGHT_KG,BMI,AST,ALT,FIBRONESTICS'
col_names = col_names.split(',')
# load dataset
def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
        
  
    return res 
Data = pd.read_csv('C:/Users/TechFerry/Downloads/ims_data_converted.csv',sep=',', usecols =col_names).dropna()

feature_cols = ['AGE_AT_ENROLLMENT', 'AGE_AT_TEST', 'HEIGHT_M', 'WEIGHT_KG','BMI', 'AST','ALT','FIBRONESTICS']
X = Data[feature_cols] # Features
Y = Data["FIBRONESTICS"]

# split X and y into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=0)

# instantiate the model (using the default parameters)
logreg = LogisticRegression()
y_train = y_train.fillna(0)
# fit the model with data
logreg.fit(X_train,y_train)
y_pred=logreg.predict(X_test)
print(logreg.coef_)
print(y_pred)
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(cnf_matrix)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
