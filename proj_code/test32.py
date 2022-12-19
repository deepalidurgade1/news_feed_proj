#  Extract paragraph(body) from given URL

import requests
from bs4 import BeautifulSoup

feed_links = []
# Request
url = 'http://timesofindia.indiatimes.com/rssfeedstopstories.cms'
r2 = requests.get(url)
r2.status_code

# We'll save in coverpage the cover page content
coverpage = r2.content

# Soup creation
soup1 = BeautifulSoup(coverpage, 'xml')         # 'html5lib')
# News identification  ## span class="rssp"
coverpage_news = soup1.find_all('div', class_="_3YYSt clearfix")
# x = coverpage_news[0].get_text()
# y = coverpage_news[0]['href']

print(coverpage_news)
# print(y)


# # Empty lists for content, links and titles
# news_contents = []
# list_links = []
# list_titles = []
#
# for n in np.arange(0, number_of_articles):
#
#     # only news articles (there are also albums and other things)
#     if "inenglish" not in coverpage_news[n].find('a')['href']:
#         continue
#
#     # Getting the link of the article
#     link = coverpage_news[n].find('a')['href']
#     list_links.append(link)
#
#     # Getting the title
#     title = coverpage_news[n].find('a').get_text()
#     list_titles.append(title)
#
#     # Reading the content (it is divided in paragraphs)
#     article = requests.get(link)
#     article_content = article.content
#     soup_article = BeautifulSoup(article_content, 'html5lib')
#     body = soup_article.find_all('div', class_='articulo-cuerpo')
#     x = body[0].find_all('p')
#
#     # Unifying the paragraphs
#     list_paragraphs = []
#     for p in np.arange(0, len(x)):
#         paragraph = x[p].get_text()
#         list_paragraphs.append(paragraph)
#         final_article = " ".join(list_paragraphs)
#
#     news_contents.append(final_article)

article = requests.get("https://timesofindia.indiatimes.com/city/lucknow/up-bypoll-outcome-a-signal-ofcourse-correction"
                       "-for-parties/articleshow/96313747.cms")
article_content = article.content
soup_article = BeautifulSoup(article_content, 'xml')
body = soup_article.find_all("div", class_="clearfix rel")

# body_text = body.get_text("text")
print(body)
# print(body_text)
# x = body[0].find_all('p')
# # Unifying the paragraphs
# list_paragraphs = []
# for p in np.arange(0, len(x)):
#     paragraph = x[p].get_text()
#     list_paragraphs.append(paragraph)
#     final_article = " ".join(list_paragraphs)
# news_item['Body'] = final_article