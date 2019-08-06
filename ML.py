from sklearn.cluster import KMeans
import csv 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
  

X = np.array([[1,2],[1,4],[1,0],[10,2],[10,4],[10,0]])
KMeans = KMeans(n_clusters=2, random_state=0).fit(X)
csv.register_dialect('myDialect',delimiter = ';',quoting=csv.QUOTE_ALL,skipinitialspace=True)
def loadCSV(filename): 
    ''' 
    function to load dataset 
    '''
    with open(filename, 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            return (row[5], row[6],row[7],row[8],row[9],row[10],row[11])
    csvFile.close()

loadCSV('C:/Users/TechFerry/Downloads/ims_data_new.csv')    


def plot_logisticRegression_Func(ageAtEnrol, ageatTest, height, weight,BMI, AST,ALT):
    return 1.0/(1+np.exp(np.dot(ageAtEnrol,ageatTest,height,BMI
    ,AST,ALT)))

X, y = load_iris(return_X_y=True)
# print(X)
# print(y)
clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial')
# print(clf)

from sklearn.model_selection import train_test_split
X, y = np.arange(10).reshape((5,2)), range(5)
# print(X)
# print(y)
# array([[0, 1],
#        [2, 3],
#        [4, 5],
#        [6, 7],
#        [8, 9]])
# >>> list(y)


import matplotlib.pyplot as plt 
import numpy as np
from sklearn import datasets, linear_model, metrics 

# load the boston dataset 
boston = datasets.load_boston(return_X_y=False)
# defining feature matrix(X) and response vector(y) 
X = boston.data 
y = boston.target

# splitting X and y into training and testing sets 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, 
													random_state=1) 

# create linear regression object 
reg = linear_model.LinearRegression() 
# train the model using the training sets 
reg.fit(X_train, y_train) 

# regression coefficients 
print('Coefficients: \n', reg.coef_) 

# variance score: 1 means perfect prediction 
print('Variance score: {}'.format(reg.score(X_test, y_test))) 

# plot for residual error 

## setting plot style 
plt.style.use('fivethirtyeight') 

## plotting residual errors in training data 
plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train, 
			color = "green", s = 10, label = 'Train data') 

## plotting residual errors in test data 
plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test, 
			color = "blue", s = 10, label = 'Test data') 

## plotting line for zero residual error 
plt.hlines(y = 0, xmin = 0, xmax = 50, linewidth = 2) 

## plotting legend 
plt.legend(loc = 'upper right') 

## plot title 
plt.title("Residual errors") 

## function to show plot 
plt.show() 





import numpy as np 
import matplotlib.pyplot as plt 

def estimate_coef(x, y): 
	# number of observations/points 
	n = np.size(x) 

	# mean of x and y vector 
	m_x, m_y = np.mean(x), np.mean(y) 

	# calculating cross-deviation and deviation about x 
	SS_xy = np.sum(y*x) - n*m_y*m_x 
	SS_xx = np.sum(x*x) - n*m_x*m_x 

	# calculating regression coefficients 
	b_1 = SS_xy / SS_xx 
	b_0 = m_y - b_1*m_x 

	return(b_0, b_1) 

def plot_regression_line(x, y, b): 
	# plotting the actual points as scatter plot 
	plt.scatter(x, y, color = "m", 
			marker = "o", s = 30) 

	# predicted response vector 
	y_pred = b[0] + b[1]*x 

	# plotting the regression line 
	plt.plot(x, y_pred, color = "g") 

	# putting labels 
	plt.xlabel('x') 
	plt.ylabel('y') 

	# function to show plot 
	plt.show() 

def main(): 
	# observations 
	x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
	y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 

	# estimating coefficients 
	b = estimate_coef(x, y) 
	print("Estimated coefficients:\nb_0 = {} \\nb_1 = {}".format(b[0], b[1])) 

	# plotting regression line 
	plot_regression_line(x, y, b) 

if __name__ == "__main__": 
	main() 


# import
import numpy as np
import matplotlib.pyplot as plt

# generate random data-set
np.random.seed (0)
x = np.random.rand (100, 1)
y = 2 + 3 * x + np.random.rand (100, 1)

# plot
plt.scatter (x, y, s = 10)
plt.xlabel ( 'x')
plt.ylabel ( 'y')
plt.show ()
