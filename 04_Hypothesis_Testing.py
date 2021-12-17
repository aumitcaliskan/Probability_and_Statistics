#!/usr/bin/env python
# coding: utf-8

# # **Hypothesis Testing**
# 

# The goal of hypothesis testing is to answer the question, “Given a sample and an apparent effect, what is the probability of seeing such an effect by chance?” The first step is to quantify the size of the apparent effect by choosing a test statistic (t-test, ANOVA, etc). The next step is to define a null hypothesis, which is a model of the system based on the assumption that the apparent effect is not real. Then compute the p-value, which is the probability of the null hypothesis being true, and finally interpret the result of the p-value, if the value is low, the effect is said to be statistically significant, which means that the null hypothesis may not be accurate.
# 

# ## Objectives
# 

# *   Import Libraries
# *   Lab exercises
#     *   Stating the hypothesis
#     *   Levene's Test for equality
#     *   Preparing your data for hypothesis testing
# *   Quiz
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
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats


# Read in the csv file from the URL using the request library
# 

# In[2]:


ratings_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
df = pd.read_csv(ratings_url)


# ### T-Test: Using the teachers' rating data set, does gender affect teaching evaluation rates?
# 

# We will be using the t-test for independent samples. For the independent t-test, the following assumptions must be met.
# 
# *   One independent, categorical variable with two levels or group
# *   One dependent continuous variable
# *   Independence of the observations. Each subject should belong to only one group. There is no relationship between the observations in each group.
# *   The dependent variable must follow a normal distribution
# *   Assumption of homogeneity of variance
# 

# State the hypothesis
# 
# *   $H\_0: µ\_1 = µ\_2$ ("there is no difference in evaluation scores between male and females")
# *   $H\_1: µ\_1 ≠ µ\_2$ ("there is a difference in evaluation scores between male and females")
# 

# We can plot the dependent variable with a historgram
# 

# In[4]:


