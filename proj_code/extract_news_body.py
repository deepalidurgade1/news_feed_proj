# Extract news Body from given link of news (news Url from table3: RSS_Feed_URL) and get sentiment from it
from goose3 import Goose
from requests import get
import boto3

news_url = 'https://timesofindia.indiatimes.com/world/china/overwhelmed-with-bodies-' \
           'police-guard-beijing-crematorium-as-covid-deaths-rise-in-china/articleshow/96366841.cms'

AWS_REGION = "ap-south-1"

session = boto3.Session(aws_access_key_id="AKIAQQOR2JV2JEVUGO4A",
                        aws_secret_access_key="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")

client = session.client('comprehend', region_name=AWS_REGION)

# def extract_news_body(news_url):
#     response = get(news_url)
#     extractor = Goose()
#     article = extractor.extract(raw_html=response.content)
#     body = article.cleaned_text
#     print(body)
#     return body

Mytxt = 'BEIJING: Police and security guards were stationed outside a Beijing crematorium reportedly designated to ' \
         'handle Covid fatalities, as questions over China’s virus death toll mount.Guards pushed journalists to the ' \
         'back of the Beijing Dongjiao Funeral Parlor’s parking lot on Monday, as a line of about a dozen black ' \
         'minivans entered the site on Beijing’s eastern outskirts, used to prepare and process bodies for cremation.' \
         'The vans appeared to be dropping off bodies and were surrounded at one point by what seemed to be mourners ' \
         'or relatives.The crematorium has drawn scrutiny after workers told foreign media including the Financial ' \
         'Times and the Wall Street Journal that they were overwhelmed with bodies since China scrapped most Covid ' \
         'restrictions and Beijing experienced a surge in cases. That contrasts with the official virus death count, ' \
         'which saw just two Covid fatalities recorded for Beijing this weekend, the first in almost a ' \
         'month.Photographs taken earlier on Monday showed rows of cars — some adorned with ribbons often used ' \
         'in China to signify a vehicle is part of a funeral procession — entering Dongjiao, and employees in full ' \
         'PPE moving a coffin. The crematorium has been designated to handle Covid-positive cases and has been' \
         ' working around the clock, with about 200 bodies arriving daily, from 30 to 40 on a typical day, an ' \
         'employee told the Journal on Friday. Meanwhile, staff told the FT that the bodies of at least 30 Covid ' \
         'victims were cremated on Wednesday, when no fatalities were recorded for all of China, let alone Beijing. '\
         'The disparity comes as China embarks on a complete pivot away from its stringent Covid Zero policy, which ' \
         'has been dragging on the economy all year and stoking popular unrest. After painting Covid as a lethal ' \
         'threat the population needed to be protected from for most of the pandemic, officials are now saying it’s ' \
         'not dangerous, with one top adviser saying omicron could be likened to a “cold.”The inevitable rise in ' \
         'deaths that comes from reopening doesn’t fit with that messaging, especially with some experts predicting ' \
         'almost 1 million fatalities from this coming wave alone.Other countries that made a similar shift from ' \
         'containing Covid to living with it, like Singapore and New Zealand, saw much bigger increases in deaths' \
         ' when they reopened, and they had higher vaccination rates, especially among the elderly. China’s booster' \
         ' rate for those over 80 is just 40%.'

def get_sentiment(my_txt):
    # get the sentiment by calling detect_sentiment()  from AWS Comprehend Service
    # For AWS Comprehend Service, the maximum document size for sentiment analysis, targeted sentiment analysis,
    # syntax analysis, and the batch synchronous operations is 5 KB.
    text = my_txt
    new_senti_str = ""
    if len(text) < 1000:
        response = client.detect_sentiment(Text=text, LanguageCode='en')                              # Lang_Code
        final_sentiment = response['Sentiment']
        print("Sentiment: ", sentiment)
        return final_sentiment

    else:
        while len(text) >= 2000:
            response = client.detect_sentiment(Text=text[:2000], LanguageCode='en')
            new_senti_str += " " + response['Sentiment']
            print("1. ", new_senti_str)
            text = text[2000:]              # take next chunk of text from 1000 onwards

        print("last text chunk size: ", len(text))                    # print last chunk size
        # Process the last chunk of text which is less than 1000
        response = client.detect_sentiment(Text=text, LanguageCode='en')
        new_senti_str += " " + response['Sentiment']
        print("2.", new_senti_str)

        print(new_senti_str)
        final_sentiment = client.detect_sentiment(Text=new_senti_str, LanguageCode='en')
        return final_sentiment


# news_body = extract_news_body(news_url)
sentiment = get_sentiment(Mytxt)
# print(len(news_body))
print(sentiment)
