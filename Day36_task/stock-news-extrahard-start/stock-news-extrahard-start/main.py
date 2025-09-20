import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

api_key = os.environ.get("STOCK_MARKET_API_KEY")
news_api_key = os.environ.get("news_api")
print(news_api_key)
stock_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key,

}
news_parameter ={
    "q": COMPANY_NAME,
    "language": "en",
    "domains": "bloomberg.com",
    "searchln": "title",
    "apiKey": news_api_key,
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock = requests.get(url="https://www.alphavantage.co/query", params=stock_parameter)
stock_data = stock.json()

news = requests.get(url="https://newsapi.org/v2/everything", params=news_parameter)
print(news.json())

last_trading_day = list(stock_data["Time Series (Daily)"])[0]
day_before = list(stock_data["Time Series (Daily)"])[1]

last_day_closing = float(stock_data["Time Series (Daily)"][last_trading_day]["4. close"])
day_before_closing = float(stock_data["Time Series (Daily)"][day_before]["4. close"])
change_in_price = (last_day_closing-day_before_closing)/last_day_closing

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if -0.05 >= change_in_price >= 0.05:
    pass
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

