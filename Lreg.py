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
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
import seaborn as sns

col_names = 'AGE_AT_ENROLLMENT,AGE_AT_TEST,HEIGHT_M,WEIGHT_KG,BMI,AST,ALT,FIBRONESTICS'
col_names = col_names.split(',') 
# load dataset

Data = pd.read_csv('C:/Users/TechFerry/Downloads/ims_data_converted.csv',sep=',', usecols =col_names).dropna()

feature_cols = ['AGE_AT_ENROLLMENT', 'AGE_AT_TEST', 'HEIGHT_M', 'WEIGHT_KG','BMI', 'AST','ALT']
X = Data[feature_cols] # Features
Y = Data.FIBRONESTICS


# split X and y into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=0)


# instantiate the model (using the default parameters)
logreg = LogisticRegression()
y_train = y_train.dropna()
# fit the model with data
logreg.fit(X_train,y_train)
y_pred=logreg.predict(X_test)
print(logreg.coef_)
print(y_pred)


cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(cnf_matrix)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

class_name = [0,1] #name of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_name))
plt.xticks(tick_marks, class_name)
plt.yticks = (tick_marks,class_name)
#create heatmap

sns.heatmap(pd.DataFrame(cnf_matrix), annot = True,cmap = "YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")

plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
# plt.show()

#Linear Regression Equation:
p = np.poly1d(logreg.coef_[0])
print(np.poly1d(p))
# print(p())

 
# def FIBRONESTICS_TEST(x):
#     sum = 0
#     for i in logreg.coef_[0]:
#         sum = i+int(sum*x)
#     return sum    

def fiboresticsTest(x):
    j=0
    k=0
    sum =0
    if(len(x)==len(logreg.coef_[0])):
        for coef in logreg.coef_[0]:
            if(k==0):
                sum = sum+coef
            else:
                sum = sum+coef*x[j]
                j = 1+j
            k = 1+k
    return print(sum)
fiboresticsTest([30,33,1.79,95.85,29.91,58,95])
fiboresticsTest([47,0,1.57,58.06,23.55,0,0])
