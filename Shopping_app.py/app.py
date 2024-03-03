class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_total_cost(self):
        total = sum(item.price for item in self.items)
        return total

    def reset(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

def save_balance(balance):
    with open("balance.txt", "w") as balance_file:
        balance_file.write(str(balance))

def read_balance():
    try:
        with open("balance.txt", "r") as balance_file:
            return float(balance_file.read())
    except FileNotFoundError:
        return 0.0

def record_transaction(item, price):
    with open("transactions.txt", "a") as transactions_file:
        transactions_file.write(f"{item} sold for ${price:.2f}\n")
