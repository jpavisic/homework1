
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


# Task 1 (1.2): Function fib computes the Fibonacci sequence, returning the nth value.
def fib(n):
    if n<2:
        return n
    return fib(n-2)+fib(n-1)


# In[4]:


# Task 1 (1.3): Read input.txt file using pandas
data = pd.read_csv("input.txt", sep=',', escapechar='\\', encoding='utf-16', header=0, engine='python', index_col=0, na_values=['NA', '--'])


# In[5]:


# Function shape returns the number of (rows, columns) in a dataframe
def shape(x):
    return x.shape
# Function totalpop2010 returns the world population in millions according to the input.txt data in 2010 
def totalpop2010(x):
    return round(data['2010'].sum())

