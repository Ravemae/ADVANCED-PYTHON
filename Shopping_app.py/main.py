from items import item
from app import ShoppingCart, save_balance, read_balance, record_transaction

# Example usage:
if __name__ == "__main__":
    teddy = item("Teddy", "Toy", 4, 5.20)
    sweet = item("Rolo", "Chocolate", 2, 2.42)

    cart = ShoppingCart()
    cart.add_item(teddy)
    cart.add_item(sweet)

    total_cost = cart.get_total_cost()
    print(f"Total cost: ${total_cost:.2f}")

    user_balance = read_balance()
    user_balance -= total_cost
    save_balance(user_balance)
    record_transaction(cart.items, total_cost)
    print(f"Updated balance: ${user_balance:.2f}")