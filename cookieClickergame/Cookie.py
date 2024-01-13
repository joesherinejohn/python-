from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# click on the cookie as soon as possible
cookie = driver.find_element(By.ID, value="cookie")

all_items= driver.find_elements(By.CSS_SELECTOR, value="#store div")
all_items_id = [items.get_attribute("id") for items in all_items]

# print(all_items_id)
dict_cost = {}
for n in  all_items_id:
	dict_cost[n] = 0
print(dict_cost)
start = time.time()
time_check = start + 5
five_mins = start + (60*5)

while True:
	cookie.click()
	if time.time() > time_check:
		for key in  dict_cost:
			# print(key)
			get_cost = driver.find_element(By.ID, value=f"{key}")
			# print(get_cost.text)
			if get_cost.text != "":
				new_cost = (get_cost.text.split("\n")[0].split("-")[1].strip()).replace(",","")
			# new_cost =(get_cost.text).split("-")[1].strip()
			# 	print(new_cost)
				dict_cost[key] = int(new_cost)
			# print(dict_cost)
		current_count = driver.find_element(By.ID, value="money").text
		# print(current_count.text)
		if "," in current_count:
			current_count = current_count.replace(",","")
		current_count_int = int(current_count)
			
		affordable_dict = {}
		for id, cost in dict_cost.items():
			if current_count_int >cost and cost != 0:
				affordable_dict[cost] = id
			# print( id, cost)
		# print(current_count_int,affordable_dict)
		highest = max(affordable_dict)
		# print(highest)
		to_buy_id = affordable_dict[highest]
		get =  driver.find_element(By.ID, value=to_buy_id).click()
		time_check = time.time() + 5
		
	if time.time() > five_mins:
		cookiepersec = driver.find_element(By.ID, value="cps")
		print(f"Cookies/second : {cookiepersec.text}")
		driver.quit()
		break
		
