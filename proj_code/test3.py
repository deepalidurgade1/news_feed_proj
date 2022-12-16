from bs4 import BeautifulSoup
import requests
import feedparser
import urllib.parse


def isFeedLink(link):
    myList = ['/rss.cms', '/feed/', '/xml', 'feeds/posts/default', '.rss']
    if any(x in link for x in myList):
        return True
    elif link[-5:] == '/feed':
        return True
    else:
        return False
#
# str1 = 'https://timesofindia.indiatimes.com/rss.cms'
# isFeedLink(str1)

def find_feed(site):
    page = requests.get(site).text
    # result = []
    possible_feeds = []
    html = BeautifulSoup(page, 'html.parser')
    if site[-1] == '/':
        site = site[:-1]
        print("------", site)

    for anchor in html.find_all('a'):
        # print(anchor.get('href', '/'))
        feed_urls = anchor.get('href', '/')
        # print("current urls = ", feed_urls)
        if len(feed_urls) > 1:
            flag = isFeedLink(feed_urls)
            if flag == True:
                if site in feed_urls:
                    possible_feeds.append(feed_urls)
                else:
                    feed_urls = site + feed_urls
                    possible_feeds.append(feed_urls)
    return possible_feeds

# driver code Note : Don't give Backward slash at the end of a site
site1 = 'https://timesofindia.indiatimes.com/'
site2 = 'https://www.business-standard.com/'
site3 = 'https://www.business-standard.com/rss-feeds/listing/'
result = find_feed(site3)
print("Total Feeds: ", len(result))
print(result)

# vgm_url = 'https://www.business-standard.com/rss/home_page_top_stories.rss'
vgm_url = result[0]
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, features="xml")
items = soup.findAll('item')
print(items)
# if items == []:
#     next_res = find_feed(vgm_url)
#
# print("Total Feeds: ", len(next_res))
# print(set(next_res))


# news_item = {}
# news_item['RSS_Feed'] = vgm_url
# news_item['Title'] = items[0].title.text
# news_item['Description'] = items[0].description.text
# print(news_item)

