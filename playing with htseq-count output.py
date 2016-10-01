import os
os.chdir("/Users/Scott/htseq-count-panda/")

import pandas as pd

df = pd.read_table("counts/RNA_1.rawcounts",header=None)
df.tail
df2 = df[1:2794]
sum(df2.loc[:,1])

df3 = df2[df2.loc[:,1]>0]
df3.sort(1)
df.tail
print("I don't think this is the right {} counts").format("raw")

df3.head(5)

for index, row in df3.iterrows():
    print("This is the name of the gene: {} \
    and this is the value: {}").format(row[0],row[1])
    