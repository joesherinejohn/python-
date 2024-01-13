MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def get_coins():
    print("Please insert coins")
    coins_quaters = int(input("How many quaters?: "))
    coins_dime = int(input("How many dime?: "))
    coins_nickels =int(input("How many nickels?: "))
    coins_pennies = int(input("How many pennies?: "))
    total_cost = (0.25 * coins_quaters) + (0.10 * coins_dime) +(0.05 * coins_nickels) +(0.01 * coins_pennies)
    return round(total_cost, 2)




rotate = True
left_resources = resources
left_resources["money"] = 0.0
while  rotate == True:
    option = input ("What would you like? (espresso/latte/cappuccino): ").lower()
    if option == "report":
        print("Water:" , left_resources["water"])
        print("Milk:", left_resources["milk"])
        print("Coffee:", left_resources["coffee"])
        print("Money:", left_resources["money"])
    elif option == "espresso":
       if left_resources["water"] <= 0 or left_resources["coffee"]<=0:
           print("Sorry there is not enough ingredients to make coffee")
       else:
           cost =  get_coins()
           if cost < float(MENU[option]["cost"]):
               print ("Sorry that's not enough money. Money refunded.")
               continue
           else:
               water = left_resources["water"] - MENU[option]["ingredients"]["water"]
               coffee = left_resources["coffee"] - MENU[option]["ingredients"]["coffee"]
               if water < 0:
                    print("Sorry there is not enough water.")
                    print(f"Your money {cost} is refunded")
               elif coffee < 0:
                   print("Sorry there is not enough coffee.")
                   print(f"Your money {cost} is refunded")
               else:
                  left_resources["water"] = left_resources["water"] - MENU[option]["ingredients"]["water"]
                  left_resources["coffee"] = left_resources["coffee"] - MENU[option]["ingredients"]["coffee"]
                  remain_money = round(cost - float(MENU[option]["cost"]), 2)
                  print(f"Here is ${remain_money} in change. ")
                  left_resources["money"] += MENU[option]["cost"]
                  print(f"Here is your {option} . Enjoy :) ")

    elif option== "latte":
        if left_resources["water"] <= 0 or left_resources["milk"] <= 0 or left_resources["coffee"] <= 0:
            print("Sorry there is not enough ingredients to make coffee")
        else:
            cost = get_coins()
            if cost < float(MENU[option]["cost"]):
                print("Sorry that's not enough money. Money refunded.")
                continue
            else:
                water = left_resources["water"] - MENU[option]["ingredients"]["water"]
                milk = left_resources["milk"] - MENU[option]["ingredients"]["milk"]
                coffee = left_resources["coffee"] - MENU[option]["ingredients"]["coffee"]
                if water < 0:
                    print("Sorry there is not enough water.")
                    print(f"Your money {cost} is refunded")
                elif milk < 0:
                    print("Sorry there is not enough milk.")
                    print(f"Your money {cost} is refunded")
                elif coffee < 0:
                    print("Sorry there is not enough coffee.")
                    print(f"Your money {cost} is refunded")
                else:
                    left_resources["water"] = left_resources["water"] - MENU[option]["ingredients"]["water"]
                    left_resources["milk"] = left_resources["milk"] - MENU[option]["ingredients"]["milk"]
                    left_resources["coffee"] = left_resources["coffee"] - MENU[option]["ingredients"]["coffee"]
                    remain_money = round(cost - float(MENU[option]["cost"]), 2)
                    print(f"Here is ${remain_money} in change. ")
                    left_resources["money"] += MENU[option]["cost"]
                    print(f"Here is your {option} . Enjoy :) ")
    elif option=="cappuccino":
        if left_resources["water"] <= 0 or left_resources["milk"] <= 0 or left_resources["coffee"] <= 0:
            print("Sorry there is not enough ingredients to make coffee")
        else:
            cost = get_coins()
            if cost < float(MENU[option]["cost"]):
                print("Sorry that's not enough money. Money refunded.")
                continue
            else:
                water = left_resources["water"] - MENU[option]["ingredients"]["water"]
                milk = left_resources["milk"] - MENU[option]["ingredients"]["milk"]
                coffee = left_resources["coffee"] - MENU[option]["ingredients"]["coffee"]
                if water < 0:
                    print("Sorry there is not enough water.")
                    print(f"Your money {cost} is refunded")
                elif milk < 0:
                    print("Sorry there is not enough milk.")
                    print(f"Your money {cost} is refunded")
                elif coffee < 0:
                    print("Sorry there is not enough coffee.")
                    print(f"Your money {cost} is refunded")
                else:
                    left_resources["water"] = left_resources["water"] - MENU[option]["ingredients"]["water"]
                    left_resources["milk"] = left_resources["milk"] - MENU[option]["ingredients"]["milk"]
                    left_resources["coffee"] = left_resources["coffee"] - MENU[option]["ingredients"]["coffee"]
                    remain_money = round(cost - float(MENU[option]["cost"]), 2)
                    print(f"Here is ${remain_money} in change. ")
                    left_resources["money"] += MENU[option]["cost"]
                    print(f"Here is your {option} . Enjoy :) ")
    elif option=="nothing":
        rotate = False
        print("Thank you for using this coffee machine")
    else:
        print("Please enter a valid input.")

