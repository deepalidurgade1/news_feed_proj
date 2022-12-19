import boto3

def get_sentiment(my_txt):
    # Extract the language code of given text by calling detect_dominant_language() API
    lang_response = client.detect_dominant_language(
        Text=my_txt
    )

    Lang_Code = lang_response['Languages'][0]['LanguageCode']

    # get the sentiment by calling detect_sentiment() API
    senti_response = client.detect_sentiment(
        Text=my_txt,
        LanguageCode=Lang_Code
    )

    return senti_response['Sentiment']


AWS_REGION = "ap-south-1"

session = boto3.Session(aws_access_key_id="AKIAQQOR2JV2JEVUGO4A",
                        aws_secret_access_key="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")

client = session.client('comprehend', region_name=AWS_REGION)

my_txt = "This place is extremely cost saving but the owner is very rude :("
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



