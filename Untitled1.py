#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df =pd.read_csv('C:/vinod/wallpaper/Data for ML/datasets_4909_7459_USA_Housing.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


sns.pairplot(df)


# In[7]:


sns.distplot(df['Price'])


# In[8]:


df.corr()


# In[9]:


sns.heatmap(df.corr(),annot =True)


# In[10]:


df.columns


# In[11]:


x =df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population','Address']]


# In[12]:


y =df['Price']


# In[13]:


import sklearn


# In[14]:


from sklearn.cross_validation import train_test_split


# In[ ]:


from sklearn.model_selection import train_test_split


# In[ ]:


x_train,x_test,y_train,y_test =train_test_split(x,y,test_size =0.33,random_state =43)


# In[ ]:


from sklearn.linear_model import LinearRegression


# In[ ]:


lr =LinearRegression()


# In[ ]:


lr.fit(x_train,y_train)


# In[ ]:


print()

