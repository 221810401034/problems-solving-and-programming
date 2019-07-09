#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Day objectives

1.python data structures
   . lists
   . Tuples
   . Dictionaries
 . basic program sets on data strutcures
 . advanced problem set 
 . contact application(Dicionary object)

 Data structures:
        
        . to store,search and sort the data


# In[5]:


lst = [1,8,16,9,2] #creating the list object in python
print(lst) # Access the entire list
print(lst[0]) #Access the first item list
print(lst[1]) #Access the second item list
print(lst[-1]) #Access the last item list
print(lst[-2])
print(lst[1:])
print(lst[1:4])


# In[6]:


li = ["Gitam","Python",1989,2002]
print(li)
li[2] = 2019
print(li)


# In[7]:


# delete the specific item in the list
print(li)
del li[2]
print(li)


# In[13]:


# Basic List Operations
lst1 = [1,9,6,18,2]
print(len(lst1)) # Len of the list
print(lst1 * 2) # Repetation
print(len(lst1))
print(9 in lst1)# List item is present or not
print(15 in lst1)
# Access the list items using iteration
for x in range(len(lst1)):
    print(lst1[x],end=' ')


# In[18]:


# Function of the list
lst1
print(min(lst1)) # Min item/element of the list
print(max(lst1)) # Max element of the list
print(sum(lst1)) # Sum of the all elements of the list
print(sum(lst1)//len(lst1)) #Average of list elements
print(sum(lst1[1::2])/len(lst1[1::2])) # Average of all the alternate elements


# In[30]:


lst1
lst1.append(24) # Adding a new element at the end of the list
lst1
lst1.insert(2,56) # Adding an element at particular index
lst1
lst1.count(18) # Return the value how many times the object repeated
lst1.index(56)
lst1.sort() # It's sort the list in ascending order
lst1
lst.pop() # remove the last element from the list
lst1
lst.pop() # Remove an element from the particular index
lst2 = [123,23,45]
lst1.extend(lst2) # merge the list2 into list1
lst1


# In[48]:



lst=[2,6,8]
lst.append(24)
lst
lst.insert(3,55)
lst
lst.count(3)
lst.index(8)
lst.sort()
lst
lst.pop()
lst
lst.pop(1)
lst


# In[28]:


# fumction to dind the second large item from the list
# Input : [1,19,6,2,8,18,3]
# output : 18
def secondlarge(li):
    li.sort()
    return li[-2]
li = [1,19,6,2,8,18,3]
secondlarge(li)


# In[29]:


def secondlarge(ls):
    ls.sort()
    return ls[-2]
def genericlarge(ls,n):
    ls.sort()
    return ls[-n]
ls = [2,10,7,3,8,67]
genericlarge(ls,4)


# In[51]:


# Function
# Input : [1,5,9,6,5,15,1,2,5],key=5 #Duplicate
# Output : 1 4 8
def LinearSearch2(li,tarItem):
    for x in range(len(li)):
        if li[x] == tarItem:
            print(x,end=" ")
    return
li = [1,5,9,6,5,15,1,2,5]
LinearSearch2(li,5)


# In[2]:


# Function
# Input : List
# Output : Seq of characters
# Test case
# [1,5,9,6,5,15,1,2,5],tar=5 -- !! !!!!! !!!!!!!!!
def LinearSearch3(li,tarItem):
    # Implemen tthe logic
    for x in range(len(li)):
        if li[x] == tarItem:
            j = 0
            while j != x+1:
                print("!",end="")
                j = j + 1
            print(end=" ")
    return
li = [1,5,9,6,5,15,1,2,5]
LinearSearch3(li,5) # !! !!!!! !!!!!!!!!


# In[4]:


# Function
# Input : List
# Output : Formatted
# Test case:
# [12,2,45,9,18,15,36] -- 60
# A list item which is perfectly multiple of 3 and 5
def LinearSearch4(li):
    sum = 0
    for x in range(len(li)):
        if li[x] % 3 == 0 and li[x] % 5 == 0:
            sum += li[x] # Sum = Sum + li[x] 
    return sum
li = [12,2,45,9,18,15,36]
LinearSearch4(li) # 60


# In[5]:


# Function
#i/p:list
#o/p:formatted o/p
#test case
#[1,2,3,4,5] --[1,3,8,15,5]
#[6,5,2,8,2] --[6,12,40,4,2]
def LinearSearch5(li):
    for x in range(len(li)):
        if x == 0 or x == len(li) - 1:
            print(li[x],end=" ")
        else:
            print(li[x-1]*li[x+1],end=" ")
    return
li = [1,2,3,4,5]
LinearSearch5(li)


# In[1]:


#Function
# i/p: list
#o/p : formatted o/p
# test cases:
#[1,6,9,4,16,19,22] -- 1 9 19 22
def LinearSearch6(li):
    # Implement the logic
    for x in range(len(li)):
        if x == 0 or x == len(li) - 1:
            print(li[x],end=" ")
        elif li[x-1] % 2 == 0 and li[x+1] % 2 == 0:
            print(li[x],end=" ")
    return
li = [1,6,9,4,16,19,22]
LinearSearch6(li) # 1 9 19 22


# In[2]:


# 1990 -- [1,9,9,0]
def numberlistconversion(n):
    li = []
    while n != 0:
        r = n % 10
        li.append(r)
        n = n // 10
    li.reverse()
    return li
numberlistconversion(14569) #[1,4,5,6,9]


# In[4]:


# Function to count the occurences of a character in a string
# "Python Programming", p-->2
# "Python Programming", m-->2
def countCharOccurances(s,c):
    cnt=0
    for ch in s:
        if ch == c:
            cnt+=1
    return cnt
countCharOccurances("Python Programming",'m')


# In[5]:


#String to list
#input will be string
#.Expected output will be list
# Function to convert string to list
# Test case
# "1 2 3 4 5 6" --[1,2,3,4,5,6]

def strintToListConversion(s):
    li=s.split()
    numberslist =[]
    for i in li:
        numberslist.append(int(i))
    return numberslist
s="1 2 3 4 5 6"
strintToListConversion(s) #[1,2,3,4,5,6]


# ### Sorting Algorithms:
#  - All the sorting algorithms makes the list into ascending order
#  
#   

# In[6]:


# Function to represent the Bubble sort
def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li
li= [19,1,25,6,18,3]
bubbleSort(li)


# In[ ]:




