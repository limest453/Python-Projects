user = input("Enter a string: ")

vow = "aeiou"
vowl = []

for i in user:
    if i in vow:
        vowl.append(i)

vowl.reverse()

result = ""
index = 0

for x in user:
    if x in vow:
        result += vowl[index]
        index += 1
    else:
        result += x


print(result)
