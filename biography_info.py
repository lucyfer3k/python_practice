#!/usr/bin/python
import re

def gather_data(prompt, pattern):
    '''Asks user for input using __prompt__, verifies if the type provided
    matches __pattern__, returns value if correct or "" if incorrect.'''
    value = input(prompt)
    if not re.match(pattern, value):
        print("Incorrect value! Try again.\n")
        return None
    else:
        return value

if __name__ == "__main__":
    print ("This program will summarize your biography info provided.\n")
    name = address = birthdate = personal_goals = None

    name_q = "What is your name: "
    name_p = r"^[a-zA-Z\.\s]+$"
    
    while name is None:
        name = gather_data(name_q, name_p)

    birthdate_q = "What is your birthdate (DD-MM-YYYY): "
    birthdate_p = r"^[0-1]\d-[0-3]\d-[1-2]\d{3}$"
          
    while birthdate is None:
        birthdate = gather_data(birthdate_q, birthdate_p) 

    address_q = "What is your address: "     
    address_p = r"^[\w\.\-\s]+$" 
          
    while address is None:
        address = gather_data(address_q, address_p)

    personal_goals_q = "What are your personal goals: "     
    personal_goals_p = r"^[\w\s\.\-!?\"\']+$" 
          
    while personal_goals is None:
        personal_goals = gather_data(personal_goals_q, personal_goals_p) 

    print("\nYou can find Your biography below:")
    print("- Name: {}\n- Date of birth: {}\n- Address: {}\n- Personal goals: {}".format(name, birthdate, address, personal_goals))
