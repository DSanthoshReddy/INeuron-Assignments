#!/usr/bin/env python
# coding: utf-8

# ## Q 1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()
# 

# In[5]:


seq = [1,2,3,4,5]

def addition(a,b):

    return a+b

def myreduce(givenFunc,seq):
    
    output = seq[0]
    
    for item in seq[1:]:
        output = givenFunc(output,item)
        
    return output

output = myreduce(addition,seq)


print(output)


# ## 1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()
# 

# In[7]:


def myFilter(givenFunc,seq):
    newSeq = []
    for item in seq:
        if givenFunc(item):
            newSeq.append(item)
            
    return newSeq

def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False
  
  
# sequence 
allLetters = ['g','a','e', 'e', 'j', 'k', 's', 'p', 'r'] 
print(myFilter(fun,allLetters))


# ## 2. Implement List comprehensions to produce the following lists.
# ## Write List comprehensions to produce the following Lists

# In[4]:


input_list = ['x','y','z']

out_List = [i*count for i in input_list for count in range(1,5)]

print(out_List)


# In[5]:


input_list = ['x','y','z']

out_List_2 = [i*count for count in range(1,5) for i in input_list]

print(out_List_2)


# In[11]:


ip_list = [2,3,4]

op_list = [[j+k] for j in ip_list for k in range(0,3)]

print(op_list)


# In[16]:


ip_list = [2,3,4,5]

op_list = [[j+k for k in range(0,4)] for j in ip_list ]

print(op_list)


# In[19]:


ip_list = [1,2,3]

op_list = [(k,j) for j in ip_list for k in ip_list]

print(op_list)


# In[ ]:




