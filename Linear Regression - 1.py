
# coding: utf-8

# In[2]:


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import pylab as pl


# In[3]:


get_ipython().system('wget -O FuelConsumption.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv')


# In[4]:


df = pd.read_csv('FuelConsumption.csv')


# In[5]:


df.head()


# In[6]:


df2 = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]


# In[7]:


df2.head(10)


# In[8]:


plt.bar(df2.CYLINDERS,range(len(df2.CYLINDERS)))


# In[9]:


plt.scatter(df2.FUELCONSUMPTION_COMB,df2.CO2EMISSIONS)


# In[10]:


plt.scatter(df2.ENGINESIZE,df2.CO2EMISSIONS)


# In[11]:


split = np.random.rand(len(df)) < 0.8


# In[12]:


train = df2[split]
test = df2[~split]


# In[13]:


plt.scatter(train.ENGINESIZE,train.CO2EMISSIONS)


# In[14]:


from sklearn import linear_model


# In[15]:


regr = linear_model.LinearRegression()


# In[16]:


train_x = np.asanyarray(train[['ENGINESIZE']])


# In[17]:


train_y = np.asanyarray(train[['CO2EMISSIONS']])


# In[18]:


regr.fit(train_x,train_y)


# In[19]:


plt.scatter(train.ENGINESIZE,train.CO2EMISSIONS)


# In[20]:


plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')


# In[21]:


test_x = np.asanyarray(test[['ENGINESIZE']])


# In[22]:


test_y = np.asanyarray(test[['CO2EMISSIONS']])


# In[26]:


y_pred = regr.predict(test_x)


# In[36]:


D = pd.DataFrame({'Actual':list(test_y),'Predicted':list(y_pred)})


# In[38]:


D


# In[44]:


print('Mean Absolute Error = ')
print(np.mean(np.absolute(y_pred-test_y)))


# In[47]:


from sklearn.metrics import r2_score
r2_score(y_pred,test_y)

