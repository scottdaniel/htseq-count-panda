import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
s

dates = pd.date_range('20130101', periods=6)
dates

df = 0
df = pd.DataFrame(np.random.randn(6,4), index=dates,
    columns=list('ABCD'))
df

df2 = pd.DataFrame( { 'A' : 1.,
                        'B' : pd.Timestamp('20130102'),
                        'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                        'D' : np.array([3] * 4,dtype='int32'),
                        'E' : pd.Categorical(["test","train","test","train"]),
                        'F' : 'foo' })
df2
df2.dtypes
df2.sort_values('E')

df.head()
df.tail(1)
df.index
df.columns
df.values
df.describe()
df.T
df.sort_index(axis=1, ascending=False)
df.sort_values('B')
df['A']
df[0:3]
df.loc[dates[0]]
df.loc[:,['A','B']]
df[df.A > 0]
df[df > 0]
df2 = df.copy()
df2['E'] = ['one','one', 'two', 'three', 'four', 'three']
df2
df2[df2['E'].isin(['two','four'])]

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130101', periods=6))
s1
df['F'] = s1
df
df.at[dates[0],'A'] = 0
df
df.iat[0,1]=0
df
df.loc[:,'D'] = np.array([5] * len(df))
df
df > 0
df['sum'] = df.apply(func=sum,axis=1)
df
df[df['sum']>7]

