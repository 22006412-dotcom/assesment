# Custom function with parameters and return value
def split_bill(total_amount, people, tip):
    # selection (if / else)
    if tip > 0:
        total_amount = total_amount + tip
    else:
        total_amount = total_amount

    # calculation
    each_person = total_amount / people

    return each_person  # returned value


# loop to enter names
names = []
num_people = int(input("Enter number of people: "))

for i in range(num_people):  # loop
    name = input("Enter name: ")
    names.append(name)

# inputs
bill = float(input("Enter total bill amount: "))
tip = float(input("Enter tip amount (0 if none): "))

# function call
amount_each = split_bill(bill, num_people, tip)

# output
print("\nBill Split Result:")
for name in names:  # loop
    print(name, "pays:", round(amount_each, 2)) 
  
