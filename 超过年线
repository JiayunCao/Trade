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
d_ma['MA'] = d_ma.iloc[:,1].rolling(window=250).mean()
# print(d_ma[250:280])


col0 = d_ma.iloc[:,0]
col1 = d_ma.iloc[:,1]
col2 = d_ma.iloc[:,2]
for i in range(1,len(col1)-1):
        if(col1[i]>col2[i] and col1[i + 1]<col2[i + 1]):
            print("低于年线：",col0[i])
        elif (col1[i] < col2[i] and col1[i + 1] > col2[i + 1]):
            print("超过年线：",col0[i])
