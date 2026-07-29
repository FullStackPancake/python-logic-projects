print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? $"))
people = int(input("How many people to split the bill? "))

print(f"total bill: {bill}")
print(f"tip: {tip}")
print(f"people: {people}")

total_bill = bill * (tip / 100) + bill
bill_for_person = total_bill / people

print(f"Each person should pay: {bill_for_person}")
