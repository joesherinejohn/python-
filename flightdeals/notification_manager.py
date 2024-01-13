import smtplib
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    # def __init__(self, flight_data, sheet_data):
    #     self.flight = flight_data
    #     self.sheet = sheet_data
    #     self.send_notification()

    def send_notification(self, emails,message):
        email_others = emails
        myemail =XXXX
        password =XXXX
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=myemail, password=password)
            connection.sendmail(from_addr=myemail,
                                to_addrs=email_others,
                                msg=(message.encode('utf-8')))
