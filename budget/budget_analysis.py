import pandas as pd
import matplotlib as plt
from plotnine import *
from plotnine import *

import matplotlib.font_manager as fm
fontpath = 'C:/Windows/Fonts/NanumBarunGothic.ttf'
font_name = fm.FontProperties(fname=fontpath, size=15).get_name()
plt.rc('font', family=font_name)

budget_2010  = pd.read_csv('budget_2010.csv', encoding='utf-8' ).copy

# def branch(district):
#     district_2010 = budget_2010[]
# 함수만드는 중


JEJU_2010  = budget_2010[budget_2010['자치단체명'].str.contains('제주본청',regex=True)]
JEJU_2010 = JEJU_2010[['자치단체명','분야명','세출결산액']].copy()
JEJU_2010 = JEJU_2010.groupby(['분야명']).sum()
JEJU_2010['분야별비율'] = JEJU_2010['세출결산액']
JEJU_2010['분야별비율'] = (JEJU_2010['분야별비율']/ JEJU_2010['세출결산액'].sum()) * 100
