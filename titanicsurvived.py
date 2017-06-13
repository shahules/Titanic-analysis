
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import os
import pylab as plt
os.chdir("Desktop/python exp docs")
df=pd.read_csv("train.csv")
survivors=df.groupby("Pclass")["Survived"].aggregate(sum)
fig=plt.figure()
ax=fig.add_subplot(111)
rect=ax.bar(survivors.index.values.tolist(),survivors,color="c",width=0.5)
ax.set_ylabel("No. of survivors")
ax.set_xlabel("Class type")
ax.set_title("total number of survivors based on class")
xTickMarks=(survivors.index.values.tolist())
ax.set_xticks=(survivors.index.values.tolist)
xtickNames=ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames,fontsize=25)
plt.show()


# In[9]:




# In[5]:




# In[5]:




# In[5]:




# In[5]:




# In[ ]:



