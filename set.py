#!/usr/bin/env python
# coding: utf-8

# In[5]:


# CREATE A SET
set1={"a","b","c"}
set1


# In[6]:


# add an element
set1={"a","b","c"}
set1.add("1")
set1


# In[9]:


set1={"a","b","c"}
set1.add("1")
set1.add("$")
set1.add("100")
set1.add("apple")
set1.add("@")
set1.add("bat")
set1.add("1000")
set1





# In[10]:


#adding ,ultiple item using update
set1={"a","b","c"}
set1.update(['x','2','top'])
set1


# In[11]:


# find length of set
set1={"$","1","100","1000","a","b","c"}
x=len(set1)
print(x)


# In[12]:


# remove value from set
set1={"$","1","100","1000","a","b","c"}
set1.remove("1000")
set1


# In[16]:


#pop an element from an set
set1={"a","b","c","12","100"}
y=set1.pop()
print(y)




# 

# In[17]:


# clear a set
set1={"$","1","100","1000","a","b","c"}
set1.clear()
set1


# In[24]:


# delete a set
set1={"100","1000","a","b","c"}
del set1
set1


# In[26]:


# union of a set
set1={"a","b","c"}
set2={"1","2","3"}
set3=set1.union(set2)
set3


# In[28]:


# intersection of a set
set1={"a","b","c"}
set2={"c","d","e"}
set3=set1.intersection(set2)
set3


# In[31]:


# subset of set
set1={"a","b","c"}
set2={"1","2","3"}
set1.issubset(set2)


# In[35]:


set1.issuperset(set2)


# In[33]:


set1={"a","b","c"}
set2={"a","b","c","d","e"}
set1.issubset(set2)


# In[34]:


set2.issuperset(set1)


# In[36]:


# symmetric
set1={"a","b","c"}
set2={"b","c","e"}
set1.symmetric_difference(set2)


# In[38]:


set1={"a","b","c"}
set2={"b","c","e"}
set1.update(set2)
set1


# In[ ]:




