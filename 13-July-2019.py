#!/usr/bin/env python
# coding: utf-8

# ### Transforming Code into Idiomatic Python
# * Replace traditional index manipulation with Python core looping idiomatic
# 

# In[1]:


# Looping over a range of numbers - Traditional Approach
for i in [0,1,2,3,4,5]:
    print(i**2,end=" ")


# In[2]:


# Idiomatic Programming
for i in range(6):
    print(i**2,end=" ")


# ## Looping Over a Collection

# In[3]:


colors = ['red','green','yellow','purple']
for i in range(len(colors)):
    print(colors[i],end=" ")


# In[4]:


for color in colors:
    print(color,end=" ")


# ## Looping backwards

# In[5]:


colors = ['red','green','yellow','purple']
for i in range(len(colors)-1,-1,-1):
    print(colors[i],end=" ")


# In[7]:


for color in reversed(colors):
    print(color,end=" ")


# ## Looping in Sorted List

# In[10]:


colors = ['red','green','yellow','purple']
for color in sorted(colors):
    print(color,end=" ")


# In[11]:


colors = ['red','green','yellow','purple']
for color in sorted(colors,reverse=True):
    print(color,end=" ")


# ###
#   - if x<=y and y<=z
#   - if x<=y<=z
#   - if x==True
#   - if x:

# ## Pandas

# In[1]:


import pandas as pd


# In[2]:


dt = {'Id' :[11,12,13,14,15],
     'first_name':['A','B','C','D','E'],
     'company':['aa','bb','cc','dd','ee'],
     'address':['Hyd','Hyd','Hyd','Hyd','Hyd']}
mydt = pd.DataFrame(dt)


# In[3]:


print(mydt)


# In[4]:


import os


# In[ ]:


os.chdir("D:\\MyData\\")# Saves to certain Location


# In[10]:


mydt.to_csv('WorkingFile.csv',index = False)


# In[ ]:




