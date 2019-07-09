#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1) [1,4,5,6,9] - 14569
def convert(s):
    x=0
    for i in range(len(s)):
        x=x*10+s[i]
    return x
s=[1,4,5,6,9]
convert(s)


# In[2]:


# 2) [1,4,5,6,9]  - 46 (Consider only even numbers from list)
def even(s):
    x=0
    for i in range(len(s)):
        if s[i]%2==0:
            x=x*10+s[i]
    return x
s=[1,4,5,6,9]
even(s)


# In[3]:


# 3. [1,2,3,4,5] - [1,4,3,16,5] (Consider only even number and square of it)
def square(s):
    for i in range (len(s)):
        if s[i]%2==0:
            s[i]=s[i]**2
    return s
s=[1,2,3,4,5]
square(s)


# In[5]:


# [15,19,12,16,4] - [15,34,31,28,4] (Need to add previous number to current number)
def linearSearch5(li):
    for x in range(len(li)):
        if x ==0 or x == len(li) -1:
            print(li[x],end=" ")
        else:
            print(li[x-1]+li[x],end=" ")
    return
li = [15,19,12,16,4]
linearSearch5(li)


# In[ ]:




