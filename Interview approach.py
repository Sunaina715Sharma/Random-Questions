#!/usr/bin/env python
# coding: utf-8

# In[2]:


s = "abcbbccbbbcaaaaabbbbbbbbcccccccccccabcbcaaaaaaabbbbb"


# In[12]:


# for i in range(0,len(s)):
#     if s[i]==s[1+1]:
#         print("yes")
#     else:
#         print("No")
i = 0
while i<len(s):
    if s[i]==s[i+1]:
        print("Yes")
    i = i+7
else:
    print("No")
    


# In[13]:


# Questions from different approach


# In[ ]:


# Candidate approach
x=["Kumod",23,"Rahul",24,"ankit",25]
y=["name","age"]


# In[ ]:


l1 = []
l2 = []
l3 = []
for i in x:
    if i=="Kumod" or i==23:
        l1.append(i)
    elif i=="Rahul" or i==24:
        l2.append(i)
    else:
        l3.append(i)
print(l1)
print(l2)
print(l3)


# In[ ]:


l = []
dict(zip(y,l1))
dict(zip(y,l2))
dict(zip(y,l3))


# In[ ]:


l.append(dict(zip(y,l1)))
l.append(dict(zip(y,l2)))
l.append(dict(zip(y,l3)))
l


# In[ ]:


# Interviewer Approach
s=["Kumod",23,"Rahul",24,"ankit",25]
t=["name","age"]


# In[ ]:


z = []
for i in range(0,len(s),2):
    m = {t[0]:s[i],t[1]:s[i+1]}
    z.append(m)
print(z)

