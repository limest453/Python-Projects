import sys
total = 0
print("------Currency Converter-----------")

print("Select the currency you have: \n AED[1]\n KWD[2]\n GBP[3]\n USD[4]")
try:
    fro = int(input(""))
except:
    print("Please type an integer")
    sys.exit()
print("\nHow much of this currency?")
try:
    froAmount = float(input(""))
except:
    print("Please type a number")
    sys.exit()
print("\nSelect the currency you want to change to: \n AED[1]\n KWD[2]\n GBP[3]\n USD[4]")
try:
    to = int(input(""))
except:
    print("Please type an integer")
    sys.exit()


if fro == 1 and to == 1:
    print("\n\nSame currency")
if fro == 1 and to == 2:
    total = froAmount * 0.083
    print(total)
if fro == 1 and to == 3:
    total = froAmount * 0.2
    print(total)
if fro == 1 and to == 4:
    total = froAmount * 0.27
    print(total)

if fro == 2 and to == 1:
    total = froAmount * 12.02
    print(total)
if fro == 2 and to == 2:
    print("\n\nSame currency")
if fro == 2 and to == 3:
    total = froAmount * 2.42
    print(total)
if fro == 2 and to == 4:
    total = froAmount * 3.27
    print(total)

if fro == 3 and to == 1:
    total = froAmount * 4.96
    print(total)
if fro == 3 and to == 2:
    total = froAmount * 0.41
    print(total)
if fro == 3 and to == 3:
    print("\n\nSame currency")
if fro == 3 and to == 4:
    total = froAmount * 1.35
    print(total)

if fro == 4 and to == 1:
    total = froAmount * 3.67
    print(total)
if fro == 4 and to == 2:
    total = froAmount * 0.31
    print(total)
if fro == 4 and to == 3:
    total = froAmount * 0.74
    print(total)
if fro == 4 and to == 4:
    print("\n\nSame currency")


            


