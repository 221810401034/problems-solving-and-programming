#!/usr/bin/env python
# coding: utf-8

# ### Standard libraries
#   - File I/o
#   - Regular Expression
#   - Datetime
#   - Math (numerical and Mathematical)

# ### File Handling in Python 
#  - File:- Document containing information resides on the permanent storage
#  - Different types of files :- txt,doc,pdf,csv and etc...
#  - Input -- Keyboard
#  - Output -- File
# ### Modes of the File I/O
#  - 'w' -- This mode is used to file writing
#        -- If the file is not present first it creates the file and write so             me data to it
#        -- If the file is already present then it will rewrite the 

# In[2]:


# Function to create a file and write to the file
def createFile(filename):
    f = open(filename,'w')
    for i in range(10):
        f.write('This is %d line' % i)
    print("File is created and data has written")
    return
createFile('file1.txt')


# In[3]:


ls


# In[4]:


cat file1.txt


# In[6]:


def createFile(filename):
    f = open(filename,'w')
    print('Testing...\n')
    print("File is created and has written")
    return
createFile('file1.txt')


# In[7]:


def createFile(filename):
    f = open(filename,'w')
    f.write('Testing...\n')
    print("File is created and has written")
    return
createFile('file1.txt')


# In[8]:


def appenddata(filename):
    f = open(filename,'a')
    for i in range(10):
        print("This is %d Line\n" % i)
    print("file created and sccessfully data written")
    return
appenddata('file2.txt')


# In[9]:


def appenddata(filename):
    f = open(filename,'a')
    for i in range(10):
        f.write("This is %d Line\n" % i)
    print("file created and sccessfully data written")
    return
appenddata('file2.txt')


# In[10]:


def appendData(filename):
    f = open(filename,'a')
    f.write("New Line 1 \n")
    f.write("New Line 2 \n")
    print("File Created and Successfully data written")
    return
appendData('file2.txt')


# In[11]:


def readfiledata(filename):
    f = open(filename,'r')
    if f.mode == 'r':
        x = f.read()
        print(x)
    f.close()
    return
readfiledata('file2.txt')


# In[12]:


#function to rad the file
def fileoperations(filename,mode):
    with open(filename,mode) as f:
        if f.mode == 'r':
            data = f.read()
            print(data)
        elif f.mode == 'a':
            f.write('data to the file')
            print('the data successfully written')
    f.close()
    return
filename = input('enter the file name')
mode = input('enter the mode of the file')
fileoperations(filename,mode)


# In[13]:


# Data Analysis
# Word Count Program
def wordCount(filename,word):
    with open(filename, 'r') as f:
        if f.mode == 'r':
            x= f.read()
            li= x.split()    #It splits the string with whitespace
    cnt= li.count(word)
    return cnt
filename = input('Enter the file name :')
word = input('Enter the word :')  #which word count you need
wordCount(filename,word)


# In[14]:


# character count from the given file
def charcount(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = list(x)
    return len(li)
filename = input('Enter the filename : ')
charcount(filename)


# In[15]:


s1 = 'python program'
print(s1.split())


# In[16]:


# Function to find the no of lines in the input file
# Input -- filename(file2.txt)
# Output -- No of Lines(12)
def countoflines(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = x.split("\n")
    return len(li)
filename = input('Enter the filename :')
countoflines(filename)


# In[21]:


# Function to print the Upper and Lower characters
def caseCount(filename):
    cntUpper = 0
    cntLower = 0
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = list(x)
    for i in li:
        if i.isupper():
            cntUpper += 1 # cntupper = cntupper +1
        elif i.islower():
            cntLower += 1 # cntlower = cntlower +1
    output = 'Upper case = {0} , Lower case = {1}'.format(cntUpper,cntLower)
    return output
filename = input('Enter the filename : ')
caseCount(filename)


# ### math, random, os
#  - os packagr it contains the certains methods which works with OS 

# In[22]:


ls


# In[37]:


cd Users/mplab/probsolvingprogramming/git


# In[38]:


ls


# In[39]:


cd ..


# In[40]:


import os
os.listdir('git/')  # Listdir()  --ls


# In[41]:


li = os.scandir('git/')
for i in li:
    print(i)


# In[42]:


from pathlib import Path
li = Path('git/')
for i in li.iterdir():
    print(i.name)


# In[64]:


import os
dirPath = "Git/"
for i in os.listdir(dirPath):
    if os.path.isfile(os.path.join(dirPath,i)):
        print(i)
        


# In[47]:


dirPath = 'Git/'
with os.scandir(dirPath) as f:
    for i in f:
        if i.is_file():
            print(i.name)


# In[48]:


dirPath = 'Git/'
for i in os.listdir(dirPath):
    if os.path.isdir(os.path.join(dirPath,i)):
        print(i)


# In[49]:


from pathlib import Path
dirPath = Path('Git/')
for i in dirPath.iterdir():
    if i.is_dir():
        print(i.name)


# ### Creating a Single Directory

# In[51]:


import os
os.mkdir('SingleDirectory')


# In[59]:


import pathlib
p = pathlib.Path('Test')
p.mkdir()


# In[61]:


ls


# ### Creating Multiples Directories

# In[62]:


import os
os.makedirs('2019/July/11')


# In[63]:


ls


# ### Filename Pattern Matching 

# In[68]:


cd probsolvingprogramming


# In[69]:


import os
dirPath = 'Git/'
for f_name in os.listdir(dirPath):
    if f_name.endswith('.ipynb'):
        print(f_name)


# In[70]:


import os
dirPath = 'Git/'
for f_name in os.listdir(dirPath):
    if f_name.startswith('.ipynb'):
        print(f_name)


# ### Deleting Files and Directories

# In[73]:


ls


# In[79]:


cd git


# In[80]:


ls


# In[81]:


import os
data_file = 'file1.txt' # Give the entire Path
os.remove(data_file)


# In[76]:


pwd


# In[77]:


data_dir = 'TestFolder'
os.rmdir(data_dir)


# In[78]:


ls


# In[84]:


cd ..


# In[85]:


import shutil # Delete the tree of structure of folder
data_dir = '2019'
shutil.rmtree(data_dir)


# ### Regular Expressions
#  - Used to specific pattern matching 

# In[ ]:




