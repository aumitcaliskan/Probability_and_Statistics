#!/usr/bin/env python
# coding: utf-8

# # **Data Visualization**
# 

# ## Objectives
# 

# *   Import Libraries
# *   Lab Exercises
#     *   Identifying duplicates
#     *   Plotting Scatterplots
#     *   Plotting Boxplots
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


# Import the libraries we need for the lab
# 

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 


# Read in the csv file from the url using the request library
# 

# In[3]:


ratings_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
df = pd.read_csv(ratings_url)


# ### Identify all duplicate cases using prof. Using all observations, find the average and standard deviation for age. Repeat the analysis by first filtering the data set to include one observation for each instructor with a total number of observations restricted to 94.
# 

# Identify all duplicate cases using prof variable - find the unique values of the prof variables
# 

# In[11]:


df.head()


# In[10]:


df.info()


# In[4]:


df.prof.unique()


# Print out the number of unique values in the prof variable
# 

# In[5]:


df.prof.nunique()


# Using all observations, Find the average and standard deviation for age
# 

# In[6]:


df['age'].mean()


# In[7]:


df['age'].std()


# Repeat the analysis by first filtering the data set to include one observation for each instructor with a total number of observations restricted to 94.
# 
# > first we drop duplicates using prof as a subset and assign it a new dataframe name called no_duplicates_ratings_df
# 

# In[13]:


no_duplicates_df = df.drop_duplicates(subset =['prof'])
no_duplicates_df.head()


# > Use the new dataset to get the mean of age
# 

# In[14]:


no_duplicates_df['age'].mean()


# In[15]:


no_duplicates_df['age'].std()


# ### Using a bar chart, demonstrate if instructors teaching lower-division courses receive higher average teaching evaluations.
# 

# In[16]:


df.head()


# Find the average teaching evaluation in both groups of upper and lower-division
# 

# In[19]:


df.groupby('division')['eval'].mean()


# In[20]:


division_eval = df.groupby('division')[['eval']].mean().reset_index()
division_eval


# Plot the barplot using the seaborn library
# 

# In[21]:


sns.set(style="whitegrid")
ax = sns.barplot(x="division", y="eval", data=division_eval)


# ### Plot the relationship between age and teaching evaluation scores.
# 

# Create a scatterplot with the scatterplot function in the seaborn library
# 

# In[23]:


ax = sns.scatterplot(x='age', y='eval', data=df)


# ### Using gender-differentiated scatter plots, plot the relationship between age and teaching evaluation scores.
# 

# Create a scatterplot with the scatterplot function in the seaborn library this time add the <code>hue</code> argument
# 

# In[24]:


ax = sns.scatterplot(x='age', y='eval', hue='gender',
                     data=df)


# ### Create a box plot for beauty scores differentiated by credits.
# 

# We use the <code>boxplot()</code> function from the seaborn library
# 

# In[25]:


ax = sns.boxplot(x='credits', y='beauty', data=df)


# ### What is the number of courses taught by gender?
# 

# We use the <code>catplot()</code> function from the seaborn library
# 

# In[26]:


sns.catplot(x='gender', kind='count', data=df)


# ### Create a group histogram of taught by gender and tenure
# 

# We will add the <code>hue = Tenure</code> argument
# 

# In[27]:


sns.catplot(x='gender', hue = 'tenure', kind='count', data=df)


# ### Add division as another factor to the above histogram
# 

# We add another argument named <code>row</code> and use the division variable as the row
# 

# In[28]:


sns.catplot(x='gender', hue = 'tenure', row = 'division',
            kind='count', data=df,
            height = 3, aspect = 2)


# ### Create a scatterplot of age and evaluation scores, differentiated by gender and tenure
# 

# Use the <code>relplot()</code> function for complex scatter plots
# 

# In[31]:


sns.relplot(x="age", y="eval", hue="gender",
            row="tenure",
            data=df, height = 3, aspect = 2)


# ### Create a distribution plot of teaching evaluation scores
# 

# We use the <code>distplot()</code> function from the seaborn library, set <code>kde = false</code> because we don'e need the curve
# 

# In[32]:


ax = sns.distplot(df['eval'], kde = False)


# ### Create a distribution plot of teaching evaluation score with gender as a factor
# 

# In[34]:


## use the distplot function from the seaborn library
sns.distplot(df[df['gender'] == 'female']['eval'], color='green', kde=False) 
sns.distplot(df[df['gender'] == 'male']['eval'], color="orange", kde=False) 
plt.show()


# ### Create a box plot - age of the instructor by gender
# 

# In[35]:


ax = sns.boxplot(x="gender", y="age", data=df)


# ### Compare age along with tenure and gender
# 

# In[36]:


ax = sns.boxplot(x="tenure", y="age", hue="gender",
                 data=df)


# ## Practice Questions
# 

# ### Question 1: Create a distribution plot of beauty scores with Native English speaker as a factor
# 
# *   Make the color of the native English speakers plot - orange and non - native English speakers - blue
# 

# In[40]:


sns.distplot(df[df['native'] == 'yes']['beauty'], color = 'orange', kde=False)
sns.distplot(df[df['native'] == 'no']['beauty'], color = 'blue', kde=False)


# ### Question 2: Create a Horizontal box plot of the age of the instructors by visible minority
# 

# In[45]:


sns.boxplot(x='age', y='minority', data=df)


# ### Question 3: Create a group histogram of tenure by minority and add the gender factor
# 

# In[52]:


sns.catplot(x='tenure', hue='minority', row='gender', kind='count',  data=df)


# ### Question 4: Create a boxplot of the age variable
# 

# In[53]:


sns.boxplot(x= 'age',data=df)

