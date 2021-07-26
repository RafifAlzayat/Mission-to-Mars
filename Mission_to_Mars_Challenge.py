#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
import pandas as pd
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:



executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:



mars_news_url = "https://redplanetscience.com/"
browser.visit(mars_news_url)


# In[4]:


html = browser.html
soup_news = soup(html, "html.parser")
type(soup_news)


# In[5]:



news_title = soup_news.find(class_="content_title").text
news_title


# In[6]:


news_p = soup_news.find('div', class_='article_teaser_body').text
news_p


# In[7]:



mars_data = {"news_title": news_title,"news_p": news_p}


# In[8]:



img_url = "https://spaceimages-mars.com/"
browser.visit(img_url)


# In[9]:



html = browser.html
featured_img_soup = soup(html, "html.parser")


# In[10]:


featured_img_relative_path = featured_img_soup.find_all("img")[1]["src"]


featured_img_url = img_url + featured_img_relative_path
featured_img_url


# In[11]:


facts_url = "https://galaxyfacts-mars.com/"
browser.visit(facts_url)


# In[12]:


html = browser.html
soup_facts = soup(html, "html.parser")
type(soup_facts)


# In[13]:


facts_table = pd.read_html(facts_url)
facts_table


# In[14]:



mars_table = facts_table[1]
mars_table.columns =['Description', 'Value']
mars_table_df = pd.DataFrame(mars_table)


# In[15]:


mars_table_df.to_html("mars_table.html", index = False)


# In[16]:



hemispheres_url = "https://marshemispheres.com/"
browser.visit(hemispheres_url)
html = browser.html
soup_hemispheres = soup(html, "html.parser")
all_items = soup_hemispheres.find_all('div', class_='item')
all_items


# In[17]:


urls = []
titles = []
for item in all_items:
    urls.append(hemispheres_url + item.find('a')['href'])
    titles.append(item.find('h3').text.strip())


# In[18]:


urls
titles


# In[19]:


img_urls = []
for each_url in urls:
    browser.visit(each_url)
    html = browser.html
    a = soup(html, 'html.parser')

    each_url = hemispheres_url + a.find('img',class_='wide-image')['src']
    img_urls.append(each_url)
    
img_urls


# In[20]:


hemisphere_urls = []

for i in range(len(titles)):
    hemisphere_urls.append({'title':titles[i],'img_url':img_urls[i]})

hemisphere_urls


# In[21]:


for i in range(len(hemisphere_urls)):
    print(hemisphere_urls[i]['title'])
    print(hemisphere_urls[i]['img_url'] + '\n')


# In[ ]:





# In[ ]:




