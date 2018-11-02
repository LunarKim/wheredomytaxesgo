import pandas as pd
import matplotlib as plt
import numpy as np
from plotnine import *

import matplotlib.font_manager as fm
fontpath = 'C:/Windows/Fonts/NanumBarunGothic.ttf'
font_name = fm.FontProperties(fname=fontpath, size=15).get_name()
plt.rc('font', family=font_name)

import os
os.chdir('data_path.')
dirs = os.listdir()


def load_file(district, year):
    for filename in dirs:
        if filename[7:11] == year:
            budget= pd.read_csv(filename, encoding='utf-8' ).copy()
            df = budget[budget['자치단체명'].str.contains(district,regex=True)]
            df = df[['회계연도','자치단체명','분야명','부문명','세출결산액']].copy()
    return df

def branch(district,year):
        df = load_file(district, year).groupby(['회계연도','자치단체명','분야명']).sum()
        df['분야별비율'] = df['세출결산액']
        df['분야별비율'] = (df['분야별비율']/ df['세출결산액'].sum()) * 100
        print(df['분야별비율'].plot.bar())
        return df

def category(district, year, category):
        df = load_file(district,year)
        df1= df.groupby(['분야명'])[['세출결산액']].sum()
        df1['분야별비율']=(df1['세출결산액']/ df1['세출결산액'].sum()) * 100
        df1.columns = ['분야별결산액','분야별비율']
        df = pd.merge(df1,df,on='분야명')
        df['부문별비율'] = (df['세출결산액']/df['분야별결산액']) * 100
        select = df[(df['분야명'] == category)]
        select.groupby(['분야명','부문명'])[['부문별비율']].sum().plot.bar()
