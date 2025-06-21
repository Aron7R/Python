members = [{"Name":"Aron" , "ID" : 123},
           {"Name":"Pariza" , "ID" : 321},
           {"Name":"Vivek" , "ID" : 213}]

books = [{"Title":"The Chronicles of Narnia" , "Author" : "C.S Lewis"},
        {"Title":"The Diary of a Wimpy Kid" , "Author" : "Jeff Kinny"},
        {"Title":"Charlie and the Chocolate Factory" , "Author" : "Roald Dahl"}] 

print("Welcome to National Library of Bangladesh")
print("Please Enter Your ID / Click 0 to Create One")
id = int(input("Enter Your ID: "))

if id == 0:
    name = input("Enter Your Name: ")
    id = int(input("Enter Your Unique ID: "))
    members.append({"Name": name , "ID":id})

for item in members :
    if item["ID"] == id:
        print("Welsome ", item["Name"])
        break

print("Available Books")
print("----------------")
for book in books:
    print(f"{book["Title"]} - {book["Author"]}")
