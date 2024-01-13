import requests
from requests.auth import HTTPBasicAuth
import os

class DataManager:
	def __init__(self):
	    self.SHEET_USERNAME = os.environ["AUTH_SHEETY_USERNAME"]
	    self.SHEET_PASSWORD = os.environ["AUTH_SHEETY_PASSWORD"]
	    self.SHEET_URL = "XXXX"

	def get_sheet(self):
            list_sheet = []
            list_sheet.append({"city":"Paris",
                               "iataCode":"",
                               "lowestPrice":60})
            list_sheet.append({"city": "Denpasar",
                               "iataCode": "",
                               "lowestPrice": 900})
            return list_sheet


	def put_self(self, sheet_data):
		for data in sheet_data:
			body ={
				"price":{
					"iataCode":data["iataCode"]
				}
			}

