Train_1 = ("Dhaka Express" , "Dhaka" , "Khulna" , 500)
Train_2 = ("Rajsahi Express" , "Rajsahi" , "Dhaka" , 600)
Train_3 = ("Chittagong Express" , "Chittagong" , "Rajsahi" , 800)

Trains = [Train_1 , Train_2 , Train_3]

print("Available Trains -")
for item in Trains:
    print(f"{item[0]} | {item[1]} -> {item[2]} | {item[3]}")

choice = int(input("Select Your Train(1/2/3): "))

selected_train = Trains[choice-1]

num_ticket = int(input("Enter How Many Tickets You Want: "))
total_Price = num_ticket * selected_train[3]

Booking = {
    "Train Name": selected_train[0],
    "From": selected_train[1],
    "To": selected_train[2],
    "Number of Passenger": num_ticket,
    "Total Price": total_Price
}
for key , value in Booking.items():
    print(f"{key}- {value}")


    