# -*- coding: utf-8 -*-
"""
Created on Sat May 19 23:56:37 2018

@author: Deniz Timartas
"""
#First things first, everything actually starts here, we have a dataframe and we dont yet know what it has inside it.
#So here we will show some data mining techniques to understand the data and here on we will decide how to use them.

#These are the modules we will be using. The 'as' here means that we will use the module in the code with an acronym.
import pandas as pd
import os

#We have our data set in csv format, we show this csv's adress to a variable.
CSV_PATH = os.path.join('..','Projects','proj','transactions2.csv')

#Then we read thatdata set into a pandas dataframe variable called df.
df = pd.read_csv(CSV_PATH)

#If you need a pickle for some other research, you can also use these 2 lines according to that. But we will continue with csv.
df.to_pickle(os.path.join('..', 'Projects','proj', 'transactions.pickle'))
df = pd.read_pickle(os.path.join('..', 'Projects','proj', 'transactions.pickle'))

#After you have the df variable, you can inspect that variable to see whats inside.
#Here is the code that will give us the values only for the columns written inside.
df[['product_id', 'product_name']]

#Or you can use iloc to take a range of rows and columns
df2=df.iloc[ : ,2:4]

#This function calculates the sum of all selling_price and purchase_price rows.
df.selling_price.sum()
df.purchase_price.sum()

#We can also render our data like this to define some specific limits.
df1=df[df['purchase_price']>1]

#describe is an easier way to show the mean, median, maximum and minimum values, quantile over percentages, 
#variations and standard derivations. But when you need to use a specific data inside your code, you will use 
#the latter 8 line of codes according to your needs.
df1.describe()

df1.selling_price.mean()
df1.selling_price.median()
df1.selling_price.max()-df.selling_price.min()
df1.selling_price.quantile(.25)
df1.selling_price.quantile(.5)
df1.selling_price.quantile(.75)
df1.selling_price.var()
df1.selling_price.std()

#Here are some inline graphical plots. I will not cover all the details here as we will be using them in other codes.
#kind variable here defines the kind of graph we will use. 
df.selling_price.plot(kind='hist', title='Yapılan Satışlar için Histogram Grafiği', color='c', bins=20)
df.selling_price.plot(kind='kde', title='Satış Fiyatları İçin KDE Grafiği', color='c')

#Here is a complex use of groupby. We have two uniques process types and '.agg' here will show us the purchase_price
#and selling_price columns 'mean' according to these process types.
df.groupby(['process_type']).agg({'purchase_price':'mean','selling_price':'mean'})
