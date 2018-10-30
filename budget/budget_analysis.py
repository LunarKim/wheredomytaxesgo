import pandas as pd
import matplotlib as plt
from plotnine import *
from plotnine import *

import matplotlib.font_manager as fm
fontpath = 'C:/Windows/Fonts/NanumBarunGothic.ttf'
font_name = fm.FontProperties(fname=fontpath, size=15).get_name()
plt.rc('font', family=font_name)

import os
os.chdir('data_path.')
dirs = os.listdir()


def branch(district,year):

    for filename in dirs:
        if filename[7:11] == year:
            budget= pd.read_csv(filename, encoding='utf-8' ).copy()

            df = budget[budget['자치단체명'].str.contains(district,regex=True)]

            df = df[['회계연도','자치단체명','분야명','세출결산액']].copy()
            df = df.groupby(['회계연도','자치단체명','분야명']).sum()
            df['분야별비율'] = df['세출결산액']
            df['분야별비율'] = (df['분야별비율']/ df['세출결산액'].sum()) * 100
            print(df['분야별비율'].plot.bar())
        else:
            break
