import pandas as pd
import matplotlib as plt
from plotnine import *

import matplotlib.font_manager as fm
fontpath = 'C:/Windows/Fonts/NanumBarunGothic.ttf'
font_name = fm.FontProperties(fname=fontpath, size=15).get_name()
plt.rc('font', family=font_name)

import os
os.chdir('data_path')
dirs = os.listdir()
print(dirs)

def time_series(district):

    result   = pd.DataFrame()
    year = 2010

    for f in dirs:

        df= pd.read_csv(f, encoding='utf-8' ).copy()
        df = df[df['자치단체명'].str.contains(district,regex=True)]
        df = df[['자치단체명','분야명','부문명','세출결산액']].copy()
        df = df.groupby(['분야명']).sum()
        df[str(year)] = df['세출결산액']
        df[str(year)] = (df[str(year)]/ df['세출결산액'].sum()) * 100
        df = df.drop(['세출결산액'],axis=1)

        if year < 2011:
            result = df
        else:
            df = df
            result =  pd.merge(result,df, on='분야명')
        year = year + 1
    return result

def time_plot_all(district):
    time_series(district).plot.bar()

def time_plot_category(district, category):
    time_series(district).loc[category].plot.line()
