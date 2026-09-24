#Password Checker
import time

checks = 0

def password_checker(checks):
  print("Welcome to PGO Security Systems") #Title displayed on screen
  print("*******************************") 
  print("") #goes one line down 
  
  password = input("Enter your password: ") #Password is a variable that asks a question
  
  print("")
  
  if password == "abcd1234": #checks if inputed variable is equal to the password
    print("Access Granted") #Displays text on screen
    print("")
  else: #checks if inputed variable is not equal to the password
    if checks == 2: #checks if attempted 2 times
      print("Access Denied               2 attempts made")
      print("")
      time.sleep(1) #waits for a second
      print("You have been locked out for 10 minutes")
      time.sleep(600) #waits for a minute
      password_checker(checks) #calls the function again
    elif checks == 4:
      print("Access Denied               4 attempts made")
      print("")
      time.sleep(1) #waits for a second
      print("You have been locked out for 10 minutes")
      time.sleep(1200) #waits for a minute
      password_checker(checks) #calls the function again
    else:
      print("Access Denied") 
      print("")
      checks += 1 #adds one to attemps
      time.sleep(1) #waits one second
      password_checker(checks) #calls the function again
    
password_checker(checks) #this calls the function initially to start the program

#Apps/Websites that ustilise python:
#Instagram, Dropbox, Reddit, Quora, Spotify