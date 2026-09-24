import time
print("Welcome to the Online Restaurant Calculator - solve all the payment disputes!\n\n")
time.sleep(1.2)

people = int(input("How many people are going to pay?\n"))
print("\n")
amount = float(input("What is the total cost of the bill in AED? (Only include the number)\n"))
print("\n")

total = amount / people
print(f"So with {people} people and the total cost of the bill being {amount} AED,")
print(f"Each of the {people} people have to pay {total:.2f} AED!")
