import sys
import time

print("--------Number size-------\n")
time.sleep(1)

try:
    num = int(input("What is your number?\n"))
except:
    print("Please enter an integer")
    sys.exit()

if num < 100:
    print("Small")
elif num <= 130:
    print("Medium")
else:
    print("Large")
