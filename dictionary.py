#!/usr/bin/env python
# coding: utf-8

# In[5]:


#ques 1
number={
    "A":42,
    "B":33,
    "C":50,
}
print(number)


# In[7]:


#ques 2
rollno={
    1:"aman",
    2:"akash",
    3:"kamal",
}
print(rollno)


# In[8]:


#ques 3 
dict1={
    "A":32,
    "B":65,
}
print(dict1.items())


# In[10]:


#ques 4
dict1={
    "A":32,
    "B":65,
}
del dict1['A']
print(dict1)


# In[11]:


#ques 5 
dict1={
    "A":42,
    "B":33,
    "C":50,
}
for key,value in dict1.items():
    print(key,value)


# In[12]:


#ques 6 
dict1={
    "mango":"fruit",
    "apple":"fruit",
    "tomato":"veggie",
    "patato":"veggie",
}
if "mango" in dict1:
    print("yes")
else:
    print("no")


# In[13]:


#ques7 
dict1={
    "A":42,
    "B":33,
    "C":50,
}
dict1["A"]="x"
print(dict1)


# In[14]:


#ques8
dict1={
    "A":42,
    "B":33,
    "C":50,
}
dict1["A"]=65
print(dict1)


# In[17]:


#ques9
dict1={
    "A":42,
    "B":33,
    "C":50,
}
dict1["A"]=(1,2,3)
print(dict1)


# In[20]:


#ques10
dict1={
    "A":42,
    "B":33,
    "C":50
}
dict2={
    "A":42,
    "B":33,
    "C":50
}
dict1==dict2


# In[21]:


#ques11
dict1={}
for key in range(1,11):
    dict1[key]=key*key
print(dict1)


# In[35]:


#ques12
dict1={
    "a":12,
    1:"abc",
    5:{"a":16,2:"def",},
    "c":17,
}
print(dict1)


# In[44]:


#ques13
dict4={
    "A":42,
    "B":33,
    "C":50
}
print(dict4.clear())


# In[56]:


#ques14
d1={"a":1,"b":2}
d2={"c":3,"d":4}
d3={"e":5,"f":6}
for d in(d1,d2,d3):
    d.update(d)
    print(d)


# In[63]:


#ques15
dict1={
    "A":42,
    "B":33,
    "C":50
}
sum=0
for key,value in dict1.items():
    sum=sum+value
print(sum)


# In[64]:


#ques16
dict1={
    "A":4,
    "B":3,
    "C":5,
}
mul=1
for key,value in dict1.items():
    mul=mul*value
print(mul)


# In[70]:


#ques17
dict1={
    "key1":"value1",
    "key2":"value2",
    "key3":{"key31":"value31","key32":"value32"
           },
}
dict1["key3"]["key32"]


# In[ ]:




