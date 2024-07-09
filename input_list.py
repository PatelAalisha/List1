#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Take user Input for lit


# In[2]:


l1=input("Enter a list element and separated by commmas:").split()
print("List is:",l1)
for i in l1:
    print(i)


# In[6]:


l2=[int(x) for x in input("Enter integers for list separated by spaces:").split()]
print("List is:",l2)


# In[8]:


input_str=input("Enter the element for the list :")
l1=input_str.split()
l1=[int(element)for element in l1]
print("List is:",l1)
for element in l1:
    print(element)


# In[ ]:





# In[ ]:




