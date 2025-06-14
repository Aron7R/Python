PhoneBook = {}

def AddContact(name,phone):
    PhoneBook[name] = phone
    print(f"{name}-{phone} Added Successfully!")

def RemoveContact(name):
    del PhoneBook[name]
    print(f"{name} Removed Succesfully!")

def UpdateContact(name,phone):
    PhoneBook[name] = phone
    print(f"{name} Updates Succesfully!")

def ViewBook():
    for key,value in PhoneBook.items():
        print(f"{key}-{value}")


while True:
    print("Welcome to PhoneBook.\n1.Add Contact\n2.Delete Contact\n3.Update Contact\n4.View Contact\n5.Exit")
    choice = int(input("Enter Your Choice(1,2,3,4,5): "))
    
    if choice == 1:
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        AddContact(name, phone)
    elif choice == 2:
        name = input("Enter Name: ")
        RemoveContact(name)
    
    elif choice == 3:
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        UpdateContact(name, phone)
    
    elif choice == 4:
        ViewBook()
    
    elif choice == 5:
        break
    
    else:
        print("Invalid Entry")

