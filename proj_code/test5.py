# Test Connection with RDS Postgres SQL

# -----------------------Using sqlalchemy----------------------------------
from sqlalchemy import create_engine
import pandas as pd

# # conn_string = 'postgresql://<user>:<password>@<host>:<port>/<db>'
conn_string = 'postgresql://postgres_admin:postgres123@postgres-db-identifier1.cxfegqfzlnwt.ap-south-1.' \
              'rds.amazonaws.com:5432/db_news_feed'

engine = create_engine(conn_string)               # forms a connection to the PostgreSQL database

# with engine.connect() as connection:
#     query = "SELECT * FROM table1"
#     content = connection.execute(query)
#     for row in content:
#         print(" Row : ", row)
#         print(" link : ", row[1])
#         print(type(row))

    #our dataframe
data = {'Name': ['Tom', 'dick', 'harry'],
        'Age': [22, 21, 24]}

# Create DataFrame
df = pd.DataFrame(data)

with engine.connect() as connection:
    #     query = "SELECT * FROM table1"
    #     content = connection.execute(query)
    #     for row in content:
    #         print(" Row : ", row)
    #         print(" link : ", row[1])
    #         print(type(row))
    df.to_sql('data', con=connection, if_exists='replace',
              index=False)
    # conn = psycopg2.connect(conn_string
    #                         )
    # conn.autocommit = True
    # cursor = conn.cursor()
    # sql1 = '''select * from data;'''
    # cursor.execute(sql1)
    # for i in cursor.fetchall():
    #     print(i)
    #
    # # conn.commit()
    # conn.close()


# -----------------------Using psycopg2----------------------------------
# import psycopg2
#
# hostname = "postgres-db-identifier1.cxfegqfzlnwt.ap-south-1.rds.amazonaws.com"
# database = "db_news_feed"
# username = "postgres_admin"
# pwd = "postgres123"
# port_id = "5432"
#
# conn=psycopg2.connect(
#              host=hostname,
#              dbname=database,
#              user=username,
#              password=pwd,
#              port=port_id
#              )
#
# cursor = conn.cursor()
# res = cursor.execute("SELECT * FROM table2")
# print(res)
# conn.close()
