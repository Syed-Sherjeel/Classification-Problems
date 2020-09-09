#!/usr/bin/env python
# coding: utf-8

# # Red wine quality a polynomial regression approach

# ## Introduction

# Red wine is a type of wine made from dark-colored grape varieties. The actual color of the wine can range from intense violet, typical of young wines, through to brick red for mature wines and brown for older red wines.In this project we are going to explore quality of with respect to amount of different content.We will also discover how much quality of red wine depends upon these contents.Lastly we will model a relationship between these quantities and quality of red wine

# ![](data:image/jpeg;base64,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)

# # Libraries

# We will be needing following libraries, 
# - Scikitlearn
# - pandas
# - matplotlib
# 
# ## Scikitlearn: 
# Now the relationship between quality of wine and different content inside the wine can be modeled using a statistical technique known as Regression.Here we will use its variant known as polynomial regression as tool for modelling the relationship between redwine and various contents that are used in production of redwine.
# ## Pandas: 
# Pandas is an amazing data handling and data wrangling tool that makes our job a lot easier and efficent compared to normal file opeing using trivial open code.Pandas come with several builtin function that allow exploratory data analysis and preprocessing a lot easier.

# # Importing libraries

# In[12]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score
import seaborn as sns


# # Exploratory data analysis and Preprocessing

# In[2]:


data_set=pd.read_csv('winequality-red.csv',delimiter=';')
data_set.head()
#X,y,X_test,y_test=train_test_split()


# In[3]:


# Checking for null values
data_set.isnull()
#dropping null values 
data_set.dropna()
#forward filling null values
data_set.fillna(method='ffill')


# In[10]:


data_set.describe()


# In[4]:



#checking average quality of wine in data
#checking the distribution of this data
plt.hist(data_set[data_set['quality']>data_set['quality'].mean()].quality.values)


# In[5]:


# checking lowest quality wines in our data set
#checking distribution of this data
plt.hist(data_set[data_set['quality']<data_set['quality'].mean()].quality.values)


# In[6]:


#checking distribution of qulaity of wines
plt.hist(data_set.quality.values)


# # Visualizing Outliers

# In[14]:


plt.subplot(421)
sns.boxplot(data_set['quality'])
plt.subplot(422)
sns.boxplot(data_set['fixed acidity'])
plt.subplot(423)
sns.boxplot(data_set['volatile acidity'])
plt.subplot(424)
sns.boxplot(data_set['residual sugar'])
plt.subplot(425)
sns.boxplot(data_set['free sulfur dioxide'])
plt.subplot(426)
sns.boxplot(data_set['total sulfur dioxide'])
plt.subplot(427)
sns.boxplot(data_set['density'])
plt.subplot(428)
sns.boxplot(data_set['citric acid'])


# It is obvious that data contain a lot of outliers.If we train model on this dataset then our model would end up hitting a local optima as optimization would be non convex.We need to do the feature scaling which will standardize the dataset.
# ![](1_g1xhcuv3IHHm7EKUP5JkSA.png)

# ## Splitting data set

# In[15]:


#First split explanatory variable and Output variable
y = data_set['quality']
# All the input parameters used to predict the value are represented as y.
X =data_set[['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol']]
#X=data_set.iloc[:,:-1]
#y=data_set.iloc[:,-1:]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2)
X_test.head()


# ## Feature Scaling

# In[9]:


scale=StandardScaler()
scale.fit_transform(X_train)
scale.fit_transform(y_train.reshape(-1,1))
scale.fit_transform(X_test)
scale.fit_transform(y_test.reshape(-1,1))


# ## Polynomial Features

# In[ ]:


features=PolynomialFeatures(degree=3)
features.fit_transform(X_train)
features.fit_transform(X_test)


# ## Setting degree of polynomial

# In[ ]:


Model=SVC(kernel='poly',degree=3,C=.2,gamma=1.1)


# # Fitting model

# In[ ]:


Model.fit(X_train,y_train)


# # Training set error

# In[ ]:


y_predict=Model.predict(X_train)
predicted_data = np.round_(y_predict)
print(accuracy_score(y_train,predicted_data))
print(precision_score(y_train,predicted_data))
print(recall_score(y_train,predicted_data))


# # Test set error

# In[ ]:


y_predict=Model.predict(X_test)
print(accuracy_score(y_predict,y_test))

