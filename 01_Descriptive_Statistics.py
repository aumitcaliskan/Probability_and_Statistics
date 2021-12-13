#!/usr/bin/env python
# coding: utf-8

# # Descriptive Statistics
# 

# ## Objectives
# 

# *   Import Libraries
# *   Read in Data
# *   Lab exercises and questions
# 

# ## Import Libraries
# 

# All Libraries required for this lab are listed below. The libraries pre-installed on Skills Network Labs are commented. If you run this notebook in a different environment, e.g. your desktop, you may need to uncomment and install certain libraries.
# 

# In[ ]:


#! mamba install pandas==1.3.3
#! mamba install numpy=1.21.2
#!  mamba install matplotlib=3.4.3-y


# Import the libraries we need for the lab
# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Read in the csv file from the URL using the request library
# 

# In[2]:


ratings_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
df=pd.read_csv(ratings_url)


# ## Data Description
# 
# | Variable    | Description                                                                                                                                          |
# | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
# | minority    | Does the instructor belong to a minority (non-Caucasian) group?                                                                                      |
# | age         | The professor's age                                                                                                                                  |
# | gender      | Indicating whether the instructor was male or female.                                                                                                |
# | credits     | Is the course a single-credit elective?                                                                                                              |
# | beauty      | Rating of the instructor's physical appearance by a panel of six students averaged across the six panelists and standardized to have a mean of zero. |
# | eval        | Course overall teaching evaluation score, on a scale of 1 (very unsatisfactory) to 5 (excellent).                                                    |
# | division    | Is the course an upper or lower division course?                                                                                                     |
# | native      | Is the instructor a native English speaker?                                                                                                          |
# | tenure      | Is the instructor on a tenure track?                                                                                                                 |
# | students    | Number of students that participated in the evaluation.                                                                                              |
# | allstudents | Number of students enrolled in the course.                                                                                                           |
# | prof        | Indicating instructor identifier.                                                                                                                    |
# 

# ## Display information about the dataset
# 
# 1.  Structure of the dataframe
# 2.  Describe the dataset
# 3.  Number of rows and columns
# 

# print out the first five rows of the data
# 

# In[3]:


df.head()


# get information about each variable
# 

# In[4]:


df.info()


# get the number of rows and columns - prints as (number of rows, number of columns)
# 

# In[5]:


df.shape


# ### Can you identify whether the teachers' Rating data is a time series or cross-sectional?
# 

# Print out the first ten rows of the data
# 
# 1.  Does it have a date or time variable? - No - it is not a time series dataset
# 2.  Does it observe more than one teacher being rated? - Yes - it is cross-sectional dataset
# 
# > The dataset is a Cross-sectional
# 

# In[6]:


df.head(10)


# ### Find the mean, median, minimum, and maximum values for students
# 

# Find Mean value for students
# 

# In[7]:


df['students'].mean()


# Find the Median value for students
# 

# In[8]:


df['students'].median()


# Find the Minimum value for students
# 

# In[9]:


df['students'].min()


# Find the Maximum value for students
# 

# In[10]:


df['students'].max()


# ### Produce a descriptive statistics table
# 

# In[13]:


df.describe()


# ### Create a histogram of the beauty variable and briefly comment on the distribution of data
# 

# using the <code>matplotlib</code> library, create a histogram
# 

# In[14]:


plt.hist(df['beauty'])


# here are few conclusions from the histogram
# most of the data for beauty is around the -0.5 and 0
# the distribution is skewed to the right
# therefore looking at the data we can say the mean is close to 0
# 

# ### Does average beauty score differ by gender? Produce the means and standard deviations for both male and female instructors.
# 

# Use a group by gender to view the mean scores of the beauty we can say that beauty scores differ by gender as the mean beauty score for women is higher than men
# 

# In[21]:


df.groupby('gender').agg({'beauty':['mean', 'std', 'var']})


# ### Calculate the percentage of males and females that are tenured professors. Will you say that tenure status differ by gender?
# 

# First groupby to get the total sum
# 

# In[22]:


tenure_count = df[df.tenure == 'yes'].groupby('gender').agg({'tenure': 'count'}).reset_index()


# Find the percentage
# 

# In[23]:


tenure_count['percentage'] = 100 * tenure_count.tenure/tenure_count.tenure.sum()
tenure_count


# In[30]:


tc = df[df['tenure'] == 'yes'].groupby('gender').agg({'tenure':'count'})


# In[31]:


tc


# In[37]:


tc['percentage'] = tc.tenure/tc.tenure.sum()*100


# In[38]:


tc


# ## Practice Questions
# 

# ### Question 1: Calculate the percentage of visible minorities are tenure professors. Will you say that tenure status differed if teacher was a visible minority?
# 

# In[45]:


mt = df.groupby('minority').agg({'tenure':'count'})


# In[46]:


mt


# In[47]:


mt['percentage'] = mt.tenure/mt.tenure.sum()*100


# In[48]:


mt


# ### Question 2: Does average age differ by tenure? Produce the means and standard deviations for both tenured and untenured professors.
# 

# In[51]:


df.groupby('tenure').agg({'age': ['mean','std']})


# ### Question 3: Create a histogram for the age variable.
# 

# In[56]:


plt.hist(df['age'])


# ### Question 4: What is the Median evaluation score for tenured Professors?
# 

# In[60]:


df[df['tenure'] == 'yes']['eval'].median()

