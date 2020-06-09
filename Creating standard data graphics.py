#!/usr/bin/env python
# coding: utf-8

# # Creating standard data graphics

# In[2]:


import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams


# # Creating a line chart from list objects

# In[8]:


x =range(1,10)
y = [1,2,3,4,0,4,3,2,1]

plt.plot(x,y)


# # Plotting a line chart from pandas

# In[12]:


cars = pd.read_csv(r"C:\Users\Ramesh\Desktop\mtcars.csv")

cars.column = ['car_name','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

cars.head()

mpg = cars['mpg']


# In[14]:


mpg.plot()


# In[16]:


cyl =cars['cyl']
cyl.plot()


# In[18]:


hp =cars['hp']
hp.plot()


# In[19]:


df = cars[['cyl','wt','mpg']]
df.plot()


# # Creating a bar chart

# In[21]:


plt.bar(x,y)


# # Creating bar charts from pandas object

# I am going to plot the 'mpg' variable as bar.

# In[22]:


mpg.plot(kind = "bar")


# For getting a plot horizontally ,Add 'h' after bar "mpg.plot(kind = "barh")"

# In[24]:


mpg.plot(kind = "barh")


# # Pie charts

# In[25]:


x = [1,2,3,4,0,5]
plt.pie(x)
plt.show()


# # Saving a plot

# In[26]:


plt.pie(x)
plt.savefig("Pie_chart.png")
plt.show()


# In[27]:


get_ipython().run_line_magic('pwd', '')


# In[ ]:




