# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 03:02:41 2018

@author: Deniz Timartas
"""
#This is the .py file we will use to generate 3D scatter graphs for each of the 3 year span.

#These are the modules we will be using. The 'as' here means that we will use the module in the code with an acronym.
import os
import plotly as py
import pandas as pd

#This is a 2 line code to use plotly 3D graphical analysis module in offline mode.
from plotly.offline import init_notebook_mode
py.offline.init_notebook_mode(connected=True)

#We have our data set in csv format, we show this csv's adress to a variable.
CSV_PATH = os.path.join('..','Projects','proj','transactions2.csv')

#Then we read thatdata set into a pandas dataframe variable called df. parse_dates function here forms our frame's
#date data in datetime format.
df = pd.read_csv(CSV_PATH, parse_dates=[11,10])

#We have 41 different type so we will use a cycle in range 41.
for i in range(41):

    #We will first hold a specific type_id's data in a dfx and then we will try to divide them in a range of a month.
    dfx = df[df['type_id']==i+1]

    #We also have some returns in out data set. These corrupt the outcome in many ways so we will get rid of them by
    #Just having the rows of purchase_prices that are over 1.
    dfx=dfx[dfx['purchase_price']>1]
    
    #We will then only take the information we will need which are 'date','purchase_price' and 'selling_price'
    dfx=dfx.iloc[:,[10,5,6]]

    #In this section we are trying to first set the data's lowest date limit and then set the highest to get only
    #a specific year data. We define 3 different dataframes to hold these data.
    df1 = dfx[dfx['date']>'2017-01-01']
    df1 = df1[df1['date']<'2018-01-01']
    df2 = dfx[dfx['date']>'2016-01-01']
    df2 = df2[df2['date']<'2017-01-01']
    df3 = dfx[dfx['date']>'2015-01-01']
    df3 = df3[df3['date']<'2016-01-01']
    
    #We need a dictionary and a cluster for each year so first we will form scatter dictionaries.
    #Here we define what mode we will use, you can look up different modes that fulfill your needs. The type is scatter3d.
    #We also define the x, y and z axis' columns here. We also set different colors for each group just to make it beautiful
    #and easier to distinguish.
    scatter1 = dict(
        mode = "markers",
        name = "x",
        type = "scatter3d",    
        x = df1['date'], y = df1['purchase_price'], z = df1['selling_price'],
        marker = dict( size=2, color="red" )
    )
    scatter2 = dict(
        mode = "markers",
        name = "y",
        type = "scatter3d",    
        x = df2['date'], y = df2['purchase_price'], z = df2['selling_price'],
        marker = dict( size=2, color="blue" )
    )
    scatter3 = dict(
        mode = "markers",
        name = "z",
        type = "scatter3d",    
        x = df3['date'], y = df3['purchase_price'], z = df3['selling_price'],
        marker = dict( size=2, color="green" )
    )
    
    #We also need clustering dictionaries, you can set opacity in range of 0-1 to make it opaque. Everything else
    #is similar to scatter.      
    clusters1 = dict(
        alphahull = 7,
        name = "x",
        opacity = 0.2,
        color='red',
        type = "mesh3d",    
        x = df1['date'], y = df1['purchase_price'], z = df1['selling_price']
    )
    clusters2 = dict(
        alphahull = 7,
        name = "y",
        opacity = 0.2,
        color='blue',
        type = "mesh3d",    
        x = df2['date'], y = df2['purchase_price'], z = df2['selling_price']
    )
    clusters3 = dict(
        alphahull = 7,
        name = "z",
        opacity = 0.2,
        color='green',
        type = "mesh3d",    
        x = df3['date'], y = df3['purchase_price'], z = df3['selling_price']
    )

    #Our data is ready to do some magic. Define the layout.
    layout = dict(
        title = '3d point clustering',
        scene = dict(
            xaxis = dict( zeroline=True ),
            yaxis = dict( zeroline=True ),
            zaxis = dict( zeroline=True ),
        )
    )
        
    #lets also make a dictionary for our figure.
    fig = dict( data=[scatter1, scatter2, scatter3, clusters1, clusters2, clusters3], layout=layout )
   
    #This code here will generate the html 3D graphs for us.
    # Use py.iplot() for IPython notebook.
    py.offline.plot(fig, filename=('Yillara_Gore_Satis_Fiyatlari_' + str(i+1) + '_3D'), validate='false')


