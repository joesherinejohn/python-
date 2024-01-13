import requests
from bs4 import BeautifulSoup
import smtplib

myemail= "XXXXX"
password = "XXXXX"

URL = "url for the product"
header = {
    "user-agent" :"XXXX",
  "Accept-Language":"en-US,en;q=0.9"
}

response = requests.get(url=URL,headers=header)
# print(response.text)
html_website = response.text

soup = BeautifulSoup(html_website,"html.parser")
value = soup.find(name='span', class_= 'aok-offscreen').getText()
# print(value)
value = (value.replace("$","")).strip()
# print()
if float(value) < 130.00:
	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(user=myemail, password=password)
		connection.sendmail(from_addr=myemail,
							to_addrs=myemail,
							msg=f"Subject:Alert,Price is low\n\n Hello, The instapot price has reduced . Please check the website")
	
