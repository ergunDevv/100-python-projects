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
coin_values = {'penny': 0.01, 'nickel': 0.05, 'dime': 0.1, 'quarter': 0.25}
profit = 0
while True:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_type=='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

        continue
    if MENU[coffee_type]['ingredients']['water'] > resources['water']:
        print('Sorry there is not enough water.')
        continue
    elif MENU[coffee_type]['ingredients']['milk'] > resources['milk']:
        print('Sorry there is not enough milk.')
        continue
    elif MENU[coffee_type]['ingredients']['coffee'] > resources['coffee']:
        print('Sorry there is not enough coffee.')
        continue
    print('Please insert coins.')
    quarters = int(input("How many quarters?: "))*coin_values["quarter"]
    dimes = int(input("How many dimes?: "))*coin_values["dime"]
    nickels = int(input("How many nickels?: "))*coin_values["nickel"]
    pennies = int(input("How many pennies?: ")) * coin_values["penny"]
    profit += quarters+dimes+nickels+pennies
    if MENU[coffee_type]['cost'] > profit:
        print("Sorry that's not enough money. Money refunded.")
        profit -= quarters+dimes+nickels+pennies
        quarters=0
        dimes=0
        nickels=0
        pennies=0
        continue
    resources['water']-=MENU[coffee_type]['ingredients']['water']
    resources['milk']-=MENU[coffee_type]['ingredients']['milk']
    resources['coffee']-=MENU[coffee_type]['ingredients']['coffee']
    change =round(profit-MENU[coffee_type]['cost'], 2) 
    print(f"Here is ${change} in change.")
    print(f"Here is your {coffee_type} ☕️. Enjoy!")
    quarters=0
    dimes=0
    nickels=0
    pennies=0