# Beckett Pizza Plaza 4-for-3 Offer Program

def get_valid_price(pizza_number):
    """Prompt the user to enter a valid price for a pizza."""
    while True:
        try:
            price = float(input(f"Enter Price of Pizza #{pizza_number}: "))
            if price <= 0:
                print("Please enter a valid price!")
            else:
                return price
        except ValueError:
            print("Please enter a valid price!")

# Welcome message
print("Beckett Pizza Plaza 4-for-3 Offer")
print("=================================")

# Get prices for 4 pizzas
prices = []
for i in range(1, 5):
    price = get_valid_price(i)
    prices.append(price)

# Calculate total and discount
cheapest = min(prices)  # Free pizza
total_paid = sum(prices) - cheapest
discount = (cheapest / sum(prices)) * 100

# Display results
print(f"\nOrder Total is £{total_paid:.2f}, a fabulous discount of {discount:.0f}%!")