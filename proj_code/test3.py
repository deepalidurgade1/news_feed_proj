# # Extract Feeds from the given webpage
#
# from bs4 import BeautifulSoup
# import requests
# import feedparser
# import urllib.parse
#
# # Function to check if the link is feed-link or not
# def isFeedLink(link):
#     myList = ['/rss.cms', '/feed/', '/xml', 'feeds/posts/default', '.rss', '.cms']
#     if any(x in link for x in myList):
#         return True
#     elif link[-5:] == '/feed':
#         return True
#     else:
#         return False
#
#
# # Function to find the feed-link from a given url
# def find_feed(site):
#     page = requests.get(site).text
#     # result = []
#     possible_feeds = []
#     html = BeautifulSoup(page, 'html.parser')
#     # if site[-1] == '/':
#     #     site = site[:-1]
#     #     print("------", site)
#
#     for anchor in html.find_all('a'):
#         # print(anchor.get('href', '/'))
#         feed_urls = anchor.get('href', '/')
#         print(feed_urls)
#         # print("current urls = ", feed_urls)
#         if len(feed_urls) > 1:
#             flag = isFeedLink(feed_urls)
#             if flag:
#                 possible_feeds.append(feed_urls)
#     return possible_feeds
#
#
# # driver code Note : Don't give Backward slash at the end of a site
# site1 = 'https://timesofindia.indiatimes.com/'
# site1_rss = 'https://timesofindia.indiatimes.com/rss.cms'
# site2 = 'https://www.business-standard.com/'
# site2_rss = 'https://www.business-standard.com/rss-feeds/listing/'
# result = set(find_feed(site1_rss))
# print("Total Feeds: ", len(result))
# print(result)
#
# # # vgm_url = 'https://www.business-standard.com/rss/home_page_top_stories.rss'
# # vgm_url = result[0]
# # html_text = requests.get(vgm_url).text
# # soup = BeautifulSoup(html_text, features="xml")
# # items = soup.findAll('item')
# # print(items)
# # if items == []:
# #     next_res = find_feed(vgm_url)
# #
# # print("Total Feeds: ", len(next_res))
# # print(set(next_res))
#
#
# # news_item = {}
# # news_item['RSS_Feed'] = vgm_url
# # news_item['Title'] = items[0].title.text
# # news_item['Description'] = items[0].description.text
# # print(news_item)



# Extract all feeds from RSS feed List wepage
import requests
from bs4 import BeautifulSoup

feed_links = []
# Request
url = 'https://timesofindia.indiatimes.com/rss.cms'
r1 = requests.get(url)
r1.status_code

# We'll save in coverpage the cover page content
coverpage = r1.content

# Soup creation
soup1 = BeautifulSoup(coverpage, 'html.parser')         # 'html5lib')
# News identification  ## span class="rssp"
coverpage_news = soup1.find_all('span', class_='rssp')
for n in range(0, len(coverpage_news)):
    link = coverpage_news[n].find('a')['href']
    feed_links.append(link)

print(feed_links)
print(len(feed_links))
