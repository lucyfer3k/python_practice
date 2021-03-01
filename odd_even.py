#!/usr/bin/python

print ("Welcome to 1 to 1000 odd or even program!\n")

i = ""

while i != "q":
    try:
        value = int(input("\nWhat number are you thinking of? "))
        
        if value%2 == 0:
            print ("That's an even number! Wanna have another go?")
       
        elif value%2 == 1:
            print ("That's an odd number! Wanna have another go?")

    except ValueError:
            print ("Incorrect value! Try again?")

    i = input("q to quit: ")
