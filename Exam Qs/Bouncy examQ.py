
while True:
    user = int(input("Enter a number greater than 0: "))
    if user > 0:
        break

check = str(user)
increasing = 0
decreasing = 0

for num in range(0, len(check)):
    if num > 0:
        if check[num] >= check[num-1]:
            increasing += 1
        elif check[num] <= check[num-1]:
            decreasing += 1
        
if increasing == 0 or decreasing == 0:
    print("The number is not bouncy")
elif increasing == decreasing and increasing != 0:
    print("The number is perfectly bouncy")
else:
    print("The number is bouncy")

    
