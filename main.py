from menu import MENU, resources

money = 0
turn_on = True


def report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print(f"Money: ${money}")


def make_espresso():
    if resources["water"] < 50:
        print("Sorry, there is not enough water")
    elif resources["coffee"] < 18:
        print("Sorry, there is not enough coffee")
    else:
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
        resources["water"] -= 250
        resources["coffee"] -= 24
        resources["milk"] -= 100
        print("Here is your cappuccino. Enjoy")


while turn_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "report":
        report()
    elif user_choice == "espresso":
        make_espresso()
        money += 1.5
    elif user_choice == "latte":
        make_latte()
        money += 2.5
    elif user_choice == "cappuccino":
        make_cappuccino()
        money += 3.0
    elif user_choice == "off":
        print("Good Bye!!")
        turn_on = False
    else:
        print("Wrong selection.")
        turn_on = False




