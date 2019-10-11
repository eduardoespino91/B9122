#!/usr/bin/env python
# coding: utf-8

# In[1]:


def EMI(rate,N,PV,FV):
    return (PV + (FV/(1+rate)**N))*((rate*(1+rate)**N)/(((1+rate)**N)-1))
    print (a)


# In[2]:


EMI(0.05,30,10000,2000)


# In[ ]:




