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

df
df1 = df.reindex(index=dates[0:4],columns=list(df.columns) + ['E'])
df1
df1.loc[dates[0]:dates[1],'E'] = 1
df1.dropna(how='any')
df1.fillna(value=5)
pd.isnull(df1)
df.mean()
df.mean(1)
s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
s
df.sub(s,axis='index')

df.apply(np.cumsum)
df.apply(lambda x: x.max() - x.min())

s = pd.Series(np.random.randint(0, 7, size=10))
s
s.value_counts()
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s
s.str.lower()
df = pd.DataFrame(np.random.randn(10, 4))
df
pieces = [df[:3], df[3:7], df[7:]]
pieces
pieces[2]
pd.concat(pieces)

left = pd.DataFrame({'key': ['foo', 'foo','bar'], 'lval': [1, 2, 3]})
left
right = pd.DataFrame({'key': ['foo', 'foo','baz'], 'rval': [4, 5, 6]})
right
pd.merge(left,right,on='key',how='inner')
pd.merge(left,right,on='key',how='right')
pd.merge(left,right,on='key',how='left')
pd.merge(left,right,on='key',how='outer')

df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
df
s = df.iloc[3]
s
df.append(s,ignore_index=True)

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
   ....:                           'foo', 'bar', 'foo', 'foo'],
   ....:                    'B' : ['one', 'one', 'two', 'three',
   ....:                           'two', 'two', 'one', 'three'],
   ....:                    'C' : np.random.randn(8),
   ....:                    'D' : np.random.randn(8)})
df
df.groupby('A').sum()
df.groupby(['A','B']).sum()

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
   ....:                      'foo', 'foo', 'qux', 'qux'],
   ....:                     ['one', 'two', 'one', 'two',
   ....:                      'one', 'two', 'one', 'two']]))
tuples
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
index
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df
df2 = df[:4]
df2
stacked = df2.stack()
stacked
stacked.unstack(0)

df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
   .....:                    'B' : ['A', 'B', 'C'] * 4,
   .....:                    'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
   .....:                    'D' : np.random.randn(12),
   .....:                    'E' : np.random.randn(12)})
df
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
