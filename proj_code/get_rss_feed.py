import requests
from bs4 import BeautifulSoup


def get_rss_feed(website_url):
    if website_url is None:
        print("URL should not be null")
    else:
        source_code = requests.get(website_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        # print(soup)
        for link in soup.find_all("a", attrs={'class': 'main-cont-left topB'}):
            href = link.get('href')
            print(len(href))
            # href = link.get('href')
            print(href)


get_rss_feed('https://www.business-standard.com/rss-feeds/listing/')



