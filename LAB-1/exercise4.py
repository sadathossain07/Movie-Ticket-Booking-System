name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))

fare_table = ["1. Dhaka - 465",
            "2. Rongpur - 860",
            "3. Sylhet - 650",
            "4. Rajshahi - 400"]
passenger_types = ["1. Adult", 
                 "2. Child", 
                 "3. Student",
                 "4. Senior"]

print("Destinations:")
for i in fare_table:
    print(i)

chosen_destination = int(input("Select a destination (1-4): "))

if chosen_destination == 1:
    destination = "Dhaka"
    fare = 465
elif chosen_destination == 2:
    destination = "Rongpur"
    fare = 860
elif chosen_destination == 3:
    destination = "Sylhet"
    fare = 650
elif chosen_destination == 4:
    destination = "Rajshahi"
    fare = 400
else:
    print("Invalid destination")


ticket_number = int(input("Enter ticket number: "))

print("Passenger Types:")
for i in passenger_types:
    print(i)

passenger_type = int(input("Select passenger type (1-4): "))

if passenger_type == 1:
    passenger_type = "Adult"
    discount = 0
elif passenger_type == 2:
    passenger_type = "Child"
    discount = 60
elif passenger_type == 3:
    passenger_type = "Student"
    discount = 40
elif passenger_type == 4:
    passenger_type = "Senior"
    discount = 20
else:
    print("Invalid passenger type")


total = fare * ticket_number
discount_amount = total * discount / 100
final_fare = total - discount_amount


print("\n--- Ticket Information ---")
print(f"Passenger: {name}")
print(f"Age: {age}")

print(f"Destination: {destination}")

print(f"Passenger Type: {passenger_type}")

print(f"Number of Tickets: {ticket_number}")

print(f"Fare per Ticket: {fare} Tk")
print(f"Total Fare: {total} Tk")
print(f"Discount: {discount} %")

print(f"Discount Amount: {discount_amount} Tk")
print(f"Grand Total Fare: {final_fare} Tk")