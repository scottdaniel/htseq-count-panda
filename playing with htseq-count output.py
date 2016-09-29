import os
os.chdir("Desktop")

import pandas as pd

df = pd.read_table("RNA_1.rawcounts",header=None)

sum = df.sum(0)

