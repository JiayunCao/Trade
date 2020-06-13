import csv
import pandas as pd
import matplotlib.pyplot as plt


csv_file = "/Users/jiayuncao/Desktop/Q金融/close.csv"
csv_data = pd.read_csv(csv_file, low_memory = False)#防止弹出警告

df = pd.DataFrame(csv_data)
df.head(100)
df.drop(df.index[0:4687], inplace=True)  
db=df[['trade_days','000656.SZ']]
db.reset_index(drop=True, inplace=True)
db.head(100)
db.reset_index(drop=True, inplace=True)
db.set_index('trade_days')







d_ma=db.copy()
d_ma['pct'] = d_ma['000656.SZ'].pct_change(periods=90, fill_method=None, limit=None, freq=None)
v = d_ma[abs(d_ma['pct']) > 0.4]
pd.set_option('display.max_rows', None)
v['index'] = v.index.tolist()
print(v)
col4= v.iloc[:,4]
for i in range(1,len(col1)-1):
    if(col4[i]<(col4[i+1]-5)):
        print("这波涨幅时间",col0[i])
