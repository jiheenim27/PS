#!/usr/bin/env python
# coding: utf-8

# In[2]:


test1 = ["h","e","l","l","o"]
test2 = ["H","a","n","n","a","h"]


# ### Solution 2

# In[ ]:


def reverseString(s: str) -> None:
    s[:] = s[::-1]


# In[ ]:


def reverseString(s: str) -> None:
    s.reverse()

