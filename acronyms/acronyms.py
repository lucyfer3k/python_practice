#!/usr/bin/env python3
import sys, re

def acronym(strings):
    '''Takes a string with more than one word and returns an acronym from it's
    first letters or 1 if there are no words to create acronym from'''
    strings_no_punctuation = re.sub(r"[\!\.?\-\*_]*", r"", strings).strip()

    if re.search(r"^\w+\s[\w\s]+\w$", strings_no_punctuation):
        acronym = ""
        for string in strings_no_punctuation.split():
            acronym += string[0]
        return acronym.upper()
    else:
        return 1


if __name__ == "__main__":
    print("Welcome to What's my acronym program!\n")
    try:
        result = acronym(sys.argv[1])
        if result != 1:
            print("Acronym for '{}' is: {}".format(sys.argv[1], result))
        else:
            print("I don't know an acronym for '{}'.".format(sys.argv[1]))
    except:
        print("You need to provide an argument!")
    
