def display_inventory(inventory):
    """Print each inventory item and the total value of all stock."""
    total_value = 0

    print("Inventory:")
    for item, details in inventory.items():
        quantity = details["quantity"]
        price = details["price"]
        print(f"{item}: quantity = {quantity}, price = ${price:.2f}")
        total_value += quantity * price

    print(f"Total inventory value: ${total_value:.2f}")


if __name__ == "__main__":
    inventory = {
        "Notebook": {"quantity": 20, "price": 2.50},
        "Pen": {"quantity": 50, "price": 1.20},
        "Backpack": {"quantity": 8, "price": 25.00},
    }

    display_inventory(inventory)