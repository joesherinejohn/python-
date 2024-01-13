
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
from pprint import pprint
import datetime as dt

data_sheet = DataManager()
sheet_data = data_sheet.get_sheet()
# pprint(sheet_data)
print(sheet_data)

flight_search = FlightSearch()
for data in sheet_data:
    if  not data["iataCode"]:
        update_iata = flight_search.update_IATA(data["city"])
        data["iataCode"]= update_iata

pprint(sheet_data)
# data_sheet.put_self(sheet_data)

from_date = dt.datetime.now()+ dt.timedelta(1)
to_date  = dt.datetime.now()+dt.timedelta(180)
# print(from_date,to_date)
# # print(from_date.strftime("%d/%m/%Y"))
# # print(to_date.strftime("%d/%m/%Y"))
for data in sheet_data:
    flight_data = flight_search.check_flights("LON",
                                to_loc=data["iataCode"],
                                from_date = from_date,
                                to_date=to_date)
    # print(flight_data.destination_city)
    # print(flight_data.price)
    # print(flight_data.price, data["lowestPrice"])
    if data["city"] == flight_data.destination_city:
        if data["lowestPrice"] >= flight_data.price:
                # print(f"Notify{flight_data.destination_city}")
            notify =NotificationManager()
            if flight_data.stop_over == 0:
                message =f"Subject: Alert for ticket booking\n\n Low Price Alert! Only £{flight_data.price} to fly from London-LON to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}"
            elif flight_data.stop_over == 1:
                message =(f"Subject: Alert for ticket booking\n\n Low Price Alert! Only £{flight_data.price} to fly from London-LON to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}\n"
                              f"Flight has {flight_data.stop_over}stop over , via {flight_data.via_city} city.")
            print(message)
            # users_data = data_sheet.users_data()
            # for data in users_data:
            #     emails = data["email"]
            #     print(message)
                # notify.send_notification(emails, message)
           
