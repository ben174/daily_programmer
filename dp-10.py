#!/usr/bin/python 

import random

def main(): 
    letters = get_dictionary()
    input = "this is a hacker test. 123" 
    input = input.upper()
    output = []
    for i in input: 
        try: 
            r = random.randrange(0, len(letters[i]))
            output.append(letters[i][r])
        except: 
            output.append(i)
    print " ".join(output)


def get_dictionary(): 
    f = open('translations.txt', 'r')
    lines = f.readlines()
    letters = {}
    for line in lines:
        line_split = line.split()
        letters[line_split[0]] = line_split[1:]
    return letters

if __name__ == '__main__': 
    main()
