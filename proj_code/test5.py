# # Test Connection with RDS Postgres SQL
#
# # -----------------------Using sqlalchemy----------------------------------
# from sqlalchemy import create_engine
# import pandas as pd
#
# # # conn_string = 'postgresql://<user>:<password>@<host>:<port>/<db>'
# conn_string = 'postgresql://postgres_admin:postgres123@postgres-db-identifier1.cxfegqfzlnwt.ap-south-1.' \
#               'rds.amazonaws.com:5432/db_news_feed'
#
# engine = create_engine(conn_string)               # forms a connection to the PostgreSQL database
#
# # with engine.connect() as connection:
# #     query = "SELECT * FROM table1"
# #     content = connection.execute(query)
# #     for row in content:
# #         print(" Row : ", row)
# #         print(" link : ", row[1])
# #         print(type(row))
#
#     #our dataframe
# # data = {'Name': ['Tom', 'dick', 'harry'],
# #         'Age': [22, 21, 24]}
#
# # Create DataFrame
# # df = pd.DataFrame(data)
# list2 = []
#
# with engine.connect() as connection:
#     # 1. query to read all contents
#     #     query = "SELECT * FROM table1"
#     #     content = connection.execute(query)
#     #     for row in content:
#     #         print(" Row : ", row)
#     #         print(" link : ", row[1])
#     #         print(type(row))
#
#     # 2. query to read on condition
#     # read_query = "select news_url, rss_list from table1 where active_flag = '1'"
#     # result_set = connection.execute(read_query)
#     # print(result_set)                                   # gives "sqlalchemy.engine.cursor.LegacyCursorResult object"
#     # for r in result_set:
#     #     l1.append(list(r))                               # the news news_url & rss_list is stored in a list
#     #
#     # print(l1)
#     # print(l1[0][1])
#
#     # 3.  write a DF into table
#     # df.to_sql('data', con=connection, if_exists='replace', index=False)
#
#     # 4. Read table2
#     # read_query = "SELECT 'RSS_Feed' FROM table2 where 'active_flag' = '2'"
#     # result_set = connection.execute(read_query)
#     # print(result_set)  # gives "sqlalchemy.engine.cursor.LegacyCursorResult object"
#     # for res in result_set:
#     #     list2.append(res)      # the news news_url & rss_list is stored in a list
#     # print(list2)
#
#     # 5. Write query with variable
#     link = 'http://timesofindia.indiatimes.com/rssfeeds/-2128838597.cms'
#     write_query = 'UPDATE "public"."table2" SET "Active_flag" = 11 WHERE "RSS_Feed" = ' + "'" + link + "'"
#     connection.execute(write_query)
#     # conn = psycopg2.connect(conn_string
#     #                         )
#     # conn.autocommit = True
#     # cursor = conn.cursor()
#     # sql1 = '''select * from data;'''
#     # cursor.execute(sql1)
#     # for i in cursor.fetchall():
#     #     print(i)
#     #
#     # # conn.commit()
#     # conn.close()
#
#
# # -----------------------Using psycopg2----------------------------------
# # import psycopg2
# #
# # hostname = "postgres-db-identifier1.cxfegqfzlnwt.ap-south-1.rds.amazonaws.com"
# # database = "db_news_feed"
# # username = "postgres_admin"
# # pwd = "postgres123"
# # port_id = "5432"
# #
# # conn=psycopg2.connect(
# #              host=hostname,
# #              dbname=database,
# #              user=username,
# #              password=pwd,
# #              port=port_id
# #              )
# #
# # cursor = conn.cursor()
# # res = cursor.execute("SELECT * FROM table2")
# # print(res)
# # conn.close()
#
#
#
# # link = 'http://timesofindia.indiatimes.com/rssfeeds/-2128838597.cms'
# # s1 = "'" + link + "'"
# # print(s1)

from datetime import datetime
import time


print(datetime.now())
time.sleep(10)
print(datetime.now())
