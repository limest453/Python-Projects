import time
name = input ("Hello, welcome to TESTER 5000. Can you please tell me your name?\n")
print("Hello " + name + ", nice to meet you!")
time.sleep(1)
age = float (input ("How old are you " + name + "? (in numbers)\n"))
time.sleep(1)
if age > 18 and age < 90:
    print("Oh, " + age + " is a bit too old to answer this test, "+ name + ".")
if age > 90:
    print("Really?! You can't be here at "+ age + "!")
if age < 18:
    print(f"Oh wow, {name}, {age} is the perfect age for this test.")
subject = input ("What is the subject your testing for, " + name + "? \n")
print ("Ok! You choice is: " + subject + ".\n")
time.sleep(1)
clas = input ("What's your class?\n")
print("Recorded.")
time.sleep(1)
year = input ("What year are you in (write the number)\n")
time.sleep(1)
print ("So, you're in year " + year + " and in " + clas + "! Recorded.") 
