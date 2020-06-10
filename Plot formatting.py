#!/usr/bin/env python
# coding: utf-8

# # Plot formatting
# Exploring many colors and line styles and alos marker styled

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import matplotlib.pyplot as plt
from pylab import rcParams


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
rcParams['figure.figsize'] = 5,4


# # Defining plot color

# In[4]:


x = range(1,10)
y = [1,2,3,4,0.5,4,3,2,1]
plt.bar(x,y)


# Changing width and color

# In[6]:


wide = [0.5,0.5,0.5,.9,.9,.9,.5,.5,.5]
color =['green']
plt.bar(x,y,width = wide ,color = color)


# Changing color theme of pandas

# In[12]:


cars = pd.read_csv(r"C:\Users\Ramesh\Desktop\mtcars.csv")

cars.column = ['car_name','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

cars.head()


# In[15]:


df =cars[['cyl','mpg','wt']]
df.plot()


# In[17]:


color_theme = ['darkgray','lightsalmon','powderblue']
df.plot(color = color_theme)


# Changing color in pie chart

# In[19]:


z= [1,2,3,4,0.5]
plt.pie(z)
plt.show()


# In[24]:


color_theme= ['#A9A9A9','#FFA07A','#B0E0E6','#FFE4C4','#BDB76B']
plt.pie(z, colors=color_theme)
plt.show()


# # customizing line styles

# In[26]:


x1 =range(1,10)
y1 =[9,8,7,6,5,4,3,2,1]
plt.plot(x,y)
plt.plot(x1,y1)


# Changing the drawing style(ds) and line width(lw) and also the line style(ls)

# In[29]:


plt.plot(x,y, ds ='steps',lw =5)
plt.plot(x1,y1,ls ='--',lw =10)


# Setting plot markers ,marker width(mew)

# In[30]:


plt.plot(x,y,marker ='1' ,mew =20)
plt.plot(x1,y1,marker ='+',mew =15)

