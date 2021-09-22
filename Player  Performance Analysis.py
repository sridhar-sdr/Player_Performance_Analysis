
# coding: utf-8

# ## Analyzing the T20 batting performance of the famous Indian cricketer (Rohit Sharma)

# In[25]:



# importing essential libraries and packages
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns


# Read the data

# In[22]:


# Reading the data
data= pd.read_csv('Untitled spreadsheet - Sheet1.csv')

data


# In[5]:


get_ipython().run_line_magic('pylab', 'inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('Hitman_apr5_nL4b0Eg_mkWj5hb_1_qs4QpIy_FAC1mG5_qchZ22J_BkVTAV020210916172806.jpg')
imgplot = plt.imshow(img)
plt.show()


# In[6]:


not_outs = data['100s'].sum() # number of not outs in career
print('Not outs:', not_outs)


# In[7]:


p=data.iloc[12:24]
p=d1
d1= data.rename(columns={"Match type": "Opposition"})
d1


# In[24]:


#Creating the dataframe to show the the runs scored vs different opposition by Rohit Sharma
from pandas import DataFrame

Data =  ['Runs','Match type']

df = DataFrame(p,columns=['Runs','Match type'])

print (df)


# ## Centuries against different teams

# In[9]:


p[['Match type','100s']]


# In[10]:


N100s = pd.DataFrame(p.groupby('Match type')['100s'].sum())
N100s.plot(kind='bar', title='100s against different oppositions', figsize=(8, 5))
plt.ylim(0,3);


# ## Number of Not out against different opposition

# In[11]:


Not_out = pd.DataFrame(p.groupby('Match type')['NO'].sum())
Not_out.plot(kind='bar', title='Number of Not out against different oppositions', figsize=(8, 5))
plt.ylim(0,5);


# ## Number of match played against different oppositions 

# In[12]:


Different_opposition = pd.DataFrame(p.groupby('Match type')['Mat'].sum())
Different_opposition.plot(kind='bar', title='Number of match played against different oppositions', figsize=(8, 5))
plt.ylim(0,30);


# In[ ]:


d1[['Opposition','Span','Mat','Inns','Runs','HS','Avg','SR']]

c=d1.iloc[0:7]
c


# # Runs scored in the ICC tournaments

# In[14]:


#splitting required rows
c=d1.iloc[0:7]
c
#Dropping the rows
df = c.drop([3,4])
df


# In[15]:


d=df.Mat.sum()

d1=df.Runs.sum()

k= d1/d

print('Number of Matches Played in official Tournaments:',d)
print('Number of Runs Scores Played:',d1)
print('Average in the tournaments:',k)


# ## Runs scored under different captaincy

# In[16]:


q1=data.iloc[24:28]
q1

q3=q1.rename(columns={"Match type": "Captaincy"})
q3
q4=q3.drop([25])
q4
# Converting string into Numeric
q4['HS'] = q4['HS'].astype(int)


# ## Highest score in T20 under his Captaincy

# runs_scored_by_opposition = pd.DataFrame(q4.groupby('Captaincy')['HS'].sum())
# runs_scored_by_opposition.plot(kind='bar', title='Highest score in T20 under his Captaincy', figsize=(8, 5))
# plt.ylim(0,200);
# 
# 

# # Runs scored in india and other countries

# In[18]:


#splitting the data
l=data.iloc[3:5]
l


# In[26]:


away = pd.DataFrame(l.groupby('Match type')['100s'].sum())
away.plot(kind='bar', title='Runs scored in home and away against different oppositions', figsize=(8, 5))
plt.ylim(0,10);


# In[20]:


import pandas as pd
import plotly.express as px
import plotly.io as pio
grouping = df.groupby('Opposition')['Runs', 'Opposition', 'Inns','NO'].sum().reset_index()
fig = px.line(grouping, y="Runs", x='Opposition',
             title="Total runs scored by Rohit Shama in the all ICC Tournaments")
fig.show()


# Graph shows that Rohit scored less runs in the semi-finals and finals.  However, sharma scored well in most of the league matches in the tournaments.
# 

# Conclusion:
#     Rohit sharma is one of the good openers in the world and He played some brilliant innings. He scored two double centuries in ODI. However, he needs to perform in the important matches like semi,finals in the world cup matches.
