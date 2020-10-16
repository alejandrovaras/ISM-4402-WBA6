#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


import statsmodels.formula.api as sm
result = sm.ols(
 formula='grade ~ age + exercise + hours',
 data=df).fit()
result.summary()


# In[3]:


import statsmodels.formula.api as sm
result = sm.ols(
 formula='grade ~ exercise + hours',
 data=df).fit()
result.summary()


# In[4]:


df['NumberSex'] = 0


# In[5]:


import statsmodels.formula.api as sm
result = sm.ols(
 formula='grade ~ exercise + hours + NumberSex',
 data=df).fit()
result.summary()


# In[ ]:




