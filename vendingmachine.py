# Vending Machine code for Assessment 2

print("""
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▀▄▀█ ▄▀█ █▀█ █ █▀█ █▄░█ █▄░█ █▀▀ ▀ █▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █░▀░█ █▀█ █▀▄ █ █▄█ █░▀█ █░▀█ ██▄ ░ ▄█

          █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
          ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄
""")

# Inventory dictionary
Inventory = {
  "Chips": {
        "A1": {"item": "Lays", "Price": 5.00, "stock": 10},
        "A2": {"item": "Doritos", "Price": 2.00, "stock": 10},
        "A3": {"item": "Nachos", "Price": 4.00, "stock": 10},
        "A4": {"item": "Chips Oman", "Price": 2.00, "stock": 10},
        "A5": {"item": "Finnish", "Price": 2.00, "stock": 10},
        "A6": {"item": "Popcorn", "Price": 3.00, "stock": 10},
        "A7": {"item": "Bugles",  "Price": 5.00, "stock": 10}
    },
    "Candy": {
        "B1": {"item": "Snickers", "Price": 5.00, "stock": 10},
        "B2": {"item": "Barebells", "Price": 15.00, "stock": 10},
        "B3": {"item": "Twix", "Price": 5.00, "stock": 10},
        "B4": {"item": "KitKat", "Price": 5.00, "stock": 10},
        "B5": {"item": "Bueno", "Price": 5.00, "stock": 10},
        "B6": {"item": "Oreo Cake", "Price": 3.00, "stock": 10},
        "B7": {"item": "Bounty", "Price": 5.00, "stock": 10},
    },
    "Biscuits": {
        "C1": {"item": "Oreo", "Price": 4.00, "stock": 10},
        "C2": {"item": "Prime Nuts", "Price": 5.00, "stock": 10},
        "C3": {"item": "Loacker", "Price": 5.00, "stock": 10},
        "C4": {"item": "Ginger Nuts", "Price": 3.00, "stock": 10},
        "C5": {"item": "Emil", "Price": 3.00, "stock": 10},
        "C6": {"item": "Ritz", "Price": 3.00, "stock": 10},
        "C7": {"item": "Lotus Biscoff", "Price": 3.00, "stock": 10},
    },  # ← FIXED: added comma here
    "Drinks": {
        "D1": {"item": "Coke", "Price": 3.00, "stock": 10},
        "D2": {"item": "Nescafe", "Price": 7.00, "stock": 10},
        "D3": {"item": "Water", "Price": 2.00, "stock": 10},
        "D4": {"item": "Juice", "Price": 5.00, "stock": 10},
        "D5": {"item": "Energy Drink", "Price": 12.00, "stock": 10},
        "D6": {"item": "Mountain Dew", "Price": 3.00, "stock": 10},
        "D7": {"item": "Fanta", "Price": 3.00, "stock": 10}
    },

    "Water": {
        "E1": {"item": "Water", "Price": 2.00, "stock": 10},
        "E2": {"item": "Water", "Price": 2.00, "stock": 10},
        "E3": {"item": "Water", "Price": 2.00, "stock": 10},
        "E4": {"item": "Water", "Price": 2.00, "stock": 10},
        "E5": {"item": "Water", "Price": 2.00, "stock": 10},
        "E6": {"item": "Water", "Price": 2.00, "stock": 10},
        "E7": {"item": "Water", "Price": 2.00, "stock": 10},
    }
}


# Display menu
def display_menu():
    print("\n-*- Vending Machine Menu -*-")
    for category, items in Inventory.items():
        print(f"\nCategory: {category}")
        print(f"{'Code':<6}{'Item':<20}{'Price':<15}{'Stock':<6}")
        print("-" * 50)
        for code, details in items.items():
            print(f"{code:<6}{details['item']:<20}AED {details['Price']:<10.2f}{details['stock']:<6}")

# Validate code
def validate_code_inventory(code):
    for category, items in Inventory.items():
        if code in items:
            return True, category
    return False, None

# Get product code
def get_product_code():
    while True:
        code = input("Enter product code (or EXIT): ").upper()
        if code == "EXIT":
            return None, None
        valid, category = validate_code_inventory(code)
        if valid:
            return code, category
        print("Invalid code. Try again.")

# Process stock
def process_stock(code):
    for items in Inventory.values():
        if code in items:
            if items[code]['stock'] > 0:
                items[code]['stock'] -= 1
                return items[code]
            else:
                print("Item out of stock.")
                return None
    return None

# Payment
def process_payment(total_price):
    while True:
        try:
            amount = float(input(f"Insert money (AED {total_price:.2f}): "))
            if amount >= total_price:
                return amount - total_price
            else:
                print("Not enough money.")
        except:
            print("Invalid input.")

# Suggest pairing
def suggest_pairing(category):
    pairings = {
        "Chips": "Drinks",
        "Candy": "Chips",
        "Biscuits": "Drinks",
        "Drinks": "Chips"
    }

    paired_category = pairings.get(category)
    if not paired_category:
        return {}

    print(f"\nSuggested from {paired_category}:")
    for code, item in Inventory[paired_category].items():
        print(f"{code}: {item['item']} - AED {item['Price']:.2f}")

    return Inventory[paired_category]

# Receipt
def print_receipt(items):
    print("\n--- Receipt ---")
    total = 0
    for item in items:
        print(f"{item['item']} - AED {item['Price']:.2f}")
        total += item['Price']
    print(f"Total: AED {total:.2f}")
    print("Thank you!")

# Main program
def vending_machine():
    display_menu()
    cart = []

    code, category = get_product_code()
    if not code:
        return

    item = process_stock(code)
    if item:
        print(f"{item['item']} added.")
        total = item['Price']
        cart.append(item)

        pairings = suggest_pairing(category)
        if pairings:
            choice = input("Add pairing? (y/n): ").lower()
            if choice == 'y':
                pcode = input("Enter pairing code: ").upper()
                if pcode in pairings:
                    pitem = process_stock(pcode)
                    if pitem:
                        cart.append(pitem)
                        total += pitem['Price']

        change = process_payment(total)
        print(f"Change: AED {change:.2f}")
        print_receipt(cart)

# Run program
if __name__ == "__main__":
    vending_machine()
