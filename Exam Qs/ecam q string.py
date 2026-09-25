loop = True
while loop:
    user = input("Enter a string: ")
    total = 0
    up = user.upper()
    asc = False
    unique = True

    for char in user:
        total += ord(char)

    if 420 <= total <= 600:
        asc = True

    for i in range(len(user) - 1):
        if user[i] == user[i + 1]:
            unique = False
            break

    if (5 <= len(user) <= 7 and up.strip() == user.strip() and unique and asc):
        print("Done")
        loop = False
        
