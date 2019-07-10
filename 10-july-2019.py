#!/usr/bin/env python
# coding: utf-8

# ### Dictionaries
#  - It works on the concept of set unique data
#  - Keys,values is the unique identifier for a value
#  - Each key is separated from its values with colon(:)
#  - Each key and value is separated by comma(,)
#  Dictionaries enclosed with curly braces({})

# In[2]:


d1 = {"Name":"Gitam","EmailId":"gitam@gmail.com","Address":"Hyderabad"}
print(d1)


# In[3]:


d1["Name"]


# In[4]:


d1['EmailId'] = 'Gitam-Python@gmail.com'


# In[5]:


d1['EmailId']


# In[6]:


del d1['EmailId']


# In[7]:


d1


# In[8]:


d1.keys() # returns the list of keys


# In[9]:


d1.values() # returns the values


# In[10]:


d1.items() # the ist of tuples of keys and values


# ### Tuples
#    - t1 parenthesis() li square brackets[]
#    - Difference between list and tuples
#      

# In[11]:


t1 = (1,2,3,4,5,6)
t1
type(t1)


# ### Contact Application 
#    - Add Contact
#    - Serach the contact
#    - List all contacts
#       - name1 : phone1
#       - name2 : phone2
#    - Modify the contact
#    - Remove the contact
#    - Import the contact

# In[14]:


# Add contact
contacts = {} # Creating a dict objects
def addcontact(name,phone):
    if name not in contacts:
        contacts[name] = phone
        print("contact is details are added")
    else:
        print("contact details are already exists")
    return
addcontact('sreekhar','9912957409')
addcontact('shashank','8374422693')
addcontact('syam','9100964643')
addcontact('syam','9100964643')


# In[19]:


contacts


# In[17]:


# Search for contact details
def searchcontact(name):
    if name in contacts:
        print(name,":" , contacts[name])
    else:
        print("%s does not exists" % name)
    return
searchcontact('sreekhar')
searchcontact('shashank')
searchcontact('syam')
        


# In[30]:


# Import some contacts
# Merge the contact with existing one
def importcontact(newcontacts):
    contacts.update(newcontacts)
    print(len(newcontacts.keys()),"contacts addad successfully")
    return
newcontacts = {'Dinesh':9988774455,'Ajay':9977445566}
importcontact(newcontacts)


# In[31]:


contacts


# In[33]:


# Delete a contact
def deletecontact(name):
    if name in contacts:
        del contacts[name]
        print(name,"deleted successfully")
    else:
        print(name,"not exists")
    return
deletecontact('Ajay')


# In[34]:


contacts


# In[37]:


# Update the contact details
def deletecontact(name,phone):
    if name in contacts:
        contacts[name] = phone
        print(name,"Updated successfully")
    else:
        print(name,"Not exists")
    return
deletecontact('syam',9100964643)
deletecontact('Ajay',9988665544)


# In[38]:


# Classical Version
li = ["python","Programming"]
print("%s %s "% (li[0],li[1]))


# In[39]:


print("{0} {1}".format(li[0] , li[1]))


# In[40]:


li1 = [1,2,3,4]
print("%d %d %d %d " % (li1[0],li1[1],li1[2],li1[3]))


# In[41]:


print("{0} {1} {2} {3}".format(li1[0],li1[1],li1[2],li1[3]))


# ### string function
# - upper() -- will convert the given string in upper case
# - lower() -- will convert the given string in lower case
# 

# In[51]:


s1 = 'gitam'
print(s1.upper())
print(s1.lower())


# ### Boolean function(true and false)
# - islower() -- btrue if the string in lower case/false if the string not in lower case
# - isupper() -- true is the string is uppercase/ false if thr string not in upper case
# - istitle() -- true if the string follows title case / false
# - isalpha() -- true if the string contains only alphabets / false
# - isnumeric() -- true if the string contains only numbers / false
# - isspace() -- true if the string contains spaces / false

# In[44]:


s1 = 'gitam'
print(s1.islower())
print(s1.isupper())


# In[48]:


s2 = "python programming"
s3 = "python programming"
print(s2.istitle())
print(s3.istitle())


# In[49]:


s2 = "Application1889"
s3 = 'pythonprogramming'
print(s2.isalpha())
print(s3.isalpha())


# In[52]:


s1 = '1234'
s2 = "Application1234"
print(s1.isnumeric())
print(s2.isnumeric())


# In[53]:


s1 = " "
s2 = "py th on"
print(s1.isspace())
print(s2.isspace())


# ### String Methods
# - 1.join() -- Method will concatinates the two strings
# - 2.split() -- split() returns the list of strings separated 

# In[57]:


s1 = 'python'
print(" ".join(s1))


# In[58]:


s2 = "python programming easy to learn"
print(",".join(s2))


# In[59]:


li = ['python','programming','learn']
print(",".join(li))


# In[1]:


s2 = "Python Programming Easy to learn"
print(s2.split())


# In[2]:


s2 = "Python Programming Easy to learn"
print(s2.split('a'))


# In[3]:


s2 = "Python Programming Easy to learn"
li=s2.split()   #split the string -- List object
print(li)
print(len(li))


# In[4]:


s2 = "Python Programming Easy to learn"
li=list(s2)
print(li)


# ### Packages and Modules
# 
# **Packages**
#     - A collection of Modules(Single Python file .py) and subpackages
# ** Module**
#     - A single Python c=file containing set functions
#  
# Packages --> Sub Packages -->Modules -->Functions -->Statements

# In[5]:


# Import the externals packages to python file
import math
math.floor(123.45)


# In[6]:


items=[1,5]
print("s",items)


# In[7]:


# Function to generate N random numbers in given range
import random
def randomNNumbers(n,lb,ub):
    for i in range(0,n):
        print(random.randint(lb,ub),end=" ")
    return
randomNNumbers(10,0,100)


# In[ ]:




