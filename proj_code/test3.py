from bs4 import BeautifulSoup
import requests
import feedparser
import urllib.parse


def isFeedLink(link):
    myList = ['/rss', '/feed', '/xml']
    if any(x in link for x in myList):
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

    for anchor in html.find_all('a'):
        # print(anchor.get('href', '/'))
        feed_urls = anchor.get('href', '/')
        # print("current urls = ", feed_urls)
        if len(feed_urls) > 1:
            flag = isFeedLink(feed_urls)
            print(flag)
            if flag == True :
                print("Found a match")
                possible_feeds.append(feed_urls)
    return possible_feeds
    # parsed_url = urllib.parse.urlparse(site)
    # base = parsed_url.scheme+"://"+parsed_url.hostname
    # atags = html.findAll("a")
    # for a in atags:
    #     href = a.get("href", None)
    #     if href:
    #         if "xml" in href or "rss" in href or "feed" in href:
    #             possible_feeds.append(base+href)
    # for url in list(set(possible_feeds)):
    #     f = feedparser.parse(url)
    #     if len(f.entries) > 0:
    #         if url not in result:
    #             result.append(url)
    # return(result)
    #

# driver code
site1 = 'https://timesofindia.indiatimes.com/'
result = find_feed(site1)
print(result)

