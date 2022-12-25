# Parse a feed url (single url)

# Process 2 : 1) Read table2 and extract the rss_feed_url
#             2) Open the URL and Parse it to extract details from it (link, news_title, description, pub_date etc.)
#             3) pass the "description" of news to comprehend for getting "Sentiment"
#             4) Save the extracted content as DF and write it into table3

import boto3
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
from sqlalchemy import create_engine
from goose3 import Goose

# Function to create Database connection
def create_db_connection():
    # create connection string = 'postgresql://<user>:<password>@<host>:<port>/<db>'
    conn_string = 'postgresql://postgres_admin:postgres123@postgres-db-identifier1.cxfegqfzlnwt.ap-south-1.' \
                  'rds.amazonaws.com:5432/db_news_feed'

    engine = create_engine(conn_string)  # forms a connection to the PostgresSQL database
    return engine


# Function to read Table2
def read_table2():
    print("-----------------------Reading Table2 ---------------------")
    with Engine.connect() as connection:  # using "with" don't require closing of connection
        # query to read on condition
        read_query = 'SELECT "RSS_Feed" FROM "public"."table2" WHERE "Active_flag" = 2 LIMIT 1'
        result_set = connection.execute(read_query)
        print(result_set)  # gives "sqlalchemy.engine.cursor.LegacyCursorResult object"
        for res in result_set:
            link = res[0]                # the RSS_Feed is taken from tuple & saved in a variable
    print("-----------------------Reading table2 Successful------------------")
    return link

# Function to write into table3
def write_to_table2_3(df, link):
    print("------------------- Writing into table3 -----------------------")
    with Engine.connect() as connection:  # using "with" don't require closing of connection
        # query to write into table
        df.to_sql('table3', con=connection, if_exists='append', index=False)  # write a DF into table3

        print("------------------- Writing into table2 -----------------------")

        write_query = 'UPDATE "public"."table2" SET "Active_flag" = 0 WHERE "RSS_Feed" = ' + "'" + link + "'"
        connection.execute(write_query)  # change flag in table2
        print("-----------Updated table2 and table3------------")


# Function to get news body from given news_url
def extract_news_body(news_url):
    response = get(news_url)
    extractor = Goose()
    article = extractor.extract(raw_html=response.content)
    body = article.cleaned_text
    # print(body)
    return body


# Function to get sentiment from given text
def get_sentiment(my_txt):
    # get the sentiment by calling detect_sentiment()  from AWS Comprehend Service
    # For AWS Comprehend Service, the maximum document size for sentiment analysis, targeted sentiment analysis,
    # syntax analysis, and the batch synchronous operations is 5 KB.
    text = my_txt
    if len(text) != 0:
        new_senti_str = ""
        if len(text) < 2000:
            response = client.detect_sentiment(Text=text, LanguageCode='en')                              # Lang_Code
            final_sentiment = response['Sentiment']
            return final_sentiment

        else:
            while len(text) >= 2000:
                response = client.detect_sentiment(Text=text[:2000], LanguageCode='en')
                new_senti_str += " " + response['Sentiment']
                text = text[2000:]              # take next chunk of text from 1000 onwards

            # Process the last chunk of text which is less than 1000
            response = client.detect_sentiment(Text=text, LanguageCode='en')
            new_senti_str += " " + response['Sentiment']

            # Process the  new_senti_str for getting final sentiment
            response = client.detect_sentiment(Text=new_senti_str, LanguageCode='en')
            final_sentiment = response['Sentiment']
            return final_sentiment


# Function to Parse the RSS_feed page
def get_news_details(rss_feed_url):
    print("Received URL: ", rss_feed_url)
    print("------Extracting details from it------")
    news_items = []
    cols = ['RSS_Feed', 'Title', 'Description', 'Body', 'RSS_Feed_URL', 'Publish_date', 'Sentiment', 'Inserted_on']
    html_text = get(rss_feed_url).text
    soup = BeautifulSoup(html_text, features="xml")
    items = soup.findAll('item')

    # scarring HTML tags such as Title, Description, Links and Publication date
    for x in items:
        news_item = {}
        news_item['RSS_Feed'] = rss_feed_url
        news_item['Title'] = x.title.text
        news_item['Description'] = x.description.text
        news_body = extract_news_body(x.link.text)
        news_item['Body'] = news_body
        news_item['RSS_Feed_URL'] = x.link.text
        news_item['Publish_date'] = x.pubDate.text
        news_item['Sentiment'] = get_sentiment(news_body)
        news_item['Inserted_on'] = datetime.now()

        news_items.append(news_item)

    # print(news_items)
    df2 = pd.DataFrame(news_items, columns=cols)
    tbl3_df = df2.drop_duplicates()
    return tbl3_df


# Driver Code
AWS_REGION = "ap-south-1"
session = boto3.Session(aws_access_key_id="AKIAQQOR2JV2JEVUGO4A",
                        aws_secret_access_key="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")
client = session.client('comprehend', region_name=AWS_REGION)

Engine = create_db_connection()
is_data = 0                 # flag for checking data is present or not

while 1:
    # 1) Read table2 single row to get feed_url
    feed_link = read_table2()
    print(feed_link)
    print(len(feed_link))
    if len(feed_link) != 0:
        is_data = 1
    else:
        is_data = 0

    while is_data == 1:
        print("---------Data is present, again read------------")

        # 2) extract news from feed_url
        Tbl3_df = get_news_details(feed_link)

        # 3) write the news Dataframe to table3 and make active_flag = 0 in table 2
        write_to_table2_3(Tbl3_df, feed_link)

    print("-----------------wait for 15 min--------------------")
    time.sleep(900)                                 # wait for 15 min = 900 sec
    print("-----------------completed wait period--------------------")

Engine.dispose()
