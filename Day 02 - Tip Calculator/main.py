#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print(f"Welcome to the tip calculator! 👋\n{'*'*35}")
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))


total_bill = bill * ((tip/100) + 1)
bill_per_person = total_bill / people

print("*"*35)
print(f"Each person should pay: $ {bill_per_person:.2f}")