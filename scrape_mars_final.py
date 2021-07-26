
import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_news_url = "https://redplanetscience.com/"
    browser.visit(mars_news_url)
    html = browser.html
    soup_news = bs(html, "html.parser")
    
    news_title = soup_news.find(class_="content_title").text
    news_body = soup_news.find('div', class_='article_teaser_body').text
    
    img_url = "https://spaceimages-mars.com/"
    browser.visit(img_url)
    html = browser.html
    featured_img_soup = bs(html, "html.parser")

    featured_img_relative_path = featured_img_soup.find_all("img")[1]["src"]
    featured_img_url = img_url + featured_img_relative_path

    
    facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(facts_url)
    html = browser.html
    soup_facts = bs(html, "html.parser")
    
    facts_table = pd.read_html(facts_url)
    mars_table = facts_table[1]
    mars_table.columns =['Description', 'Value']
    mars_table_df = pd.DataFrame(mars_table)
    mars_table_df = mars_table_df.to_html()
         
    hemispheres_url = "https://marshemispheres.com/"
    browser.visit(hemispheres_url)
    html = browser.html
    soup_hemispheres = bs(html, "html.parser")
    all_items = soup_hemispheres.find_all('div', class_='item')
    urls = []
    titles = []
    for item in all_items:
        urls.append(hemispheres_url + item.find('a')['href'])
        titles.append(item.find('h3').text.strip())

    img_urls = []
    for each_url in urls:
        browser.visit(each_url)
        html = browser.html
        soup = bs(html, 'html.parser')

        each_url = hemispheres_url + soup.find('img',class_='wide-image')['src']
        img_urls.append(each_url)

    hemisphere_urls = []
    for i in range(len(titles)):
        hemisphere_urls.append({'title':titles[i],'img_url':img_urls[i]})
    
 
    m_data = {}
  
    m_data["news_title"] = news_title 

    m_data["news"] = news_body

    m_data["featured_img_url"] = featured_img_url

    m_data["mars_table_html"] = mars_table_df

    m_data["hemisphere_urls"] = hemisphere_urls

    browser.quit()
    
    return m_data
    
    
    
