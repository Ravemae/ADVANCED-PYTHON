class WiFi:
    def __init__(self, name="", network="", password="", type=""):
        self.name = name
        self.network = network
        self.password = password
        self.type = type

    # Write a function to create wifi according to the declared attribute

    def create_wifi(self):
        print("You can now create your wifi")
        self.name = str(input("Enter the Wifi Name\n>> "))
        self.network = str(input("Enter Network\n>> "))
        self.password = str(input("Enter Wifi Password\n>> "))
        self.type = str(input("Enter Wifi type\n>> "))
        print(f"Your Wifi {self.name} has been Created")

    def connect(self):
        print("Do you want to connect?")
        response = input("(a.) Yes\n(b.) No\n>> ").lower()
        if response == "a" or response == "Yes":
                password = str(input("Enter wifi password\n>> "))
                if password == self.password:
                    print("Connection Successful")
                else:
                    print("Connection not Successful")
        elif response == "b" or response == "No":
            print("Ok... Enjoy The Rest Of Our Service")
        else:
            print("Invalid Request!")

        return "Connection Mode!!!" 

 # Main Program
if __name__ == "__main__":
    print("Welcome!")
    print("Do you want to:")
    print("(1.) Create Wifi\n(2.) Connect to wifi")
    request = input(">> ")

    if request == "1" or request.lower() == "create wifi":
        device = WiFi()
        device.create_wifi()
    elif request == "2" or request.lower() == "connect to wifi":
        device = WiFi()
        device.connect()
    else:
        print("Invalid Request")


MTN4GC1A58 = WiFi("Dont You Dare!", "MTN", "wertyut4", "MiFi")
MTN4GC1A58.connect()
    
