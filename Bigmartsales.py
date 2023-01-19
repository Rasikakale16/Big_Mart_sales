#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


# In[6]:


df = pd.read_csv("../DataSets/Bigmartsales.csv")


# In[7]:


df


# In[5]:


df.head()


# In[6]:


df.Item_Fat_Content.unique()


# In[7]:


df.Outlet_Identifier.unique()


# In[8]:


df.dtypes


# In[9]:


df.count()


# In[10]:


df.Outlet_Identifier.count()


# In[11]:


df.Outlet_Identifier.value_counts()


# In[12]:


pd.crosstab(index =[df.Outlet_Identifier,df.Outlet_Location_Type],columns = df.Outlet_Size)


# In[13]:


pd.crosstab(index= [df.Outlet_Establishment_Year,df.Item_Fat_Content], columns = df.Item_Type, margins = True, margins_name = 'Total')


# In[14]:


df.index


# In[15]:


df.isnull()


# In[16]:


df.isnull().sum()


# In[17]:


df.Item_Weight.mean() 


# In[18]:


df


# In[19]:


df.Item_Weight = df.Item_Weight.fillna('12.69')
df


# In[20]:


df.Outlet_Size.mode()  #string object ka mode nikalenge.


# In[21]:


df.Outlet_Size = df.Outlet_Size.fillna('Medium')
df


# In[22]:


print(df.Item_Identifier.unique())
Item = input("Enter Item identifier code:")
a = df[df.Item_Identifier == Item]
print(df.Item_Type.unique())
Type = input("Enter Item Type:")
b = df[df.Item_Type == Type]
b


# In[32]:


#HIDDEN PARAMETERS
print(df.Item_Fat_Content.unique())
Item = input("Enter Item identifier code:")
a = df[df.Item_Identifier == Item]
print(df.Item_Type.unique())
Type = input("Enter Item Type:")
b = df[df.Item_Type == Type]
b

w = plt.figure(figsize =[15,7])
w.add_subplot(121)
ax1=sb.barplot(b.Outlet_Identifier,b.Item_MRP,palette='hot')
plt.xticks(rotation = 90)
plt.title("%s_models" %(Item))


# In[23]:


#VISUALS 


# In[11]:


sb.lmplot(x='Item_Weight',y='Item_MRP',col='',data=df,fit_reg=False)
plt.show()


# In[12]:


df.Item_Fat_Content.value_counts()


# In[15]:


sb.kdeplot(data = df.Outlet_Establishment_Year)
plt.show()


# In[16]:


sb.boxplot(df.Outlet_Establishment_Year)
plt.show()


# In[18]:


sb.violinplot(df.Outlet_Establishment_Year,palette = 'summer')
plt.show()


# In[19]:


sb.stripplot(df.Outlet_Establishment_Year,df.Item_MRP)
plt.show()


# In[20]:


sb.swarmplot(df.Item_MRP)
plt.show()


# In[26]:


sb.jointplot(df.Item_MRP,df.Item_Weight,color='k')
plt.show()


# In[39]:


#STATS 
df = [df.Item_Identifier== 'Dairy']


# In[41]:


df.Outlet_Identifier.min()


# In[38]:


df.describe()


# In[45]:


df.covariance()


# In[43]:


df.corr()


# In[44]:


df.std()


# In[ ]:




