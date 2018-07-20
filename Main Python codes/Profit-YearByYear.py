# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 01:34:38 2018

@author: Deniz Timartas
"""
# In this .py file, we will be calculating the profit values for each year. There are some tricks and data
#manipulations we will use here.

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
df = pd.read_csv(CSV_PATH, parse_dates=[10,11])

#In this section we are trying to first set the data's lowest date limit and then set the highest to get only
#a specific year data. We define 3 different dataframes to hold these data.
df1 = df[df['date']>'2017-01-01']
df1 = df1[df1['date']<'2018-01-01']
df2 = df[df['date']>'2016-01-01']
df2 = df2[df2['date']<'2017-01-01']
df3 = df[df['date']>'2015-01-01']
df3 = df3[df3['date']<'2016-01-01']
df4 = df[df['date']>'2018-01-01']
df4 = df4[df4['date']<'2019-01-01']


#We will first define a variable we will use as index. freq='D' makes it day by day and we also give it a range.
dateindex1 = pd.date_range('2017-01-01','2017-12-31',freq='D')

# "df1.groupby(['date']).selling_price.sum()" here calculates the sum of selling prices for each date which is day by day.
# And we then deduct the purchase prices from the selling prices to calculate the profit.
ciro1 = df1.groupby(['date']).selling_price.sum()-df1.groupby(['date']).purchase_price.sum()

#We define a sum variable and an empty serie first
ciroseri1 = []
sum = 0

#Then we make a cycle that will calculate the sum of all profits. The outcome here will be a dataframe which has each rows value
#that is the sum of all previous rows plus itself.
for i in range(len(ciro1)):
    sum = sum + ciro1[i]
    ciroseri1.append(sum)

#We have some days that are missing, which probably are the holidays. We have 3 off days at 2017 so we append the last value at the end
#of the serie as many as off days.
ciroseri1.append(312580.0969999999)
ciroseri1.append(312580.0969999999)
ciroseri1.append(312580.0969999999)

#Last, we define our pandas serie we will use with an index.
dataq1 = pd.Series(ciroseri1,index=dateindex1)


#This part is the same thing for 2016.
dateindex2 = pd.date_range('2016-01-01','2016-12-31',freq='D')

ciro2 = df2.groupby(['date']).selling_price.sum()-df2.groupby(['date']).purchase_price.sum()

ciroseri2 = []
sum = 0

for i in range(len(ciro2)):
    sum = sum + ciro2[i]
    ciroseri2.append(sum)

ciroseri2.append(272856.26799999987)
ciroseri2.append(272856.26799999987)

dataq2 = pd.Series(ciroseri2,index=dateindex2)


#This part is the same thing for 2015.
dateindex3 = pd.date_range('2015-01-01','2015-12-31',freq='D')
ciro3 = df3.groupby(['date']).selling_price.sum()-df3.groupby(['date']).purchase_price.sum()

ciroseri3 = []
sum = 0
for i in range(len(ciro3)):
    sum = sum + ciro3[i]
    ciroseri3.append(sum)

ciroseri3.append(264371.2499999998)
ciroseri3.append(264371.2499999998)

dataq3 = pd.Series(ciroseri3,index=dateindex3)


#This part is the same thing for 2018, but we only have 4 months of data here.
dateindex4 = pd.date_range('2018-01-01','2018-04-19',freq='D')
ciro4 = df4.groupby(['date']).selling_price.sum()-df4.groupby(['date']).purchase_price.sum()

ciroseri4 = []
sum = 0
for i in range(len(ciro4)):
    sum = sum + ciro4[i]
    ciroseri4.append(sum)

ciroseri4.append(112621.78999999996)

dataq4 = pd.Series(ciroseri4,index=dateindex4)


#Now here we make a figure for each of the serie we just defined.
#There are many interface options here that are useful, you can look them up from python 
#handbooks but I will try to cover some of them here. Here we define matplotlib figure as fig variable.
#We will later use that to show and save the figure. In .plot function we define default x and y axis values
#and then rot will rotate the labels so they are not on each other. 'grid' will add a grid on the back to
#make it easier to understand the values. There are also x and y labels as well as the title over the graph.
#We will be repeating it for every other year and we have our profit values year by year incremented each day.
fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
dataq1.plot(x='Index', y='0',ax=subplot, rot=45, grid=True)
subplot.set_xlabel('2017')
subplot.set_ylabel('Kar')
subplot.locator_params(nbins=40, axis='x')
subplot.set_title('Zamana Bağlı 2017 Kar Toplamı')
fig.show()
fig.savefig('profit17.jpeg')

fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
dataq2.plot(x='Index', y='0',ax=subplot, rot=45, grid=True)
subplot.set_xlabel('2016')
subplot.set_ylabel('Kar')
subplot.locator_params(nbins=40, axis='x')
subplot.set_title('Zamana Bağlı 2016 Kar Toplamı')
fig.show()
fig.savefig('profit16.jpeg')

fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
dataq3.plot(x='Index', y='0',ax=subplot, rot=45, grid=True)
subplot.set_xlabel('2015')
subplot.set_ylabel('Kar')
subplot.locator_params(nbins=40, axis='x')
subplot.set_title('Zamana Bağlı 2015 Kar Toplamı')
fig.show()
fig.savefig('profit15.jpeg')

fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
dataq4.plot(x='Index', y='0',ax=subplot, rot=45, grid=True)
subplot.set_xlabel('2018')
subplot.set_ylabel('Kar')
subplot.locator_params(nbins=40, axis='x')
subplot.set_title('Zamana Bağlı 2018 Kar Toplamı')
fig.show()
fig.savefig('profit18.jpeg')