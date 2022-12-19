# Parse a feed url (single url)
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
dt = datetime.now()
print(dt)

# Extract all feeds from RSS feed List wepage
feed_links = []
news_items = []

vgm_url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, features="xml")
items = soup.findAll('item')
# print(items)
# scarring HTML tags such as Title, Description, Links and Publication date
for x in items:
    news_item = {}
    news_item['RSS_Feed'] = vgm_url
    news_item['Title'] = x.title.text
    news_item['Description'] = x.description.text
    news_item['Body'] = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum 
        has been the industry's standard dummy text ever since tshe 1500s, when an unknown printer took a galley of 
        type and scrambled it to make a type specimen book. """
    news_item['RSS_Feed_URL'] = x.link.text
    news_item['Publish_date'] = x.pubDate.text
    news_item['Sentiment'] = "Happy"
    news_item['Inserted_on'] = datetime.now()

    news_items.append(news_item)

# print(news_items)
df = pd.DataFrame(news_items, columns=['RSS_Feed', 'Title', 'Description', 'Body', 'RSS_Feed_URL', 'Publish_date',
                                       'Sentiment', 'Inserted_on'])
print(df.shape[0])
print(df.shape[1])