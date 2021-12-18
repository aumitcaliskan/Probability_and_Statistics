#!/usr/bin/env python
# coding: utf-8

# # **Regression Analysis**
# 

# The goal of regression analysis is to describe the relationship between one set of variables called the dependent variables, and another set of variables, called independent or explanatory variables. When there is only one explanatory variable, it is called simple regression.
# 

# ## Objectives
# 

# After completing this lab you will be able to:
# 

# *   Import Libraries
# *   Regression analysis in place of the t-test
# *   Regression analysis in place of ANOVA
# *   Regression analysis in place of correlation
# 

# ## Import Libraries
# 

# All Libraries required for this lab are listed below. The libraries pre-installed on Skills Network Labs are commented. If you run this notebook in a different environment, e.g. your desktop, you may need to uncomment and install certain libraries.
# 

# In[ ]:


#install specific version of libraries used in lab
#! mamba install pandas==1.3.3
#! mamba install numpy=1.21.2
#! mamba install scipy=1.7.1-y
#!  mamba install seaborn=0.9.0-y
#!  mamba install matplotlib=3.4.3-y
#!  mamba install statsmodels=0.12.0-y


# Import the libraries we need for the lab
# 

# In[1]:


import numpy as np
import pandas as pd
import statsmodels.api as sm


# Read in the csv file from the URL using the request library
# 

# In[2]:


ratings_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
df = pd.read_csv(ratings_url)


# ## Lab Exercises
# 

# In this section, you will learn how to run regression analysis in place of the t-test, ANOVA, and correlation
# 

# ### Regression with T-test: Using the teachers rating data set, does gender affect teaching evaluation rates?
# 

# Initially, we had used the t-test to test if there was a statistical difference in evaluations for males and females, we are now going to use regression. We will state the null hypothesis:
# 
# *   $H\_0: β1$ = 0 (Gender has no effect on teaching evaluation scores)
# *   $H\_1: β1$ is not equal to 0 (Gender has an effect on teaching evaluation scores)
# 

# We will use the female variable. female = 1 and male = 0
# 

# In[3]:


## X is the input variables (or independent variables)
X = df['female']
## y is the target/dependent variable
y = df['eval']
## add an intercept (beta_0) to our model
X = sm.add_constant(X) 

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

# Print out the statistics
model.summary()


# **Conclusion:** Like the t-test, the p-value is less than the alpha (α) level = 0.05, so we reject the null hypothesis as there is evidence that there is a difference in mean evaluation scores based on gender. The coefficient -0.1680 means that females get 0.168 scores less than men.
# 

# ### Regression with ANOVA: Using the teachers' rating data set, does beauty  score for instructors  differ by age?
# 

# State the Hypothesis:
# 
# *   $H\_0: µ1 = µ2 = µ3$ (the three population means are equal)
# *   $H\_1:$ At least one of the means differ
# 

# Then we group the data like we did with ANOVA
# 

# In[5]:


df.loc[(df['age'] <= 40), 'age_group'] = '40 years and younger'
df.loc[(df['age'] > 40)&(df['age'] < 57), 'age_group'] = 'between 40 and 57 years'
df.loc[(df['age'] >= 57), 'age_group'] = '57 years and older'


# Use OLS function from the statsmodel library
# 

# In[6]:


from statsmodels.formula.api import ols
lm = ols('beauty ~ age_group', data = df).fit()
table= sm.stats.anova_lm(lm)
print(table)


# **Conclusion:** We can also see the same values for ANOVA like before and we will reject the null hypothesis since the p-value is less than 0.05 there is significant evidence that at least one of the means differ.
# 

# ### Regression with ANOVA option 2
# 

# Create dummy variables - A dummy variable is a numeric variable that represents categorical data, such as gender, race, etc. Dummy variables are dichotomous, i.e they can take on only two quantitative values.
# 

# In[7]:


X = pd.get_dummies(df[['age_group']])


# In[8]:


y = df['beauty']
## add an intercept (beta_0) to our model
X = sm.add_constant(X) 

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

# Print out the statistics
model.summary()


# You will get the same results and conclusion
# 

# ### Correlation: Using the teachers' rating dataset, Is teaching evaluation score correlated with beauty score?
# 

# In[9]:


## X is the input variables (or independent variables)
X = df['beauty']
## y is the target/dependent variable
y = df['eval']
## add an intercept (beta_0) to our model
X = sm.add_constant(X) 

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

# Print out the statistics
model.summary()


# **Conclusion:** p < 0.05 there is evidence of correlation between beauty and evaluation scores
# 

# ## Practice Questions
# 

# ### Question 1: Using the teachers' rating data set, does tenure affect beauty scores?
# 
# *   Use α = 0.05
# 

# In[ ]:


### insert code here


# ### Question 2: Using the teachers' rating data set, does being an English speaker affect the number of students assigned to professors?
# 
# *   Use "allstudents"
# *   Use α = 0.05 and α = 0.1
# 

# In[ ]:


## insert code here


# ### Question 3: Using the teachers' rating data set, what is the correlation between the number of students who participated in the evaluation survey and evaluation scores?
# 
# *   Use "students" variable
# 

# In[ ]:


## insert code here

