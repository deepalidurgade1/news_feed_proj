# Parse a feed url (single url)

# Process 2 : 1) Read table2 and extract the rss_feed_url
#             2) Open the URL and Parse it to extract details from it (link, news_title, description, pub_date etc.)
#             3) pass the "description" of news to comprehend for getting "Sentiment"
#             4) Save the extracted content as DF and write it into table3

import boto3
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, time
from sqlalchemy import create_engine

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
    with engine.connect() as connection:  # using "with" don't require closing of connection
        # query to read on condition
        read_query = 'SELECT "RSS_Feed" FROM "public"."table2" WHERE "Active_flag" = 2 LIMIT 1'
        result_set = connection.execute(read_query)
        print(result_set)  # gives "sqlalchemy.engine.cursor.LegacyCursorResult object"
        for res in result_set:
            link = list(res)  # the RSS_Feed is saved in a list
    print("-----------------------Reading table2 Successful------------------")
    return link


# Function to write into table3
def write_to_table2_3(df, link):
    print("------------------- Writing into table3 -----------------------")
    with engine.connect() as connection:  # using "with" don't require closing of connection
        # query to write into table
        df.to_sql('table3', con=connection, if_exists='replace', index=False)  # write a DF into table3

        print("------------------- Writing into table2 -----------------------")

        write_query = 'UPDATE "public"."table2" SET "Active_flag" = 0 WHERE "RSS_Feed" = ' + "'" + link + "'"
        connection.execute(write_query)  # change flag in table2
        print("-----------Updated table2 and table3------------")
    return


# Function to get sentiment from given text
def get_sentiment(my_txt):
    # Extract the language code of given text by calling detect_dominant_language() API
    # lang_response = client.detect_dominant_language(Text=my_txt)
    # lang_code = lang_response['Languages'][0]['LanguageCode']

    # get the sentiment by calling detect_sentiment() API
    # print("------------------Getting Sentiment----------------------")
    senti_response = client.detect_sentiment(
        Text=my_txt,
        LanguageCode='en'  # lang_code
    )
    return senti_response['Sentiment']


# Function to Parse the RSS_feed page
def get_news_details(RSS_feed_url):
    print("Received URL: ", RSS_feed_url)
    news_items = []
    html_text = requests.get(RSS_feed_url).text
    soup = BeautifulSoup(html_text, features="xml")
    items = soup.findAll('item')

    # scarring HTML tags such as Title, Description, Links and Publication date
    for x in items:
        news_item = {}
        news_item['RSS_Feed'] = RSS_feed_url
        news_item['Title'] = x.title.text
        news_item['Description'] = x.description.text
        news_item['Body'] = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
            has been the industry's standard dummy text ever since tshe 1500s, when an unknown printer took a galley of
            type and scrambled it to make a type specimen book. """
        news_item['RSS_Feed_URL'] = x.link.text
        news_item['Publish_date'] = x.pubDate.text
        news_item['Sentiment'] = get_sentiment(x.title.text)
        news_item['Inserted_on'] = datetime.now()

        news_items.append(news_item)

    # print(news_items)
    df2 = pd.DataFrame(news_items, columns=['RSS_Feed', 'Title', 'Description', 'Body', 'RSS_Feed_URL', 'Publish_date',
                                            'Sentiment', 'Inserted_on'])
    tbl3_df = df2.drop_duplicates()
    return tbl3_df


# Driver Code
AWS_REGION = "ap-south-1"
session = boto3.Session(aws_access_key_id="AKIAQQOR2JV2JEVUGO4A",
                        aws_secret_access_key="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")
client = session.client('comprehend', region_name=AWS_REGION)

engine = create_db_connection()

# while 1:
# 1) Read table2 single row to get feed_url
feed_link = read_table2()

# 2) extract news from feed_url
tbl3_df = get_news_details(feed_link[0])

# 3) write the news Dataframe to table3 and make active_flag = 0 in table 2
write_to_table2_3(tbl3_df, feed_link[0])

engine.dispose()
# time.sleep(900)                                # wait for 15 min = 900 sec
