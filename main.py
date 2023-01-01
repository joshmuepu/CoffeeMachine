from menu import MENU, resources

money = 0
turn_on = True


def report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print(f"Money: ${money}")


def add_money(drink):
    global money
    money += MENU[drink]["cost"]


def check_money(drink):
    cost = MENU[drink]["cost"]
    print("Please, insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How may pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total < cost:
        print("Sorry, that's not enough money.")
    else:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change")
        make_drink(drink)


def make_espresso():
    if resources["water"] < 50:
        print("Sorry, there is not enough water")
    elif resources["coffee"] < 18:
        print("Sorry, there is not enough coffee")
    else:
        add_money("espresso")
        resources["water"] -= 50
        resources["coffee"] -= 18
        print("Here is your espresso. Enjoy")


def make_latte():
    if resources["water"] < 200:
        print("Sorry, there is not enough water")
    elif resources["coffee"] < 24:
        print("Sorry, there is not enough coffee")
    elif resources["milk"] < 150:
        print("Sorry, there is not enough coffee")
    else:
        add_money("latte")
        resources["water"] -= 200
        resources["coffee"] -= 24
        resources["milk"] -= 150
        print("Here is your latte. Enjoy")


def make_cappuccino():
    if resources["water"] < 250:
        print("Sorry, there is not enough water")
    elif resources["coffee"] < 24:
        print("Sorry, there is not enough coffee")
    elif resources["milk"] < 100:
        print("Sorry, there is not enough coffee")
    else:
        add_money("cappuccino")
        resources["water"] -= 250
        resources["coffee"] -= 24
        resources["milk"] -= 100
        print("Here is your cappuccino. Enjoy")


def make_drink(drink):
    if drink == "espresso":
        make_espresso()
    elif drink == "latte":
        make_latte()
    elif drink == "cappuccino":
        make_cappuccino()
    else:
        print("Wrong selection")


while turn_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "off":
        print("Good Bye!!")
        turn_on = False
    elif user_choice == "report":
        report()
    else:
        check_money(user_choice)


