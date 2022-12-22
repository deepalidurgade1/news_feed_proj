# Process1 : 1) Read table1 to get url of rss feed list whose active_flag = 1
#            2) extract all rss feed urls from above url
#            3) save those url in table 2 and make active flag = 2 (newly inserted data)

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

# create connection string = 'postgresql://<user>:<password>@<host>:<port>/<db>'
conn_string = 'postgresql://postgres_admin:postgres123@postgres-db-identifier1.cxfegqfzlnwt.ap-south-1.' \
              'rds.amazonaws.com:5432/db_news_feed'

engine = create_engine(conn_string)                          # forms a connection to the PostgresSQL database

# Function to read Table1
def read_table1():
    list1 = []
    print("--------------Reading Table1---------------")
    with engine.connect() as connection:                         # using "with" don't require closing of connection
        # query to read on condition
        read_query = "select news_url from table1 where active_flag = '1'"
        result_set = connection.execute(read_query)
        # print(result_set)                    # gives "sqlalchemy.engine.cursor.LegacyCursorResult object"
        for res in result_set:
            list1.append(res[0])                # the news news_url is stored in a list
        print(list1)
    print("------------------Table1 Read successfully------------------")
    return list1

# Function to write into table2
def write_to_table2(df):
    print("--------------Writing into Table2---------------")
    with engine.connect() as connection:                         # using "with" don't require closing of connection
        # query to write into table
        df.to_sql('table2', con=connection, if_exists='replace', index=False)              # write a DF into table
    print("--------------Writing into Table2 successful---------------")
    return

# function to get RSS Feed URLs for given website
def get_rss_feed(news_url):
    feed_links = []
    cols = ['News_URL', 'RSS_Feed', 'Active_flag', 'Updated_Time_stamp']

    if news_url is None:
        print("News URL should not be null")
    else:
        # 2) Append appropriate text for getting rss_feed_list
        news_web_rss = {
            'https://timesofindia.indiatimes.com/': 'rss.cms',
            'https://www.ndtv.com/': 'rss',
            'https://www.hindustantimes.com/': 'rss',
            'https://www.business-standard.com/': 'rss-feeds/listing/'
        }

        if news_url in news_web_rss.keys():                   # check which news_url is to access, accordingly append
            append_str = news_web_rss[news_url]               # a string to get appropriate rss_list_url
            rss_list_url = news_url + append_str

        print("news_url: ", news_url)
        print("rss_list: ", rss_list_url)

        r1 = requests.get(rss_list_url)                                  # Request
        print(r1.status_code)
        coverpage = r1.content                                          # We'll save in coverpage the cover page content
        # Soup creation
        soup1 = BeautifulSoup(coverpage, 'html.parser')                  # 'html5lib')       Parse the html page content
        # coverpage_feeds = soup1.find_all('div', id_='main - copy')
        coverpage_feeds = soup1.find_all('span', class_='rssp')          # identification  of <span class="rssp">
        for n in range(0, len(coverpage_feeds)):                         # get feed links one by one
            link_item = {}
            link = coverpage_feeds[n].find('a')['href']                  # find link
            link_item['News_URL'] = news_url
            link_item['RSS_Feed'] = link
            link_item['Active_flag'] = 2
            link_item['Updated_Time_stamp'] = datetime.now()

            feed_links.append(link_item)                                 # create data in required format

        # print(feed_links)
        df1 = pd.DataFrame(feed_links, columns=cols)                      # create dataframe
        tbl2_df = df1.drop_duplicates()

        print(tbl2_df)
        print(len(tbl2_df))

    return tbl2_df


# Driver Program
# 1) Read table1 to get news url whose active_flag = 1
list1 = read_table1()

for i in list1:
    df = get_rss_feed(i)                        # 2) get rss feed urls from given url extracted from table1
    write_to_table2(df)                         # 3) write the Dataframe to table2

engine.dispose()                                # close all connections of the connection pool.


