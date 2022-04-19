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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#TOD0: TODO 1 : print choice
#TODO: #TODO 2 : machine on and machine off using is_on function and while function
#check the resorces then serve the coffee
def is_resources_sufficient(order_ingredients):
    """Returns true when the order can be made , False if ingredents is insufficient"""
    is_enough = True
    for item in order_ingredients:
       if order_ingredients[item] >= resources[item]:
        print(f"sorry there is not a enough water{item}")
        is_enough = False
       return is_enough
#american dollar coin base transaction
def process_coin():
    """"Returns the totat calculated when the coin is inserted """
    print("please insert the coint")
    total = int(input("how many quaters")) *0.25
    total = int(input("how many dimes")) * 0.1
    total = int(input("how many nickles")) * 0.05
    total = int(input("how many pennys")) * 0.01
    return  total
#mtransaction function
def is_transaction_succesful(money_Recieve,drink_cost):
    """Return True when the payement is accepted or , False if money is insufficient"""
    if money_Recieve >= drink_cost:
        global profit
        change = round(money_Recieve- drink_cost, 2)
        print(f"here is many dollars to{change} change")
        return True
    else:
        print("sorry thats the you dont have enough moneey")
        return  False
#coffe  making ingredent and resources function
def make_coffe(drink,order_ingredients):
    """Deduct the requred ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"here is your {drink}drink")
#machin ON and OFF code
is_on = True
while is_on:
    choice = input("What would you like espresso/latte/cappuccino:")
    if choice == "off":
        is_on = False
    elif choice =="report":
     print(f"water:{resources['water']}ml")
     print(f"milk:{resources['milk']}ml")
     print(f"coffee:{resources['coffee']}gm")
     print(f"money:{profit}$")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
          payment = process_coin()
        if is_transaction_succesful(payment,drink["cost"]):
            make_coffe(choice,drink["ingredients"])
