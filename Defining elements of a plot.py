#!/usr/bin/env python
# coding: utf-8

# # Defining elements of a plot

# In[1]:


import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series,DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
rcParams['figure.figsize'] =5,4


# In[25]:


x = range(1,10)
y =[1,2,3,4,0,4,3,2,1]

fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
ax.plot(x,y)


# In[11]:



fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])

ax.set_xlim([1,9])
ax.set_ylim([0,5])

ax.set_xticks([0,1,2,3,4,5,6,8,9,10])
ax.set_yticks([0,1,2,3,4,5])

ax.plot(x,y)


# # Adding grid

# In[12]:



fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])

ax.set_xlim([1,9])
ax.set_ylim([0,5])

ax.grid()
ax.plot(x,y)


# # Generating multiple plots in one figure with subplots

# In[27]:


fig = plt.figure()
fig,(ax1,ax2) = plt.subplots(1,2)
ax1.plot(x)
ax2.plot(x,y)

