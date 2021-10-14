#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup

class Scraper:
    
    def __init__(self,url,item):
        #https://www.flipkart.com/search?q=mobiles
        self.final_url = url + '/search?q=' + item
        self.pull_data(self.final_url)
    
    def pull_data(self,finalurl):
        print(finalurl)
        self.result=requests.get(finalurl)
        
        self.soup=BeautifulSoup(self.result.content)
        
        self.result=self.soup.findAll('div',attrs={'class','_3pLy-c row'})
        count=0
        for item in self.result:
            print(item.text)
            

    
    def refine_data(self):
        pass


# In[3]:


scraper=Scraper('https://www.flipkart.com','mobiles')


# In[30]:


import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,url,item):
        # https://www.flipkart.com/search?q=mobiles
        self.final_url = url + '/search?q=' + item
        self.pull_data(self.final_url)

    def pull_data(self, finalurl):
        print(finalurl)
        self.result = requests.get(finalurl)
        # print(result.status_code)
        # print(result.text)

        self.soup = BeautifulSoup(self.result.content)
        # print(self.soup.prettify())
        
        self.tagline = self.soup.find('div',attrs={'class','_4rR01T'})
        # print(self.tagline)
        print(self.tagline.text)
        
        self.ratings=self.soup.find('div',attrs={'class','_1wB99o'})
        #print(self.ratings)
        print(self.ratings.text)
        
        self.allitems=self.soup.find('div',attrs={'class','_1YokD2_3Mn1Gg'})
        #print(self.ratings)
        print(self.ratings.text)
        
        f
            
            


# In[31]:


scraper=Scraper('https://www.flipkart.com','mobiles')


# In[ ]:





# In[ ]:




