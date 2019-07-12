#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
def rollnumber(number):
    pattern = '^[1][5][2][1][A][0][0-9]{3}$'
    number = str(number)
    if re.match(pattern,number):
        return True
    return False
print(rollnumber('1521A0897'))


# In[3]:


def password(passw):
    pattern = '[A-za-z0-9@#!]{6,15}'
    passw = str(passw)
    if re.match(pattern,passw):
        return True
    return False
print(password('naniAX098@'))


# In[ ]:




