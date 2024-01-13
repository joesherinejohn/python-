import requests
import os
from flight_data import FlightData
from notification_manager import NotificationManager
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.search_api_key = os.environ["SEARCH_API_KEY"]
        self.search_url ="https://api.tequila.kiwi.com/locations/query"
        self.two_way_key = os.environ["TWO_WAY_KEY"]
        self.twoway_url ="https://tequila-api.kiwi.com/v2/search"


    def update_IATA(self,city):
        self.body = {
            "term" : city,
            "location_types" : "city",
        }
        header ={
            "apikey": self.search_api_key
        }
        # response_search = requests.get(url=self.search_url,params=self.body, headers=header)
        # # print(response_search.json())
        # return (response_search.json()["locations"][0]["code"])
        if city == "Paris":
            return "PAR"
        elif city =="Denpasar":
            return "DPS"
        # return "Testing"

    def check_flights(self,from_loc, to_loc, from_date, to_date):
        head ={
            "apikey":self.two_way_key
        }
        query = {
            "fly_from": from_loc,
            "fly_to": to_loc,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response_check = requests.get(url=self.twoway_url,
                                      params=query,
                                      headers=head)
        print(response_check.json())


        try:
            data = response_check.json()["data"][0]
        except IndexError:
            query = {
                "fly_from": from_loc,
                "fly_to": to_loc,
                "date_from": from_date.strftime("%d/%m/%Y"),
                "date_to": to_date.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 2,
                # "via city":"Amsterdam",
                "curr": "GBP"
            }
            count = 1
            response_check = requests.get(url=self.twoway_url,
                                          params=query,
                                          headers=head)
            print(response_check.json())
            data = response_check.json()["data"][0]
        else:
            count = 0
            # print(f"No flights found for {to_loc}")
            # return None

        if count == 1:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                via_city = data["route"][0]["cityFrom"],
                stop_over = 1,
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][3]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}:£{flight_data.price}")
            return flight_data
        else:
            flight_data= FlightData(
                price = data["price"],
                origin_city = data["route"][0]["cityFrom"],
                origin_airport = data["route"][0]["flyFrom"],
                via_city= "None",
                stop_over= 0,
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}:£{flight_data.price}" )
            return flight_data
