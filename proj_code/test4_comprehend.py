import boto3

def get_sentiment(my_txt):
    # Extract the language code of given text by calling detect_dominant_language() API
    # lang_response = client.detect_dominant_language(
    #     Text=my_txt
    # )
    #
    # Lang_Code = lang_response['Languages'][0]['LanguageCode']

    # get the sentiment by calling detect_sentiment() API

    senti_response = client.detect_sentiment(
        Text=my_txt,
        LanguageCode='en'                               #Lang_Code
    )

AWS_REGION = "ap-south-1"

session = boto3.Session(aws_access_key_id="AKIAQQOR2JV2JEVUGO4A",
                        aws_secret_access_key="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")

client = session.client('comprehend', region_name=AWS_REGION)

# my_txt = "A seven-year-old boy having his lunch collapsed on his plate and died after he was hit by a bullet fired " \
#          "accidentally from an illegal firearm his elder brother had found and was playing with in a farmhouse in " \
#          "Kadushivanahalli village, near Kanakapura in Ramanagara district, on Friday."

# my_txt = "A seven-year-old boy having his lunch collapsed on his plate and died after he was hit by a bullet fired "

# my_txt = "GGuards pushed journalists to the back of the Beijing Dongjiao Funeral Parlor’s parking lot on Monday, " \
#          "as a line of about a dozen black minivans entered the site on Beijing’s eastern outskirts, " \
#          "used to prepare and process bodies for cremation."

my_txt = "'Overwhelmed with bodies': Cops guard Beijing crematorium as Covid deaths rise in China"
print(get_sentiment(my_txt))

# resource = session.resource("s3", region_name=AWS_REGION)                             # specify domain for s3 bucket
#
# bucket_name = "news-sentiment-analysis-bucket"
# location = {'LocationConstraint': AWS_REGION}
#
# bucket = resource.create_bucket(
#     Bucket=bucket_name,
#     CreateBucketConfiguration=location)
#
# print("Amazon S3 bucket has been created")



# response = client.detect_sentiment(
#     Text=my_txt,
#     LanguageCode='en'
# )
#
# # get the response
# print(response['Sentiment'])
