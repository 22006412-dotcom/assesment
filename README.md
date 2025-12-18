this is my  code for sliting  bills and solve the problasm a groub of people have when they  have a big amount of bill and they want to slpit the billls btween them 
 i have created a function 
created a function: split_bill
def split_bill(total_amount, people, tip). 
This function:
Takes three parameters:
total_amount → the bill amount
people → number of people sharing the bill
tip → tip amount. 
 Inside the function
a) Decision (if / else)
if tip > 0:  total_amount = total_amount + tipelse:  total_amount = total_amount
If the tip is greater than 0, you add the tip to the total bill.
If the tip is 0 or less, the total stays the same.
(Note: the else part isn’t really needed, because doing nothing would give the same result.)
b) Calculation
each_person = total_amount / people
 i have  divide the final bill by the number of people to find how much each person should pay.
c) Return valuereturn each_person
The function sends back the amount each person must pay.
2.  if i want want to use it is easy just you have yo  collect people’s names using a loop
names = []
num_people = int(input("Enter number of people: "))You create an empty list called names.
You  just ask the user how many people are splitting the bill.
for i in range(num_people):
  name = input("Enter name: ")
  names append(name)
This loop runs once for each person. very basic but super usefull 
Each time, you:
Ask for a name
Store it in the names list
3. You take bill and tip input
bill = float(input("Enter total bill amount: "))
tip = float(input("Enter tip amount (0 if none): "))
You ask the user for:
Total bill amount
Tip amount
You convert both inputs to numbers (float) so calculations can be done.
4. You call the function
amount_each = split_bill(bill, num_people, tip)
You send the bill, number of people, and tip to the split_bill function.
The function calculates the share per person and stores it in amount_each.
5. You display the result
print("\nBill Split Result:")
Prints a heading.
for name in names:print(name, "pays:", round(amount_each, 2))
Loops through each name in the names list.
Prints:
The person’s name
The amount they need to pay
round(amount_each, 2) rounds the amount to 2 decimal places, like real money.
 In simple words
Your program:
Asks how many people are splitting a bill
Collects their names
Takes the bill amount and tip
Adds the tip to the bill (if any)
Splits the total equally
Displays how much each person has to pay
This is a great example of using:
Functions
Parameters & return values
Loops
Lists
User input
Conditionals
If you want, I can also:
Simplify the code
Improve it
Add error handling
