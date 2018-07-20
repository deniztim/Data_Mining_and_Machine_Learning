# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 01:08:12 2018

@author: Deniz Timartas
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 03:02:41 2018

@author: Deniz Timartas
"""
#This is the .py file we will use to generate 3D scatter graphs for each of the 3 year span's every month.

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

    #In this long section we are trying to first set the datas lowest date limit and then set the highest to get only
    #a specific months data. And we also define 36 different dataframes for 36 different months.
    df1 = dfx[dfx['date']>'2017-12-01']
    df1 = df1[df1['date']<'2018-01-01']  
    
    df2 = dfx[dfx['date']>'2017-11-01']
    df2 = df2[df2['date']<'2017-12-01'] 
    
    df3 = dfx[dfx['date']>'2017-10-01']
    df3 = df3[df3['date']<'2017-11-01']
    
    df4 = dfx[dfx['date']>'2017-09-01']
    df4 = df4[df4['date']<'2017-10-01']
    
    df5 = dfx[dfx['date']>'2017-08-01']
    df5 = df5[df5['date']<'2017-09-01']
    
    df6 = dfx[dfx['date']>'2017-07-01']
    df6 = df6[df6['date']<'2017-08-01']
    
    df7 = dfx[dfx['date']>'2017-06-01']
    df7 = df7[df7['date']<'2017-07-01']
    
    df8 = dfx[dfx['date']>'2017-05-01']
    df8 = df8[df8['date']<'2017-06-01']
    
    df9 = dfx[dfx['date']>'2017-04-01']
    df9 = df9[df9['date']<'2017-05-01']
    
    df10 = dfx[dfx['date']>'2017-03-01']
    df10 = df10[df10['date']<'2017-04-01']
    
    df11 = dfx[dfx['date']>'2017-02-01']
    df11 = df11[df11['date']<'2017-03-01']
    
    df12 = dfx[dfx['date']>'2017-01-01']
    df12 = df12[df12['date']<'2017-02-01']
    
    df13 = dfx[dfx['date']>'2016-12-01']
    df13 = df13[df13['date']<'2017-01-01']
    
    df14 = dfx[dfx['date']>'2016-11-01']
    df14 = df14[df14['date']<'2016-12-01']
    
    df15 = dfx[dfx['date']>'2016-10-01']
    df15 = df15[df15['date']<'2016-11-01']
    
    df16 = dfx[dfx['date']>'2016-09-01']
    df16 = df16[df16['date']<'2016-10-01']
    
    df17 = dfx[dfx['date']>'2016-08-01']
    df17 = df17[df17['date']<'2016-09-01']
    
    df18 = dfx[dfx['date']>'2016-07-01']
    df18 = df18[df18['date']<'2016-08-01']
    
    df19 = dfx[dfx['date']>'2016-06-01']
    df19 = df19[df19['date']<'2016-07-01']
    
    df20 = dfx[dfx['date']>'2016-05-01']
    df20 = df20[df20['date']<'2016-06-01']
    
    df21 = dfx[dfx['date']>'2016-04-01']
    df21 = df21[df21['date']<'2016-05-01']
    
    df22 = dfx[dfx['date']>'2016-03-01']
    df22 = df22[df22['date']<'2016-04-01']
    
    df23 = dfx[dfx['date']>'2016-02-01']
    df23 = df23[df23['date']<'2016-03-01']
    
    df24 = dfx[dfx['date']>'2016-01-01']
    df24 = df24[df24['date']<'2016-02-01']
    
    df25 = dfx[dfx['date']>'2015-12-01']
    df25 = df25[df25['date']<'2016-01-01']
    
    df26 = dfx[dfx['date']>'2015-11-01']
    df26 = df26[df26['date']<'2015-12-01']
    
    df27 = dfx[dfx['date']>'2015-10-01']
    df27 = df27[df27['date']<'2015-11-01']
    
    df28 = dfx[dfx['date']>'2015-09-01']
    df28 = df28[df28['date']<'2015-10-01']
    
    df29 = dfx[dfx['date']>'2015-08-01']
    df29 = df29[df29['date']<'2015-09-01']
    
    df30 = dfx[dfx['date']>'2015-07-01']
    df30 = df30[df30['date']<'2015-08-01']
    
    df31 = dfx[dfx['date']>'2015-06-01']
    df31 = df31[df31['date']<'2015-07-01']
    
    df32 = dfx[dfx['date']>'2015-05-01']
    df32 = df32[df32['date']<'2015-06-01']
    
    df33 = dfx[dfx['date']>'2015-04-01']
    df33 = df33[df33['date']<'2015-05-01']
    
    df34 = dfx[dfx['date']>'2015-03-01']
    df34 = df34[df34['date']<'2015-04-01']
    
    df35 = dfx[dfx['date']>'2015-02-01']
    df35 = df35[df35['date']<'2015-03-01']
    
    df36 = dfx[dfx['date']>'2015-01-01']
    df36 = df36[df36['date']<'2015-02-01']

    #We need a dictionary and a cluster for each month so first we will form scatter dictionaries.
    #Here we define what mode we will use, you can look up different modes that fulfill your needs. The type is scatter3d.
    #We also define the x, y and z axis' columns here. we also set different colors for each group just to make it beautiful
    #and easier to distinguish.
    scatter1 = dict(
        mode = "markers",
        name = "1",
        type = "scatter3d",    
        x = df1['date'], y = df1['purchase_price'], z = df1['selling_price'],
        marker = dict( size=2, color="b" )
    )
    scatter2 = dict(
        mode = "markers",
        name = "2",
        type = "scatter3d",    
        x = df2['date'], y = df2['purchase_price'], z = df2['selling_price'],
        marker = dict( size=2, color="g" )
    )
    scatter3 = dict(
        mode = "markers",
        name = "3",
        type = "scatter3d",    
        x = df3['date'], y = df3['purchase_price'], z = df3['selling_price'],
        marker = dict( size=2, color="r" )
    )
    scatter4 = dict(
        mode = "markers",
        name = "4",
        type = "scatter3d",    
        x = df4['date'], y = df4['purchase_price'], z = df4['selling_price'],
        marker = dict( size=2, color="c" )
    )
    scatter5 = dict(
        mode = "markers",
        name = "5",
        type = "scatter3d",    
        x = df5['date'], y = df5['purchase_price'], z = df5['selling_price'],
        marker = dict( size=2, color="m" )
    )
    scatter6 = dict(
        mode = "markers",
        name = "6",
        type = "scatter3d",    
        x = df6['date'], y = df6['purchase_price'], z = df6['selling_price'],
        marker = dict( size=2, color="y" )
    )
    scatter7 = dict(
        mode = "markers",
        name = "7",
        type = "scatter3d",    
        x = df7['date'], y = df7['purchase_price'], z = df7['selling_price'],
        marker = dict( size=2, color="k" )
    )
    scatter8 = dict(
        mode = "markers",
        name = "8",
        type = "scatter3d",    
        x = df8['date'], y = df8['purchase_price'], z = df8['selling_price'],
        marker = dict( size=2, color="w" )
    )
    scatter9 = dict(
        mode = "markers",
        name = "9",
        type = "scatter3d",    
        x = df9['date'], y = df9['purchase_price'], z = df9['selling_price'],
        marker = dict( size=2, color="b" )
    )
    scatter10 = dict(
        mode = "markers",
        name = "10",
        type = "scatter3d",    
        x = df10['date'], y = df10['purchase_price'], z = df10['selling_price'],
        marker = dict( size=2, color="g" )
    )
    scatter11 = dict(
        mode = "markers",
        name = "11",
        type = "scatter3d",    
        x = df11['date'], y = df11['purchase_price'], z = df11['selling_price'],
        marker = dict( size=2, color="r" )
    )
    scatter12 = dict(
        mode = "markers",
        name = "12",
        type = "scatter3d",    
        x = df12['date'], y = df12['purchase_price'], z = df12['selling_price'],
        marker = dict( size=2, color="c" )
    )
    scatter13 = dict(
        mode = "markers",
        name = "13",
        type = "scatter3d",    
        x = df13['date'], y = df13['purchase_price'], z = df13['selling_price'],
        marker = dict( size=2, color="m" )
    )
    scatter14 = dict(
        mode = "markers",
        name = "14",
        type = "scatter3d",    
        x = df14['date'], y = df14['purchase_price'], z = df14['selling_price'],
        marker = dict( size=2, color="y" )
    )
    scatter15 = dict(
        mode = "markers",
        name = "15",
        type = "scatter3d",    
        x = df15['date'], y = df15['purchase_price'], z = df15['selling_price'],
        marker = dict( size=2, color="k" )
    )
    scatter16 = dict(
        mode = "markers",
        name = "16",
        type = "scatter3d",    
        x = df16['date'], y = df16['purchase_price'], z = df16['selling_price'],
        marker = dict( size=2, color="w" )
    )
    scatter17 = dict(
        mode = "markers",
        name = "17",
        type = "scatter3d",    
        x = df17['date'], y = df17['purchase_price'], z = df17['selling_price'],
        marker = dict( size=2, color="b" )
    )
    scatter18 = dict(
        mode = "markers",
        name = "18",
        type = "scatter3d",    
        x = df18['date'], y = df18['purchase_price'], z = df18['selling_price'],
        marker = dict( size=2, color="g" )
    )
    scatter19 = dict(
        mode = "markers",
        name = "19",
        type = "scatter3d",    
        x = df19['date'], y = df19['purchase_price'], z = df19['selling_price'],
        marker = dict( size=2, color="r" )
    )
    scatter20 = dict(
        mode = "markers",
        name = "20",
        type = "scatter3d",    
        x = df20['date'], y = df20['purchase_price'], z = df20['selling_price'],
        marker = dict( size=2, color="c" )
    )
    scatter21 = dict(
        mode = "markers",
        name = "21",
        type = "scatter3d",    
        x = df21['date'], y = df21['purchase_price'], z = df21['selling_price'],
        marker = dict( size=2, color="m" )
    )
    scatter22 = dict(
        mode = "markers",
        name = "22",
        type = "scatter3d",    
        x = df22['date'], y = df22['purchase_price'], z = df22['selling_price'],
        marker = dict( size=2, color="y" )
    )
    scatter23 = dict(
        mode = "markers",
        name = "23",
        type = "scatter3d",    
        x = df23['date'], y = df23['purchase_price'], z = df23['selling_price'],
        marker = dict( size=2, color="k" )
    )
    scatter24 = dict(
        mode = "markers",
        name = "24",
        type = "scatter3d",    
        x = df24['date'], y = df24['purchase_price'], z = df24['selling_price'],
        marker = dict( size=2, color="w" )
    )
    scatter25 = dict(
        mode = "markers",
        name = "25",
        type = "scatter3d",    
        x = df25['date'], y = df25['purchase_price'], z = df25['selling_price'],
        marker = dict( size=2, color="b" )
    )
    scatter26 = dict(
        mode = "markers",
        name = "26",
        type = "scatter3d",    
        x = df26['date'], y = df26['purchase_price'], z = df26['selling_price'],
        marker = dict( size=2, color="g" )
    )
    scatter27 = dict(
        mode = "markers",
        name = "27",
        type = "scatter3d",    
        x = df27['date'], y = df27['purchase_price'], z = df27['selling_price'],
        marker = dict( size=2, color="r" )
    )
    scatter28 = dict(
        mode = "markers",
        name = "28",
        type = "scatter3d",    
        x = df28['date'], y = df28['purchase_price'], z = df28['selling_price'],
        marker = dict( size=2, color="c" )
    )
    scatter29 = dict(
        mode = "markers",
        name = "29",
        type = "scatter3d",    
        x = df29['date'], y = df29['purchase_price'], z = df29['selling_price'],
        marker = dict( size=2, color="m" )
    )
    scatter30 = dict(
        mode = "markers",
        name = "30",
        type = "scatter3d",    
        x = df30['date'], y = df30['purchase_price'], z = df30['selling_price'],
        marker = dict( size=2, color="y" )
    )
    scatter31 = dict(
        mode = "markers",
        name = "31",
        type = "scatter3d",    
        x = df31['date'], y = df31['purchase_price'], z = df31['selling_price'],
        marker = dict( size=2, color="k" )
    )
    scatter32 = dict(
        mode = "markers",
        name = "32",
        type = "scatter3d",    
        x = df32['date'], y = df32['purchase_price'], z = df32['selling_price'],
        marker = dict( size=2, color="w" )
    )
    scatter33 = dict(
        mode = "markers",
        name = "33",
        type = "scatter3d",    
        x = df33['date'], y = df33['purchase_price'], z = df33['selling_price'],
        marker = dict( size=2, color="b" )
    )
    scatter34 = dict(
        mode = "markers",
        name = "34",
        type = "scatter3d",    
        x = df34['date'], y = df34['purchase_price'], z = df34['selling_price'],
        marker = dict( size=2, color="g" )
    )
    scatter35 = dict(
        mode = "markers",
        name = "35",
        type = "scatter3d",    
        x = df35['date'], y = df35['purchase_price'], z = df35['selling_price'],
        marker = dict( size=2, color="r" )
    )
    scatter36 = dict(
        mode = "markers",
        name = "36",
        type = "scatter3d",    
        x = df36['date'], y = df36['purchase_price'], z = df36['selling_price'],
        marker = dict( size=2, color="c" )
    )
                        
    #We also need clustering dictionaries, you can set opacity in range of 0-1 to make it opaque. Everything else
    #is similar to scatter.                                                                 
    clusters1 = dict(
        alphahull = 7,
        name = "1",
        opacity = 0.15,
        color='b',
        type = "mesh3d",    
        x = df1['date'], y = df1['purchase_price'], z = df1['selling_price']
    )
    clusters2 = dict(
        alphahull = 7,
        name = "2",
        opacity = 0.15,
        color='g',
        type = "mesh3d",    
        x = df2['date'], y = df2['purchase_price'], z = df2['selling_price']
    )
    clusters3 = dict(
        alphahull = 7,
        name = "3",
        opacity = 0.15,
        color='r',
        type = "mesh3d",    
        x = df3['date'], y = df3['purchase_price'], z = df3['selling_price']
    )
    clusters4 = dict(
        alphahull = 7,
        name = "4",
        opacity = 0.15,
        color='c',
        type = "mesh3d",    
        x = df4['date'], y = df4['purchase_price'], z = df4['selling_price']
    )
    clusters5 = dict(
        alphahull = 7,
        name = "5",
        opacity = 0.15,
        color='m',
        type = "mesh3d",    
        x = df5['date'], y = df5['purchase_price'], z = df5['selling_price']
    )
    clusters6 = dict(
        alphahull = 7,
        name = "6",
        opacity = 0.15,
        color='y',
        type = "mesh3d",    
        x = df6['date'], y = df6['purchase_price'], z = df6['selling_price']
    )
    clusters7 = dict(
        alphahull = 7,
        name = "7",
        opacity = 0.15,
        color='k',
        type = "mesh3d",    
        x = df7['date'], y = df7['purchase_price'], z = df7['selling_price']
    )
    clusters8 = dict(
        alphahull = 7,
        name = "8",
        opacity = 0.15,
        color='w',
        type = "mesh3d",    
        x = df8['date'], y = df8['purchase_price'], z = df8['selling_price']
    )
    clusters9 = dict(
        alphahull = 7,
        name = "9",
        opacity = 0.15,
        color='b',
        type = "mesh3d",    
        x = df9['date'], y = df9['purchase_price'], z = df9['selling_price']
    )
    clusters10 = dict(
        alphahull = 7,
        name = "10",
        opacity = 0.15,
        color='g',
        type = "mesh3d",    
        x = df10['date'], y = df10['purchase_price'], z = df10['selling_price']
    )
    clusters11 = dict(
        alphahull = 7,
        name = "11",
        opacity = 0.15,
        color='r',
        type = "mesh3d",    
        x = df11['date'], y = df11['purchase_price'], z = df11['selling_price']
    )
    clusters12 = dict(
        alphahull = 7,
        name = "12",
        opacity = 0.15,
        color='c',
        type = "mesh3d",    
        x = df12['date'], y = df12['purchase_price'], z = df12['selling_price']
    )
    clusters13 = dict(
        alphahull = 7,
        name = "13",
        opacity = 0.15,
        color='m',
        type = "mesh3d",    
        x = df13['date'], y = df13['purchase_price'], z = df13['selling_price']
    )
    clusters14 = dict(
        alphahull = 7,
        name = "14",
        opacity = 0.15,
        color='y',
        type = "mesh3d",    
        x = df14['date'], y = df14['purchase_price'], z = df14['selling_price']
    )
    clusters15 = dict(
        alphahull = 7,
        name = "15",
        opacity = 0.15,
        color='k',
        type = "mesh3d",    
        x = df15['date'], y = df15['purchase_price'], z = df15['selling_price']
    )
    clusters16 = dict(
        alphahull = 7,
        name = "16",
        opacity = 0.15,
        color='w',
        type = "mesh3d",    
        x = df16['date'], y = df16['purchase_price'], z = df16['selling_price']
    )
    clusters17 = dict(
        alphahull = 7,
        name = "17",
        opacity = 0.15,
        color='b',
        type = "mesh3d",    
        x = df17['date'], y = df17['purchase_price'], z = df17['selling_price']
    )
    clusters18 = dict(
        alphahull = 7,
        name = "18",
        opacity = 0.15,
        color='g',
        type = "mesh3d",    
        x = df18['date'], y = df18['purchase_price'], z = df18['selling_price']
    )
    clusters19 = dict(
        alphahull = 7,
        name = "19",
        opacity = 0.15,
        color='r',
        type = "mesh3d",    
        x = df19['date'], y = df19['purchase_price'], z = df19['selling_price']
    )
    clusters20 = dict(
        alphahull = 7,
        name = "20",
        opacity = 0.15,
        color='c',
        type = "mesh3d",    
        x = df20['date'], y = df20['purchase_price'], z = df20['selling_price']
    )
    clusters21 = dict(
        alphahull = 7,
        name = "21",
        opacity = 0.15,
        color='m',
        type = "mesh3d",    
        x = df21['date'], y = df21['purchase_price'], z = df21['selling_price']
    )
    clusters22 = dict(
        alphahull = 7,
        name = "22",
        opacity = 0.15,
        color='y',
        type = "mesh3d",    
        x = df22['date'], y = df22['purchase_price'], z = df22['selling_price']
    )
    clusters23 = dict(
        alphahull = 7,
        name = "23",
        opacity = 0.15,
        color='k',
        type = "mesh3d",    
        x = df23['date'], y = df23['purchase_price'], z = df23['selling_price']
    )
    clusters24 = dict(
        alphahull = 7,
        name = "24",
        opacity = 0.15,
        color='w',
        type = "mesh3d",    
        x = df24['date'], y = df24['purchase_price'], z = df24['selling_price']
    )
    clusters25 = dict(
        alphahull = 7,
        name = "25",
        opacity = 0.15,
        color='b',
        type = "mesh3d",    
        x = df25['date'], y = df25['purchase_price'], z = df25['selling_price']
    )
    clusters26 = dict(
        alphahull = 7,
        name = "26",
        opacity = 0.15,
        color='g',
        type = "mesh3d",    
        x = df26['date'], y = df26['purchase_price'], z = df26['selling_price']
    )
    clusters27 = dict(
        alphahull = 7,
        name = "27",
        opacity = 0.15,
        color='r',
        type = "mesh3d",    
        x = df27['date'], y = df27['purchase_price'], z = df27['selling_price']
    )
    clusters28 = dict(
        alphahull = 7,
        name = "28",
        opacity = 0.15,
        color='c',
        type = "mesh3d",    
        x = df28['date'], y = df28['purchase_price'], z = df28['selling_price']
    )
    clusters29 = dict(
        alphahull = 7,
        name = "29",
        opacity = 0.15,
        color='m',
        type = "mesh3d",    
        x = df29['date'], y = df29['purchase_price'], z = df29['selling_price']
    )
    clusters30 = dict(
        alphahull = 7,
        name = "30",
        opacity = 0.15,
        color='y',
        type = "mesh3d",    
        x = df30['date'], y = df30['purchase_price'], z = df30['selling_price']
    )
    clusters31 = dict(
        alphahull = 7,
        name = "31",
        opacity = 0.15,
        color='k',
        type = "mesh3d",    
        x = df31['date'], y = df31['purchase_price'], z = df31['selling_price']
    )
    clusters32 = dict(
        alphahull = 7,
        name = "32",
        opacity = 0.15,
        color='w',
        type = "mesh3d",    
        x = df32['date'], y = df32['purchase_price'], z = df32['selling_price']
    )
    clusters33 = dict(
        alphahull = 7,
        name = "33",
        opacity = 0.15,
        color='m',
        type = "mesh3d",    
        x = df33['date'], y = df33['purchase_price'], z = df33['selling_price']
    )
    clusters34 = dict(
        alphahull = 7,
        name = "34",
        opacity = 0.15,
        color='y',
        type = "mesh3d",    
        x = df34['date'], y = df34['purchase_price'], z = df34['selling_price']
    )
    clusters35 = dict(
        alphahull = 7,
        name = "35",
        opacity = 0.15,
        color='k',
        type = "mesh3d",    
        x = df35['date'], y = df35['purchase_price'], z = df35['selling_price']
    )
    clusters36 = dict(
        alphahull = 7,
        name = "36",
        opacity = 0.15,
        color='w',
        type = "mesh3d",    
        x = df36['date'], y = df36['purchase_price'], z = df36['selling_price']
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
    fig = dict( data=[scatter1, scatter2, scatter3, scatter4, scatter5, scatter6, scatter7, scatter8, scatter9, scatter10,
                      scatter11, scatter12, scatter13, scatter14, scatter15, scatter16, scatter17, scatter18, scatter19, scatter20,
                      scatter21, scatter22, scatter23, scatter24, scatter25, scatter26, scatter27, scatter28, scatter29, scatter30,
                      scatter31, scatter32, scatter33, scatter34, scatter35, scatter36,
                      clusters1, clusters2, clusters3, clusters4, clusters5, clusters6, clusters7, clusters8, clusters9, clusters10,
                      clusters11, clusters12, clusters13, clusters14, clusters15, clusters16, clusters17, clusters18, clusters19, clusters20,
                      clusters21, clusters22, clusters23, clusters24, clusters25, clusters26, clusters27, clusters28, clusters29, clusters30,
                      clusters31, clusters32, clusters33, clusters34, clusters35, clusters36], layout=layout )
    
    #This code here will generate the html 3D graphs for us.
    # Use py.iplot() for IPython notebook.
    py.offline.plot(fig, filename=('Aylara_Gore_Satis_' + str(i+1) + '_3D'), validate='false')


