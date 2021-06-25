#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
get_ipython().system('pip install html5lib')


# In[4]:


from bs4 import BeautifulSoup
import requests
import re


# In[6]:


Page =requests.get("https://internshala.com/fresher-jobs")
Page


# In[7]:


Page.content


# In[9]:


soup=BeautifulSoup(Page.content)
soup


# In[10]:


first_title=soup.find('div',class_="heading_4_5 profile")
first_title


# In[12]:


first_title.text


# In[13]:


first_title.text.replace('\n','')


# In[14]:


first_company=soup.find('a',class_="link_display_like_text")
first_company


# In[16]:


first_company.text


# In[17]:


first_company.text.replace('\n','')


# In[18]:


first_Date=soup.find('div',class_="other_detail_item")
first_Date


# In[19]:


first_Date.text.replace('\n','')


# In[20]:


first_CTC=soup.find('i',class_="ic-16-money")
first_CTC


# In[21]:


first_CTC.text


# In[22]:


titles=soup.find_all('div',class_="heading_4_5 profile")
titles


# In[23]:


job_titles=[]
for i in titles:
    job_titles.append(i.text)
job_titles


# In[25]:


companies=soup.find_all('a',class_="link_display_like_text")
companies


# In[24]:


company_names=[]
for i in companies:
    company_names.appned(i.text(strip())
company_names


# In[25]:


Dates=soup.find_all('div',class_="other_detail_item")
Dates


# In[26]:


job_Dates=[]
for i in Dates:
    job_Dates.append(i.text)
job_Dates


# In[27]:


job_Dates=[]
for i in Dates:
    job_Dates.append(i.text.replace("\n",''))
job_Dates


# In[36]:


#print(titles,company,Dates)


# In[41]:


import pandas as pd
jobs['titles']=job_titles
jobs['company']=comapny_names
Jobs['Date and CTC']=Date and CTC_list


# In[42]:


jobs.to_csv()


# In[ ]:




