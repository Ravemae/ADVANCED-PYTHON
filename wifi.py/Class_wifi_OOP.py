class WiFi:
    def __init__(self, name, network, password, type):
        self.name = name
        self.network = network
        self.password = password
        self.type = type

    # Write a function to create wifi according to the declared attribute
        

        
    def create_wifi(self):
        self.name = str(input("Enter the Wifi Name\n>> "))
        self.network = str(input("Enter Network\n>> "))
        self.password = str(input("Enter Wifi Password\n>> "))
        self.type = str(input("Enter Wifi type\n>> "))
        print(f"Wifi {self.name} has been Created")

    def connect(self):
        print("Do you want to connect\n(a.) Yes\n(b.) No")
        response = str(input(">> ")).upper()
        if response == "a" or response == "Yes":
            max_entry = 5
            entry = 0

            while entry <= max_entry:
                password = str(input("Enter wifi password\n>> "))
                if password != self.password:
                    print("Connection not Successful")
                    entry += 1
                else:
                    print("Connection Successful")
                    break  #Exit loop if connection is successful
            else:
                print("Maximum attempts reached. Connection failed.")
            
            
        elif response == "b" or response == "No":
            print("Ok... Enjoy The Rest Of Our Service")
        else:
            print("Invalid Request!")

        return "Connection Mode!!!"
    
class MTN(WiFi):
    def create(self):
        return f"You've created MTN wifi named {self.name}"

     
print("You can now create your wifi")

# print("Welcome,\nDo you want to;\n(1.) Create Wifi\n(2.) Connect to wifi")
# request = str(input(">> "))
# if request == "1" or request == " Create Wifi":
#     device = WiFi(name, network, password, type)
#     device.create_wifi()
# elif request == "2" or request == " Connect to Wifi":
#     device = WiFi(name, network, password, type)
#     device.connect()
# else:
#     print("Invalid Request")

MTN4GC1A58 = WiFi("Dont You Dare!", "MTN", "wertyut4", "MiFi")
MTN4GC1A58.connect()
    

        
