import  requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY_STOCK_PRICE = "XXXX"
STOCK_PRICE_URL = "https://www.alphavantage.co/query"


parameters_stock_price = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey":API_KEY_STOCK_PRICE,
    "outputsize":"compact"
}

# STEP 1: Use https://www.alphavantage.co
response_price = requests.get(url=STOCK_PRICE_URL,params=parameters_stock_price)
response_price.raise_for_status()
print(response_price.status_code)
data_price_daily = response_price.json()
print(data_price_daily["Time Series (Daily)"])

today_date = dt.datetime.now()
if today_date.isoweekday() == 7:
    yesterday = dt.datetime.now() - dt.timedelta(2)
    daybeforeyesterday = dt.datetime.now() - dt.timedelta(3)
elif today_date.isoweekday() == 1:
    yesterday = dt.datetime.now() - dt.timedelta(3)
    daybeforeyesterday = dt.datetime.now() - dt.timedelta(4)
else:
    yesterday = dt.datetime.now() - dt.timedelta(1)
    daybeforeyesterday = dt.datetime.now() - dt.timedelta(2)

print(today_date.date(),yesterday.date(),daybeforeyesterday.date())
date_yes = str(yesterday.date())
date_daybefore = str(daybeforeyesterday.date())
# # get the closing price
final_val = float(data_price_daily["Time Series (Daily)"][date_yes]["4. close"])
start_val =float( data_price_daily["Time Series (Daily)"][date_daybefore]["4. close"])
# start_val = 220
# calculate the  difference in percentage
per_cal = ((final_val - start_val)/start_val) * 100
print(f"{per_cal}")
if int(per_cal) < -2:
    print(f"Decreases by {(int(per_cal))*(-1)}%")
elif int(per_cal) >2:
    print(f"Great News, increases by {int(per_cal)}%")



## STEP 2: Use https://newsapi.org
API_KEY_STOCK_NEWS=XXXX
STOCK_NEWS_URL = "https://newsapi.org/v2/everything"

parameters_stock_news = {
    "q":"tesla",
    "from":date_yes,
    "apikey":API_KEY_STOCK_NEWS

}


response_2 = requests.get(url=STOCK_NEWS_URL, params=parameters_stock_news)
response_2.raise_for_status()
data_news = response_2.json()
print(data_news["articles"])
print(data_news["articles"][0]["title"])
print(data_news["articles"][0]["description"])
print(data_news["articles"][1]["title"])
print(data_news["articles"][1]["description"])
print(data_news["articles"][2]["title"])
print(data_news["articles"][2]["description"])

## send email
# import smtplib
# myemail = XXXX
# password = XXXX
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=myemail, password=password)
#     connection.sendmail(from_addr=myemail,
#                         to_addrs=myemail,
#                         msg="Greatnews")
