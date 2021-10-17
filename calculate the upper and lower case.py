#!/usr/bin/env python
# coding: utf-8

# In[11]:


def case_calculator(string):
    string=string.replace(' ','')
    upper=0
    lower=0
    for char in string:
        if char.isupper():
            upper+=1
        else:
            lower+=1
        print('No. of Upper case characters : ',upper)
        print('No. of Lower case characters: ',lower)


# In[12]:


Sample_String = 'The quick Brow Fox'


# In[13]:


case_calculator(Sample_String)


# In[ ]:




