class item:
    def __init__(self, name, description, quantity, price):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
class Shop:
    def __init__(self, name, brand, quantity, price):
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.price = price
        
        
    def sell(self):
        print(f"You've purchased {self.quantity} {self.name} for {self.price}")
    
    def buy(self):
        pass
    
# class Dealer(Shop):
  
  

#     if
    
print("Welcome to JUVEC SUPERMARKET😊\nWe are always at your door step!😊")