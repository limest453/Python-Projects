#Imports
from turtle import *

#Function - Pixel
def pixel(length,color):
    pendown()
    pencolor(color)
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(length)
        right(90)
    end_fill()
    penup()

#Function - create
def create():
    while True:
        try:
            name = input("Enter the file name: ").strip()
            columns = int(input("Enter the number of columns: "))
            rows = int(input("Enter the number of rows: "))
            length = int(input("Enter the pixel length: "))
            break
        except ValueError:
            print("Please enter a number")

    print("\n")
    reset()  
    width(1)
    speed(6)
    hideturtle()
    setup(500,500)

    penup()
    f = open(f"{name}.txt","w")
    
    f.write(f"{columns}\n")
    f.write(f"{rows}\n")
    f.write(f"{length}\n")
    
    for i in range(rows):
        for x in range(columns):
            pcolor = input("Pixel Color: ").strip()
            
            f.write(f"{pcolor}\n")
            pixel(length,pcolor)
            forward(length)
        backward(length * columns)
        right(90)
        forward(length)
        left(90)
    f.close()

def load():
    name = input("\nEnter the file name which you would like to load: ").strip()
    while True:
        try:
            f = open(f"{name}.txt","r")
            break
        except:
            print("There is no file of that name. Please try again.")
            load()

    columns = int(f.readline().strip())
    rows = int(f.readline().strip())
    length = int(f.readline().strip())

    reset()  
    width(1)
    speed(0)
    hideturtle()
    setup(500,500)
    penup()
    goto(-200,200)
    pendown()

    for i in range(rows):
        for x in range(columns):
            pcolor = f.readline().strip()
            
            pixel(length,pcolor)
            forward(length)
        backward(length * columns)
        right(90)
        forward(length)
        left(90)

#Function - Main
def main():
    print("--------Pixels-------\n\n")
    print("What would you like to do?\n\n[1]Load a Drawing\n[2]Create/Overwrite a Drawing\n[3]Exit\n")
    try:
        choice = int(input("Choice: "))
    except:
        print("Please enter a valid choice.")
        main()
    if choice == 1:
        load()
    elif choice == 2:
        create()
    elif choice == 3:
        print("Exiting...")
        quit()
    else:
        print("Please enter a valid choice.")
        main()

#Main
main()
done()



            
    


