#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 1.python program to print the fibonacci series in the reverse order
def reverseFibonacci(n):
    a = [0] * n
    a[0] = 0 
    a[1] = 1 
    for i in range(2, n):   
        a[i] = a[i - 2] + a[i - 1]  
    for i in range(n - 1, -1 , -1):   
        print(a[i],end=" ")       
reverseFibonacci(5) 


# In[12]:


# 2.the program must print the sum of non repeated integers
def Q2(n):
    a=[]
    s=0
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        c=0
        for j in range(n):
            if i!=j:
                if a[i]==a[j]:
                    c+=1
        if c==0:
            s=s+a[i]
    return s
Q2(int(input("no of values")))


# In[13]:


# 3.the program must accept two strings and print the pattern
def Q3(a,b):
    if len(a)<=len(b):
        n=len(a)
        k=len(b)
    else:
        n=len(b)
        k=len(a)
    for i in range(n):
        print(a[i],b[i])
    for j in range(n,k):
        if(len(a)<=len(b)):
            print(b[j],'*')
        else:
            print(a[j],'*')
    return
x=str(input("enter str:"))
x=x.split()
Q3(x[0],x[1])


# In[14]:


# 4.The program print the longest word from the string S as the output. If two or more longest words are of same length then consider the first one.
def Q4(a,b):
    if len(a)>=len(b):
        print(a.upper())
    else:
        print(b.upper())
    return
x=str(input("enter str:"))
x=x.split()
Q4(x[0],x[1])


# In[17]:


# 5.Your program need to accept a string (alphanuermic) includes white spaces also
def Q5_1(a):
    a=a.split()
    for i in range (len(a)):
        if a[i].istitle()==True:
            print(a[i].upper(),end= " ")
    return
x=str(input("enter str:"))
Q5_1(x)


# In[14]:


# 6.The program must accept an integer N as the input. The program must print the Nth term in the series 
def findNthTerm(n): 
   if n % 2 == 0: 
       n //= 2
       print(3 ** (n - 1)) 
   else: 
       n = (n // 2) + 1
       print(2 ** (n - 1)) 
if __name__=='__main__': 
   N = 3
   findNthTerm(N) 
   N = 21
   findNthTerm(N) 


# In[19]:


# 7.The program must accept an integer N the input. The program must print the desired pattern
def Q7(n):
    for i in range(len(n)):
        n[i]=int(n[i])
    for i in range(len(n)):
        for j in range(n[i]):
            print("*",end="")
        print("")
    return
x=input("enter num")
Q7(list(x))


# In[20]:


#8. Your Program has to read one string as well as one character and you need to remove the all the occurance of the character.

#HebeonTech,e -- HbonTch
def delete(n,target):
    c=0
    for i in range(len(n)):
        if n[i]==target:
            c+=1
    print(n.replace(target,"",c))
n=str(input("enter a string"))
target=str(input("enter a char"))
delete(n,target)


# In[21]:


# 9. Your Program need to accept two strings and generate the output in merging of both strings.
def comb(a,b):
    c=a+b
    return c 
a=str(input("enter a string "))
b=str(input("enter a string "))
comb(a,b)


# In[27]:


# 10. Series Generations:-  1, 3, 9, 27, 81, ...
def square(n):
    for i in range(n):
        print(3**i,end=" ")
    return
n=int(input("enter a number"))
square(n)


# In[23]:


# 11. Series Generations:-  1, 2, 4, 8, 16, 32, 64, 128, 256, ...
def square(n):
    for i in range(n):
        print(2**i,end=" ")
    return
n=int(input("enter a number"))
square(n)


# In[24]:


# 12. Series Generations:-  1 3 4 8 15 27 50 92 169 311
def series(n):
    a=1
    b=3
    c=a+b
    print(a,b,c,end=" ")
    for i in range (4,n+1):
        d=a+b+c
        a=b
        b=c
        c=d
        print(d,end=" ")
    return
n=int(input("enter a number"))
series(n)


# In[28]:


# 13. Series Generations:-  2 15 41 80 132 197 275 366 470 587
def series(n):
    a=2
    print(a,end=" ")
    for i in range (1,n+1):
        b=a+(13*i)
        print(b,end=" ")
        a=b
    return
n=int(input("enter a number"))
series(n)


# In[26]:


# 14. Series Generations:-  1! + 2! + 3! + 4! + 5! + ... + n!
def fact(a):
    f=1
    for i in range (1,a+1):
        f*=i
    return f   
def series(m):
    s=0
    for x in range (1,n+1):
        s=s+fact(x)
    return s
n=int(input("enter n"))
series(n)


# In[23]:


#15 Series Generations:-  1,9,17, 33,49,73,97
import math
def seriesgen3(n):
    s= 1
    i=2
    while i<=n+1:
        a=math.ceil(i/2)
        s=s+8*(a-1)
        print(s,end=" ")
        i=i+1
    return 
seriesgen3(7)


# In[ ]:




