import time
import random
print("Welcome to the Band Name Generator APP - Generate the perfect band name!\n")
time.sleep(1)
st = ["Old", "The", "Ultimately", "Super", "Rocky"]
adj = ["Rocking", "Cool", "Ultimate", "Legendary", "Unbelievable", "Shaking"]
noun = ["Musicians", "Monarchs", "Rocks", "Roads", "Stingrays", "Masters"]

beg  = random.randint(0,len(st)-1)
first  = random.randint(0,len(adj)-1)
second = random.randint(0,len(noun)-1)

print(len(st))

choice = random.randint(0, 2)

if choice == 2:
    final = adj[first] + " " + noun[second]
elif choice == 0 or 1:
    final = st[beg] + " " + adj[first] + " " + noun[second]
else:
    print("ERROR 101")


print(final)
time.sleep(0.2)
print(f"Get ready for you musical journey {final}!")

































