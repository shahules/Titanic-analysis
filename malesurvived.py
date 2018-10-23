
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import os
import pylab as plt

os.chdir("Desktop//python exp docs")
df=pd.read_csv("train.csv")

age_bins=[0,18,25,40,60,100]
df["Age_bins"]=pd.cut(df.Age,bins=age_bins)
temp=df[np.isfinite(df["Age"])]
total_pas=temp.groupby("Age_bins")["Survived"].agg("count")
survived=temp.groupby("Age_bins")["Survived"].agg(sum)
print(type(survived.index.tolist()))
plt.pie(survived,labels=survived.index.tolist(),autopct='%1.1f%%',shadow=True,startangle=90)
plt.title("NO of survivors based on age groups pie charts")
plt.show()


# In[ ]:



