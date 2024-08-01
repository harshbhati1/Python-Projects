import datetime
import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# setting up dates
message1 = ""
date1 = datetime.date.today() - datetime.timedelta(days=1) # change it afterwards
date2 = datetime.date.today() - datetime.timedelta(days=2)
day1 = date1.weekday()
day2 = date2.weekday()
print(date1)
print(date2)
if day1!=5 and day2!=5 and day1!=6 and day2!=6:
    
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": os.getenv('apikey')
    }

    response = requests.get("https://www.alphavantage.co/query", params=parameters )
    response.raise_for_status()

    data = response.json()["Time Series (Daily)"]
    day1Close = float(data[str(date1)]["4. close"])
    day2Close = float(data[str(date2)]["4. close"])
    percentage = ((day1Close - day2Close)/day2Close)*100
    
    if (percentage > 0):
        message1 += f"{STOCK}:🔺{round(percentage,2)}%"
    else:
        message1 += f"{STOCK}:🔻{round(percentage,2)}%"


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    API_KEY = os.getenv('API_KEY')
    NEWS_API_URL = 'https://newsapi.org/v2/everything'

    params = {
        'q': 'Tesla OR TSLA',
        'language': 'en',
        'sortBy': 'publishedAt', 
        'apiKey': API_KEY,
        'pageSize': 3 
    }

    response = requests.get(NEWS_API_URL, params=params)
    response.raise_for_status()
    data = response.json()["articles"]
    
    for articles in data:
        message1+= f"\n Headline: {articles["title"]}"
        message1+= f"\n Brief: {articles["description"]}"
        message1+= f"\n URL: {articles["url"]} \n"



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

    account_sid = os.getenv('TWILIO_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=f'whatsapp:{os.getenv('TWILIO_WHATSAPP_NUMBER1')}',
        body=message1,
        to=f'whatsapp:{os.getenv('TWILIO_WHATSAPP_NUMBER')}'
    )
    print(f"Message SID: {message.sid}")
    print(f"Message Status: {message.status}")
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

