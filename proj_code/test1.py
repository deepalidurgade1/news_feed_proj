# Extract all feeds from RSS feed List wepage
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

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


# Extract all feeds from RSS feed List wepage
feed_links = []
news_items = []
result_df = pd.DataFrame(news_items, columns=['RSS_Feed', 'Title', 'Description', 'Body', 'RSS_Feed_URL',
                                              'Publish_date', 'Inserted_time_stamp', 'Sentiment'])
url = 'https://timesofindia.indiatimes.com/rss.cms'
r1 = requests.get(url)                                     # Request
print(r1.status_code)

coverpage = r1.content                                     # We'll save in coverpage the cover page content

# Soup creation
soup1 = BeautifulSoup(coverpage, 'html.parser')            # 'html5lib')
coverpage_news = soup1.find_all('span', class_='rssp')     # News identification  ## span class="rssp"
for n in range(0, len(coverpage_news)):
    link = coverpage_news[n].find('a')['href']             # find all links
    feed_links.append(link)

print(feed_links)
print(len(feed_links))

# code for storing the details of various feeds in pandas DF
for i in range(len(feed_links)):
    vgm_url = feed_links[i]
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
        news_item['Body'] = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum"""
        news_item['RSS_Feed_URL'] = x.link.text
        news_item['Publish_date'] = x.pubDate.text
        news_item['Inserted_time_stamp'] = datetime.now()
        news_item['Sentiment'] = "Happy"
        news_items.append(news_item)

    # print(news_items)
    df = pd.DataFrame(news_items, columns=['RSS_Feed', 'Title', 'Description', 'Body', 'RSS_Feed_URL', 'Publish_date',
                                           'Inserted_time_stamp', 'Sentiment'])

    # df.head()
    result_df = result_df.append(df)
    # df.to_csv('result/data1.csv', index=False, encoding='utf-8')
final_df = result_df.drop_duplicates()
print(final_df)
print(len(final_df))

# Save result to DB
# create connection string = 'postgresql://<user>:<password>@<host>:<port>/<db>'
conn_string = 'postgresql://postgres_admin:postgres123@postgres-db-identifier1.cxfegqfzlnwt.ap-south-1.' \
              'rds.amazonaws.com:5432/db_news_feed'

engine = create_engine(conn_string)                          # forms a connection to the PostgresSQL database
with engine.connect() as connection:
    final_df.to_sql('table3', con=connection, if_exists='replace', index=False)


# for getting Paragraph
# feed_link = news_items[-1]['link']
# print(feed_link)
# html_text1 = requests.get(feed_link).text

# page = urlopen(feed_link)
# html_text1 = page.read().decode("utf-8")
# soup1 = BeautifulSoup(html_text1, "html.parser")
# print(soup1.find_all('p'))                  # get all paragraphs