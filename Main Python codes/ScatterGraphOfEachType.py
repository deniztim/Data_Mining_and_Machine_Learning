# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 18:46:40 2018

@author: Deniz Timartas
"""
#This is a scatter graph named as warmth graph. This shows the density of sales and also their selling price
#according to each of the 3 year span's days. The reason we dont use scatter here is that scatter graphs only
#accepts integer values. And we also have datetime values in our case.

#These are the modules we will be using. The 'as' here means that we will use the module in the code with an acronym.
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout':True,
                 'axes.titlepad':20})

#We have our data set in csv format, we show this csv's adress to a variable.
CSV_PATH = os.path.join('..','Projects','proj','transactions2.csv')

#Then we read thatdata set into a pandas dataframe variable called df. parse_dates function here forms our frame's
#date data in datetime format.
df = pd.read_csv(CSV_PATH, parse_dates=[11,10])

#We have 41 different type so we will use a cycle in range 41.
for i in range(41):

    #We will first hold a specific type_id's data in a dataframe variable.
    df1 = df[df['type_id']==i+1]
    
    #We also have some returns in out data set. These corrupt the outcome in many ways so we will get rid of them by
    #Just having the rows of purchase_prices that are over 1.
    df1=df1[df1['purchase_price']>1]
    
    #Now we will define our figure to show and save.
    #There are many interface options here that are useful, you can look them up from python 
    #handbooks but I will try to cover some of them here. Here we define matplotlib figure as fig variable.
    #We will later use that to show and save the figure. In .plot function we define default x and y axis values
    #and then rot will rotate the labels so they are not on each other. There are also x and y labels as well 
    #as the title over the graph. The trick here is to define the style like in scatter graph. Which is a dot.
    #And then we use alpha value to make it a little opaque over a value range of 0-1. An Voila, we got a very valuable
    #and easy to mine data to use.
    fig = plt.figure()
    subplot = fig.add_subplot(1, 1, 1)
    df1.plot(x='date', y='selling_price',ax=subplot, rot=45, style='.', grid=True, alpha=0.15)
    subplot.set_xlabel('Dates')
    subplot.set_ylabel('Selling Prices')
    subplot.locator_params(nbins=40, axis='x')
    subplot.set_title('Warmth Graph of Selling Prices by Time')
    #If you add fig.show() here, you will be overwhelmed by 41 different graphs opened as tabs.
    fig.savefig('Warmth_Graph_Dates_Selling' + str(i+1) + '.jpeg')