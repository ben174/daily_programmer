#!/usr/bin/python 

import re 

def main(): 
    input = 'this is a test. test is a you. how are you? do not test me\n'
    f = open('forgotten.txt')
    input = f.read()
    
    process_text(input)

def process_text(input): 
    words = {}
    delimiters = '".,:;!?()[]{}'
    for d in delimiters: 
        input = input.replace(d, ' '+d+' ')

    for word in input.split(): 
        word = word.lower()
        if word in words: 
            words[word] = words[word] + 1
        else: 
            words[word] = 1

    for word in sorted(words, key=words.get, reverse=True): 
        print "%d: %s" % (words[word], word)
        

    

if __name__ == '__main__': 
    main()
