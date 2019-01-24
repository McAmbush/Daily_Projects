
# coding: utf-8

# In[34]:


str = input()


# In[35]:


li = str.split()


# In[36]:


li


# In[37]:


for i in range(len(li)):
    print(li[i][0].capitalize(),end = '')
    for j in range(1,len(li[i])):
        print(li[i][j],end = '')
    print(' ',end = '')

