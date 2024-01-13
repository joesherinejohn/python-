import requests
from  datetime import datetime
import smtplib


MY_LAT = XXX
MY_LNG = XXX
FORMAT = 0

myemail = XXXX
password = XXXX

parameters ={
    "lat": MY_LAT,
    "lng":MY_LNG,
    "formatted":FORMAT
}


def check_position():
    response_1 = requests.get(url= "http://api.open-notify.org/iss-now.json")
    response_1.raise_for_status() # this command will raise the exception for unsuccessful error code
    data_1 = response_1.json()
    iss_lat = float(data_1["iss_position"]["latitude"])
    iss_long = float(data_1["iss_position"]["longitude"])
    if (MY_LAT-5 <= iss_lat <= MY_LAT+5) and (MY_LNG-5 <= iss_long <= MY_LNG+5):
        return True


def is_night():
    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    # print(response.json())
    sunrise_hour = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour =int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])


    time_now = datetime.now()
    currenthour = time_now.hour
    if currenthour >= sunset_hour or currenthour <=sunrise_hour:
        return True



# if the iss is close to my current position and
while True:
    if check_position() and is_night() is True:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=myemail,password=password)
            connection.sendmail(from_addr= myemail,
                                to_addrs=myemail,
                                msg="Subject:ISS_Position\n\nThe iss_position is near to your latitude and longitude")


