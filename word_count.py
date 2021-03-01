#!/usr/bin/python

import re
import sys

print ("Welcome to Word count program!\n")

if len(sys.argv) > 1:
    try:
        file1 = open(sys.argv[1], "r+")
        lines = file1.readlines()
        word_count = 0

        for line in lines:
            word_count = word_count + len(re.findall(r'\w+', line))

        print ("Interesting! There are", word_count,"words in file:", sys.argv[1],".\n")
        file1.close()

    except FileNotFoundError:
        print ("File not found!")
    
else:
     i = 'y'
     while i != 'n':
        sentence = input("What's on your mind?\n")

        word_count = len(re.findall(r'\w+', sentence))

        print ("Interesting! You wrote", word_count,"words.\n")
        i = input("Try again? n to quit: ")
