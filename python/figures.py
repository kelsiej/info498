# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:33:45 2020

@author: workworkwork
"""

import plotly_express
import plotly
import pandas as pd
import matplotlib as plt
from datetime import datetime
import datetime as dt
import numpy as np
import random
import seaborn as sns
import plotly.express as px

def read_csv(csv):
    df = pd.read_csv(csv)
    df['created_at'] = df['created_at'].apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
    return df

def timespan(df):      
    min_yr = df.created_at.min().year
    max_yr = df.created_at.max().year
    posts = []
    for i in range(max_yr - min_yr):
        posts.append(len(df[(df['created_at'] > str(max_yr - i - 2) + '-12-31') & 
                            (df['created_at'] < str(max_yr - i) + '-01-01')]))
    return posts

def timespan_df(count, name, years):
    df2 = pd.DataFrame()
    df2['year'] = years
    
    df2['count'] = count
    
   # ax = sns.lineplot(x="year", y="count", data=df2)
    fig = px.line(df2, x="year", y="count", title=name)
    fig.show()
    
    with open(name + '_plotly_graph.html', 'w') as f:
        f.write(fig.to_html(include_plotlyjs='cdn'))
    
    return df2
    


pontifex = read_csv("pontifex_tweets.csv")
pyears =  [2019, 2018, 2017, 2016, 2015, 2014, 2013]
posts = timespan(pontifex)
df2 = timespan_df(posts, "Pope Francis", pyears)

dl = read_csv("DalaiLama_tweets.csv")
year = [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010]
df_posts = timespan(dl)
dl_df2 = timespan_df(df_posts, "Dalai Lama", year)

