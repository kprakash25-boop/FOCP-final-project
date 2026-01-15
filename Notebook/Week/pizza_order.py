import sys
import datetime

# ---------------------------------------------------
# Check command line argument
# ---------------------------------------------------
if len(sys.argv) != 2:
    print("Usage: python pizza_order.py orders.txt")
    exit()

filename = sys.argv[1]

# ---------------------------------------------------
# Functions
# ---------------------------------------------------

def get_valid_price(number):
    """
    Ask the user for a pizza price.
    Keep asking until a valid number greater than 0 is entered.
    """
    while True:
        try:
            value = float(input(f"Enter Price of Pizza #{number}: "))
            if value <= 0:
                print("Please enter a valid price!")
            else:
                return value
        except:
            print("Please enter a valid price!")


def calculate_offer(prices):
    """
    Apply the 4-for-3 offer.
    The cheapest pizza is free.
    """
    total = sum(prices)
    cheapest = min(prices)
    final_total = total - cheapest
    discount_percent = (cheapest / total) * 100
    return cheapest, final_total, discount_percent


def save_order(prices, cheapest, final_total, discount):
    """
    Save the order to the file given in the command line.
    """
    with open(filename, "a") as file:
        file.write("New Order\n")
        file.write(f"Date: {datetime.datetime.now()}\n")
        file.write(f"Prices: {prices}\n")
        file.write(f"Free pizza: £{cheapest:.2f}\n")
        file.write(f"Total to pay: £{final_total:.2f}\n")
        file.write(f"Discount: {discount:.2f}%\n")
        file.write("-" * 40 + "\n")


def show_orders():
    """
    Display all saved orders.
    """
    try:
        with open(filename, "r") as file:
            print("\n--- Order History ---")
            print(file.read())
    except:
        print("No previous orders found.")


def show_statistics():
    """
    Show total orders, total revenue and average order value.
    """
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        totals = []

        for line in lines:
            if "Total to pay" in line:
                amount = float(line.split("£")[1])
                totals.append(amount)

        if len(totals) > 0:
            print("\n--- Statistics ---")
            print("Total orders:", len(totals))
            print("Total revenue: £", round(sum(totals), 2))
            print("Average order: £", round(sum(totals) / len(totals), 2))
        else:
            print("No orders yet.")

    except:
        print("No statistics available.")


def show_menu():
    """
    Display the main menu.
    """
    print("\nBeckett Pizza Plaza")
    print("=" * 30)
    print("1. New Order")
    print("2. View Orders")
    print("3. View Statistics")
    print("4. Exit")


# ---------------------------------------------------
# Main Program
# ---------------------------------------------------
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        prices = []

        print("\nEnter prices for 4 pizzas")

        for i in range(1, 5):
            price = get_valid_price(i)
            prices.append(price)

        cheapest, final_total, discount = calculate_offer(prices)

        print("\nOrder Summary")
        print("Pizza prices:", prices)
        print("Free pizza: £", round(cheapest, 2))
        print("Total to pay: £", round(final_total, 2))
        print("Discount:", round(discount, 2), "%")

        save_order(prices, cheapest, final_total, discount)
        print("Order saved.")

    elif choice == "2":
        show_orders()

    elif choice == "3":
        show_statistics()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")