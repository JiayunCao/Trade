import csv
import pandas as pd
import matplotlib.pyplot as plt


csv_file = "/Users/jiayuncao/Desktop/Finance/Qfinancedata/close.csv"
csv_data = pd.read_csv(csv_file, low_memory = False)#防止弹出警告

df = pd.DataFrame(csv_data)
df.drop(df.index[0:4687], inplace=True)  #选择起始日期
db=df[['trade_days','000656.SZ','000300.SH']]
db.reset_index(drop=True, inplace=True)
db.set_index('trade_days')

d_ma=db.copy()
d_ma['MA'] = d_ma.iloc[:,1].rolling(window=250).mean()#获得MA

d_ma['pct1'] = d_ma['000656.SZ'].pct_change(periods=90, fill_method=None, limit=None, freq=None)
d_ma['大盘pct2'] = d_ma['000300.SH'].pct_change(periods=90, fill_method=None, limit=None, freq=None)
d_ma.dropna(subset=['pct1'],inplace=True)

d_ma.reset_index(drop=True, inplace=True) #这里务必要reset_index 否则下面for循环不可用
d_ma['AR']=d_ma['pct1']-d_ma['pct2']

d_ma['涨跌'] = None #创建新的一列
col6 = d_ma.iloc[:,6] #AR列
col7 = d_ma.iloc[:,7] #涨跌列

#问题在这里
for i in range(len(col3) - 1):
    if col6[i] < 0:
        col7[i] = '跌'
    else:
        col7[i] = '涨'
