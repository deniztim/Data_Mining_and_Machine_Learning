# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 23:40:57 2018

@author: Deniz Timartas
"""
#This is the .py file that makes a predictive model out of the data we have. Predictive models are the 
#models we use to predict future values some value's attribute according to the data we already had.

#These are the modules we will be using. The 'as' here means that we will use the module in the code with an acronym.
#We will use the default graphical style, ggplot here. ScikitLearn aka sklearn here is the core of our predictive code.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm
import os
import pandas as pd

#We have our data set in csv format, we show this csv's adress to a variable.
CSV_PATH = os.path.join('..','Projects','proj','transactions.csv')

#Then we read thatdata set into a pandas dataframe variable called df. parse_dates function here forms our frame's
#date data in datetime format.
df = pd.read_csv(CSV_PATH, parse_dates=[10])

#We will then only take the information we will need which are 'type','purchase_price' and 'selling_price' here.
df=df.iloc[:,[3,5,6]]

#We define 2 different dataframes for 2 types and only take the values that are consistent. The predictive models have very absurd
#outcomes for non-consistent values. So you gotta trim your data once you understand where the problem is.
df1=df[df['type']=='Mont']
df1=df1[df1['purchase_price']>1]

df2=df[df['type']=='Kupe']
df2=df2[df2['purchase_price']>1]

#Now we have the dataframes by types but we will predict the types by the purchase and selling price of a value so we dont need type
#columns here. After that we concatenate them.
df1=df1.iloc[:,[1,2]]
df2=df2.iloc[:,[1,2]]
X=pd.concat([df2,df1],ignore_index=True)

#So now we have the X frame as the values we have but now we gotta make another serie to show the scikitlearn. This serie will have zeros
#and ones as many as the values of dataframes we have. In this example we first add as many zeros as we have values of df2 and as many
#ones as df1.
Y = []
for i in range(581):
    Y.append(0)
    
for i in range(450):
    Y.append(1)

#All the trick is here, we 'fit' the data we have inside a model and train it with scikitlearn's svm module. This process may take
#longer for bigger datasets. You can define another kernel which could also be 'rbf' for a radial grouping. What this does is simply
#showing the first X data and define that datas group according to the 0 or 1 we have at Y serie's same index. Then it learns 
#to differentiate between different value's groups according to datas it learnt from X and Y.
model = svm.SVC(kernel='linear', C=1, gamma=1, degree=3, shrinking=True).fit(X,Y) 

#This figure code here is just to understand what actually is produced by our model.
fig = plt.figure()
w = model.coef_[0]
print(w)

a = -w[0] / w[1]

xx = np.linspace(0,12)
yy = a * xx - model.intercept_[0] / w[1]

h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(X.values[:, 0], X.values[:, 1], c = Y)
plt.legend()
plt.show()
fig.savefig('svm.jpeg')

#Now here we defined 2 different values to test if it predicts correct.
predictgroup1=np.array([[70, 50]])
predictgroup1=predictgroup1.reshape(1, 2)
predictgroup2=np.array([[70, 200]])
predictgroup2=predictgroup2.reshape(1, 2)

#And Voila, we have the outcomes right according to the graph we had. These codes' outcomes simply tells us that the machine thinks that
#the values we showed it belongs to the group 1 or 2.
print(model.predict(predictgroup1))
print(model.predict(predictgroup2))
