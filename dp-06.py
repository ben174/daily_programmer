#!/usr/bin/python 

import random 


def main(): 
    byte_count = 100000
    paragraph = ''
    #letters = 'abcdefghijklmnopqrstuvwxyz  '
    chars = "aaaaabbbccddeeeeeeeeffghhhhiiiiiijklllll"
    chars += "mmmmmnnnnnoooooooppppqrrrrrssssssttttttuuuvwxyz"
    chars += "                           "
    f = open('enable1.txt')
    dictblob = f.read()
    dictionary = dictblob.split()

    for i in range(byte_count): 
        paragraph += chars[random.randrange(0, len(chars))]

    print "checking words..."
    real_words = []
    for fake_word in paragraph.split(): 
        if fake_word in dictionary: 
            real_words.append(fake_word)

    print real_words

if __name__ == '__main__': 
    main()

