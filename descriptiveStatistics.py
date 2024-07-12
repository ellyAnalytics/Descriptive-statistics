#!/usr/bin/env python
# coding: utf-8

# # Descriptive Statistics using cars dataset
# ## Meant to give better data understanding
# ### mean, mode, median and quantiles

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


mtcars = pd.read_csv("D:/mtcars.csv")


# In[6]:


mtcars.head()


# In[7]:


mtcars.index = mtcars["model"]


# In[8]:


mtcars.head()


# In[9]:


del mtcars["model"]


# In[10]:


mtcars.head()


# In[11]:


mtcars.mean()


# In[12]:


mtcars.mean(axis=1)


# In[13]:


mtcars.median()


# In[14]:


mtcars.median(axis = 1)


# In[15]:


max(mtcars["mpg"]) - min(mtcars["mpg"])


# In[16]:


mtcars["mpg"]


# In[19]:


quantiles = [mtcars["mpg"].quantile(0), #minimum value
            mtcars["mpg"].quantile(0.25), #25th percentile
            mtcars["mpg"].quantile(0.50), #median value
            mtcars["mpg"].quantile(0.75), #75th percentile
            mtcars["mpg"].quantile(1.0), #maximum value
            ]
quantiles


# In[20]:


mtcars["mpg"].describe()


# norm.plot(kind = "bar")

# In[ ]:




