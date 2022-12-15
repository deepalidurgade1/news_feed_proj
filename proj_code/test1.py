import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Getting the current date and time
dt = datetime.now()
print(dt)

# scraping function
# def hackernews_rss():
#     try:
#         res = requests.get("https://www.business-standard.com/")
#         print(res)
#         return print('The scraping job succeeded: ', res)
#     except Exception as e:
#         print('The scraping job failed. See exception: ')
#         print(e)
#
# print('--------------Starting scraping-------------------------------')
# r = hackernews_rss()
# # print(r)
# print("--------------------------------------------------------------")
# # html_string = r.text
# # print(html_string)
# print('-------------------------------Finished scraping-------------------------------')
# 

# code for storing the details of various feeds in pandas DF

vgm_url = 'https://www.business-standard.com/rss/home_page_top_stories.rss'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, features="xml")
# print(soup)
items = soup.findAll('item')
# print(items)

news_items = []
# scarring HTML tags such as Title, Description, Links and Publication date
for item in items:
    news_item = {}
    news_item['RSS_Feed'] = vgm_url
    news_item['Title'] = item.title.text
    news_item['Description'] = item.description.text
    news_item['Body'] = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
                        industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
                        scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap 
                        into electronic typesetting, remaining essentially unchanged"""
    news_item['RSS_Feed_URL'] = item.link.text
    news_item['Publish_date'] = item.pubDate.text
    news_item['Sentiment'] = "Happy"
    news_item['Inserted_on'] = datetime.now()
    news_items.append(news_item)

print(news_items)

# feed_link = news_items[-1]['link']
# print(feed_link)
# html_text1 = requests.get(feed_link).text

# page = urlopen(feed_link)
# html_text1 = page.read().decode("utf-8")
# soup1 = BeautifulSoup(html_text1, "html.parser")
# print(soup1.find_all('p'))

df = pd.DataFrame(news_items, columns=['RSS_Feed', 'Title', 'Description', 'Body', 'RSS_Feed_URL', 'Publish_date',
                                       'Sentiment', 'Inserted_on'])
# df.head()
df.to_csv('result/data1.csv', index=False, encoding='utf-8')

print("--------------file saved as csv------------------")

# soup = BeautifulSoup(html_text, 'html.parser')
# print(soup)
# for link in soup.find_all('a'):
#print(link.get('href'))