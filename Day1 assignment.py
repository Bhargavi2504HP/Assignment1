#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=int(input('enter first interval:'))
b=int(input('enter second interval:'))
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
                print(i)


# In[2]:


a=int(input('enter a number'))
f=1
for i in range(1,a+1):
    if a>0:
        f=f*i
print(f)


# In[5]:


a=int(input('enter a number'))
add=0
i=0
while i<a:
    n=int(input(''))
    add=add+n
    i=i+1
print("sum="+str(add))


# In[ ]:




