from data import MENU, stock_available


def order_price(order):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total_amount = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total_amount


def update_stock(order):
    ingredients_needed = MENU[order]["ingredients"]
    for ingredient, quantity in ingredients_needed.items():
        stock_available[ingredient] -= quantity


def make_coffee(order, amount=0):
    if order in ["espresso", "latte", "cappuccino"]:
        order_cost = MENU[order]["cost"]
        ingredients_needed = MENU[order]["ingredients"]

        insufficient_ingredients = [ingredient for ingredient, quantity in ingredients_needed.items() if
                                    stock_available[ingredient] < quantity]
        if not insufficient_ingredients:
            total_amount = amount + order_price(order)

            if total_amount >= order_cost:
                change = total_amount - order_cost
                print(f"Total amount received: ${total_amount:.2f}")
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {order}. Enjoy!")

                # Update stock
                update_stock(order)
                stock_available["money"] += order_cost
            else:
                shortage = order_cost - total_amount
                print(f"You are short of ${shortage:.2f}.")
                insert_more = input("Would you like to insert more coins? (yes/no): ").lower()
                if insert_more == "yes":
                    make_coffee(order, total_amount)  # Recursive call to ask for more coins
                else:
                    print("Order canceled.")
        else:
            print(f"Sorry, there is not enough {', '.join(insufficient_ingredients)}.")
            # You can notify the admin or take appropriate action here
    elif order == "report":
        print("Report")
        print(f"Water: {stock_available['water']}ml\n"
              f"Milk: {stock_available['milk']}ml\n"
              f"Coffee: {stock_available['coffee']}g\n"
              f"Money: ${stock_available['money']:.2f}\n")
    elif order == "off":
        print("Switch off")
    else:
        print("Wrong command")


while True:
    order_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order_type == "off":
        break
    make_coffee(order_type)
    print(stock_available)