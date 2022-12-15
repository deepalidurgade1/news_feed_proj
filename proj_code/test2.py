# from trafilatura import feeds
# mylist = feeds.find_feed_urls('https://www.business-standard.com/')
# print(len(mylist))

# import requests
# from bs4 import BeautifulSoup
#
# page = requests.get('https://timesofindia.indiatimes.com/').text
# # print(page.status_code)
# # soup = BeautifulSoup(page, "lxml")
# soup = BeautifulSoup(page, 'html.parser')
# # div = soup.find('p')
# # ethereum_rate = div.contents
# #
# # print(ethereum_rate)
# print(soup)

# code from wikipedia

# from bs4 import BeautifulSoup
# from urllib.request import urlopen, Request
#
# req = Request(
#     url='https://timesofindia.indiatimes.com/',
#     headers={'User-Agent': 'Mozilla/5.0'}
# )
# with urlopen(req) as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.find_all('a'):
#         print(anchor.get('href', '/'))


# code from "https://alex.miller.im/posts/python-3-feedfinder-rss-detection-from-url/"

from bs4 import BeautifulSoup
import requests
import feedparser
import urllib.parse

def findfeed(site):
    page = requests.get('https://timesofindia.indiatimes.com/').text
    result = []
    possible_feeds = []
    html = BeautifulSoup(page, 'html.parser')

    for anchor in html.find_all('a'):
        # print(anchor.get('href', '/'))
        feed_urls = anchor.get('href', '/')
        print(feed_urls)
    if len(feed_urls) > 1:
        for f in feed_urls:
            t = f.get("type", None)
            # print(t)
            if t:
                if "rss" in t or "xml" in t:
                    href = f.get("href", None)
                    if href:
                        possible_feeds.append(href)
    parsed_url = urllib.parse.urlparse(site)
    base = parsed_url.scheme+"://"+parsed_url.hostname
    atags = html.findAll("a")
    for a in atags:
        href = a.get("href", None)
        if href:
            if "xml" in href or "rss" in href or "feed" in href:
                possible_feeds.append(base+href)
    for url in list(set(possible_feeds)):
        f = feedparser.parse(url)
        if len(f.entries) > 0:
            if url not in result:
                result.append(url)
    return(result)


# driver code
site1 = 'https://timesofindia.indiatimes.com/'
result1 = findfeed(site1)
print(result1)
