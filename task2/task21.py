
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


# Read in dataset from csv file generated from the points on the web
dset = pd.read_csv("dset_task21.csv")


# In[6]:


# Recreated the first figure on the site
fig=plt.figure()
ax1 = plt.gca()
line1, = ax1.plot(dset['years'], dset['spending'], c='r', marker='D')
ax2 = ax1.twinx()
line2, = ax2.plot(dset['years'], dset['suicides'], c='black', marker='o')
ax1.set_ylabel("US spending on science (in billion dollars)")
ax2.set_ylabel("Hanging suicides")
ax2.legend((line1, line2), ("US spending on science", "Hanging suicides"))
ax1.set_xticks(np.arange(1999, 2010, 1.0))
ax1.set_yticks(np.arange(15, 31, 5.0))
ax2.set_yticks(np.arange(4000, 10001, 2000))
ax1.set_title("US spending on science, space, and technology \n correlates with \n Suicides by hanging, strangulation and suffocation \n Correlation: 99.79% (r=0.99789126)", fontsize='14')
plt.show()
fig.savefig('task21.png', bbox_inches='tight')

