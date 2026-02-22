units = int(input("Enter units consumed: "))
senior = input("Is senior citizen? (yes/no): ")

solar = input("Has solar panel? (yes/no): ")

payment = input("is Payment mode offline: (yes or no)")


if units <= 100:
    bill = units * 3
elif units <= 300:
    bill = (100 * 3) + (units - 100) * 5
else:
    bill = (100 * 3) + (200 * 5) + (units - 300) * 8

if (senior == "yes"):
    bill = bill * 0.90

if solar == "yes" :
    if units <= 250:
        bill -= 500
    else:
        bill -= 300

if payment == "yes" :
    if bill < 1000:
        bill += 50
    else:
        bill += 100

if bill < 200:
    bill = 200

print("Electricity Bill is rs: ", bill)



