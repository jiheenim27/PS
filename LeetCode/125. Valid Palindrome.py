#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re


# In[4]:


def is_palindrome(s):
    res = ''.join(re.findall("\w",s))
    res = res.lower().replace("_","")
    return res == res[::-1]


# In[5]:


is_palindrome("A man, a plan, a canal: Panama")


# In[6]:


is_palindrome("race a car")


# ### Solution 3

# In[9]:


def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)
    return s == s[::-1]   


# In[10]:


isPalindrome("A man, a plan, a canal: Panama")


# In[11]:


isPalindrome("race a car")


# In[ ]:




