#!/usr/bin/python
import re

def verify_string(string_list):
    '''Checks if every string in the list is a single word. Returns True or False'''
    for string in string_list:
        if not re.search("^[a-zA-Z]+$", string):
            return False
    return True

if __name__ == "__main__":
    print ("Welcome to Madlibs game!\n")
    i = "" 

    while i != "q":
        print ("Please provide me with some words :)\n")
    
        noun = input("noun: ")
        verb = input("verb: ")
        exclamation = input("exclamation: ")
        adjective = input("adjective: ")
        room = input("room in a house: ")
        
        if verify_string([noun, verb, exclamation, adjective, room]):
            print ("Thank you! Your story:\n\n")

            print ("It was a {}, cold February day. My {} was hanging from the".format(adjective, noun) +
                   " celling in the {} downstairs. My mom said '{}! Take this bread and {} it!'".format(room, exclamation, verb))
        else:
            print ("At least one of the words provided is incorrect!")
        i = input("\nTry again? q to quit: ")