ax = sns.distplot(df['eval'],
                  bins=20,
                  kde=True,
                  color='red',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
## we can assume it is normal


# We can use the Levene's Test in Python to check test significance
# 

# In[6]:


scipy.stats.levene(df[df['gender'] == 'female']['eval'],
                   df[df['gender'] == 'male']['eval'], center='mean')

# since the p-value is greater than 0.05 we can assume equality of variance


# Use the <code>ttest_ind</code> from the <code>scipy_stats</code> library
# 

# In[7]:


scipy.stats.ttest_ind(df[df['gender'] == 'female']['eval'],
                   df[df['gender'] == 'male']['eval'], equal_var = True)


# **Conclusion:** Since the p-value is less than alpha value 0.05, we reject the null hypothesis as there is enough proof that there is a statistical difference in teaching evaluations based on gender
# 

# ### ANOVA: Using the teachers' rating data set, does beauty  score for instructors  differ by age?
# 

# First, we group the data into cateries as the one-way ANOVA can't work with continuous variable - using the example from the video, we will create a new column for this newly assigned group our categories will be teachers that are:
# 
# *   40 years and younger
# *   between 40 and 57 years
# *   57 years and older
# 

# In[9]:


df.loc[(df['age'] <= 40), 'age_group'] = '40 years and younger'
df.loc[(df['age'] > 40)&(df['age'] < 57), 'age_group'] = 'between 40 and 57 years'
df.loc[(df['age'] >= 57), 'age_group'] = '57 years and older'


# State the hypothesis
# 
# *   $H\_0: µ\_1 = µ\_2 = µ\_3$ (the three population means are equal)
# *   $H\_1:$ At least one of the means differ
# 

# Test for equality of variance
# 

# In[10]:


scipy.stats.levene(df[df['age_group'] == '40 years and younger']['beauty'],
                   df[df['age_group'] == 'between 40 and 57 years']['beauty'], 
                   df[df['age_group'] == '57 years and older']['beauty'], 
                   center='mean')
# since the p-value is less than 0.05, the variance are not equal, for the purposes of this exercise, we will move along


# First, separate the three samples (one for each job category) into a variable each.
# 

# In[12]:


forty_lower = df[df['age_group'] == '40 years and younger']['beauty']
forty_fiftyseven = df[df['age_group'] == 'between 40 and 57 years']['beauty']
fiftyseven_older = df[df['age_group'] == '57 years and older']['beauty']


# Now, run a one-way ANOVA.
# 

# In[14]:


f_statistic, p_value = scipy.stats.f_oneway(forty_lower, forty_fiftyseven, fiftyseven_older)
print("F_Statistic: {0}, P-Value: {1}".format(f_statistic,p_value))


# **Conclusion:** Since the p-value is less than 0.05, we will reject the null hypothesis as there is significant evidence that at least one of the means differ.
# 

# ### ANOVA: Using the teachers' rating data set, does teaching  evaluation  score for instructors  differ  by age?
# 

# Test for equality of variance
# 

# In[15]:


scipy.stats.levene(df[df['age_group'] == '40 years and younger']['eval'],
                   df[df['age_group'] == 'between 40 and 57 years']['eval'], 
                   df[df['age_group'] == '57 years and older']['eval'], 
                   center='mean')


# In[16]:


forty_lower_eval = df[df['age_group'] == '40 years and younger']['eval']
forty_fiftyseven_eval = df[df['age_group'] == 'between 40 and 57 years']['eval']
fiftyseven_older_eval = df[df['age_group'] == '57 years and older']['eval']


# In[17]:


f_statistic, p_value = scipy.stats.f_oneway(forty_lower_eval, forty_fiftyseven_eval, fiftyseven_older_eval)
print("F_Statistic: {0}, P-Value: {1}".format(f_statistic,p_value))


# **Conclusion:** Since the p-value is greater than 0.05, we will fail to reject the null hypothesis as there is no significant evidence that at least one of the means differ.
# 

# ### Chi-square: Using the teachers' rating data set, is there an association between tenure and gender?
# 

# State the hypothesis:
# 
# *   $H\_0:$ The proportion of teachers who are tenured is independent of gender
# *   $H\_1:$ The proportion of teachers who are tenured is associated with gender
# 

# Create a Cross-tab table
# 

# In[18]:


cont_table  = pd.crosstab(df['tenure'], df['gender'])
cont_table


# Use the <code>scipy.stats</code> library and set correction equals False as that will be the same answer when done by hand, it returns: 𝜒2 value, p-value, degree of freedom, and expected values.
# 

# In[25]:


scipy.stats.chi2_contingency(cont_table, correction = True)


# **Conclusion:** Since the p-value is greater than 0.05, we fail to reject the null hypothesis. As there is no sufficient evidence that teachers are tenured as a result of gender.
# 

# ### Correlation: Using the teachers rating dataset, Is teaching  evaluation  score correlated with  beauty score?
# 

# State the hypothesis:
# 
# *   $H\_0:$ Teaching evaluation score is not correlated with beauty score
# *   $H\_1:$ Teaching evaluation score is correlated with beauty score
# 

# Since they are both continuous variables we can use a pearson correlation test and draw a scatter plot
# 

# In[26]:


ax = sns.scatterplot(x="beauty", y="eval", data=df)


# In[27]:


scipy.stats.pearsonr(df['beauty'], df['eval'])


# **Conclusion:** Since the p-value  (Sig. (2-tailed)  < 0.05, we reject  the Null hypothesis and conclude that there  exists a relationship between  beauty and teaching evaluation score.
# 

# ## Practice Questions
# 

# ### Question 1: Using the teachers rating data set, does tenure affect teaching evaluation scores?
# 
# *   Use α = 0.05
# 

# In[49]:


# null hypo: there is no difference


# In[30]:


sns.distplot(df['eval'], bins=20, kde=True)


# In[33]:


scipy.stats.levene(df[df['tenure'] == 'yes']['eval'], df[df['tenure'] == 'no']['eval'], center='mean')


# In[35]:


# p value > 0.05 fail to reject so variances are equal

scipy.stats.ttest_ind(df[df['tenure'] == 'yes']['eval'], df[df['tenure'] == 'no']['eval'], equal_var=True)

# p value < 0.05 reject so tenured affects eval


# ### Question 2: Using the teachers rating data set, is there an association between age and tenure?
# 
# *   Discretize the age into three groups 40 years and youngers, between 40 and 57 years, 57 years and older (This has already been done for you above.)
# *   What is your conclusion at α = 0.01 and α = 0.05?
# 

# In[36]:


# null hypo: there is no association betwwen age and tenure
# alternative hypo: there is association betwwen age and tenure


# In[40]:


ct = pd.crosstab(df['tenure'],df['age_group'])
ct


# In[42]:


#categorical chi square test

scipy.stats.chi2_contingency(ct,correction=True)


# In[43]:


# α = 0.01, p value > α fail to reject
# α = 0.05, p value < α reject


# ### Question 3: Test for equality of variance for beauty scores between tenured and non-tenured instructors
# 
# *   Use α = 0.05
# 

# In[44]:


scipy.stats.levene(df[df['tenure'] == 'yes']['beauty'], df[df['tenure'] == 'no']['beauty'], center='mean')


# In[45]:


print('\u03B1')


# In[46]:


# p value > α fail to reject variances are equal


# ### Question 4: Using the teachers rating data set, is there an association between visible minorities and tenure?
# 
# *   Use α = 0.05
# 

# In[50]:


# null hypo : there is no association between visible minorities and tenure


# In[54]:


ct = pd.crosstab(df['tenure'],df['minority'])
ct


# In[56]:


#categorical chi square test

scipy.stats.chi2_contingency(ct,correction=True)


# In[57]:


# p > α fail to reject so variances are equal

