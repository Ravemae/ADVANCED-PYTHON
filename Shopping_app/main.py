class Shop:
    def __init__(self, name, brand, quantity):
        self.name = name
        self.brand = brand
        self.quantity = quantity

        # Write a function to sell and buy goods 
    def sell(self):
        print("Welcome to JUVEC SUPERMARKET😊\nWe are always at your door step!😊")
        print("We Sell Varities Ranging From Povisions, Confectionaries, Drinks, Kids toys,Cosmetics To Household Items")
        print(f"Right now we sell only {self.brand}, and we have {self.quantity}")
        
    def buy(self):
        amt = int(input("How many are you buying "))
        print(f"I want to buy {amt} {self.brand}")
        rem = self.quantity - amt
        print(f"We now have {rem} {self.name} left")
        
class Mall(Shop):
    print("Done!!!!!")
        
pepsi = Shop("Joyce drinks", "Pepsi", 20)
print()
pepsi.sell()
pepsi.buy()


