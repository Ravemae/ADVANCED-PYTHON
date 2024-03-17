import random as r

def usr_acc_num():
    random_integers = ''.join(str(r.randint(0, 9)) for _ in range(10))
    return random_integers

print("Welcome, what would you like to do")
print("1. Open Account\n2. Transfer\n3. Airtime\n4. Internet\n5. Balance\n6. BILLS & Utilities") 
res = str(input())

if res == "1":
    firstname = str(input("Your Firstname\n>> ")).upper()
    lastname = str(input("Your Lastname\n>> ")).upper()
    other_name = str(input("Your Other_name\n>> ")).upper()
    email = str(input("Your email\n>> ")).upper()
    number = str(input("Your Phone Number\n>> ")).upper()
    address = str(input("Your Address\n>> ")).upper()
    dob = str(input("Your date of birth\n>> "))
    account_number = usr_acc_num()
           
print(f"Dear {firstname} {lastname} {other_name}, Your Regisration was Successful.\n Your Account Number is{account_number}\nThanks for joining the family")

if res == "2":
    bank = str(input("Select Bank Name\n>>")).upper
    firstname = str(input("Your Firstname\n>> ")).upper()
    lastname = str(input("Your Lastname\n>> ")).upper()