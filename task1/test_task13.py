
# coding: utf-8

# In[1]:


from task1 import shape
from task1 import totalpop2010
import pandas as pd


# In[2]:


data = pd.read_csv("input.txt", sep=',', escapechar='\\', encoding='utf-16', header=0, engine='python', index_col=0, na_values=['NA', '--'])


# In[3]:


# Task 1.3 test that the number of rows in the data is 225 and number of columns is 31 (using the country as an index)
def test_shape():
    assert shape(data) == (225, 31)


# In[4]:


# Task 1.3 test that the world population according to the data table in 2010 is ca. 7065 million.
def test_totalpop2010():
    assert totalpop2010(data) == 7065

