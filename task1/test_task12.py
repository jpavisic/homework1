
# coding: utf-8

# In[2]:


from task1 import fib


# In[ ]:

# Task 1.2 unit test that ensures fib(2) is 1, fib(5) is 5 and fib(12) is 144.
def test_fib():
    assert fib(2) == 1
    assert fib(5) == 5
    assert fib(12) == 144

