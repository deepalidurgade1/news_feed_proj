import boto3

def get_sentiment(txt):
    # Extract the language code of given text by calling detect_dominant_language() API
    # lang_response = client.detect_dominant_language(
    #     Text=my_txt
    # )
    #
    # Lang_Code = lang_response['Languages'][0]['LanguageCode']

    # get the sentiment by calling detect_sentiment() API

    senti_response = client.detect_sentiment(
        Text=txt,
        LanguageCode='en'                               # Lang_Code
    )
    return senti_response['Sentiment']


AWS_REGION = "ap-south-1"

session = boto3.Session(aws_access_key_id="AKIAQQOR2JV2JEVUGO4A",
                        aws_secret_access_key="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")

client = session.client('comprehend', region_name=AWS_REGION)

my_txt = "COVID pandemic is not over yet! With COVID cases exploding in China, other countries are ramping up their " \
         "testing requirements, and will likely start imposing travel restrictions in the coming days. Here, we have " \
         "carefully listed those countries that are witnessing a sudden rise in COVID cases, and it is best advised " \
         "that you avoid travelling to these destinations as of now."

print(get_sentiment(my_txt))