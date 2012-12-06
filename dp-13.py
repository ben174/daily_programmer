#!/usr/bin/env python

""" Written by Ben Friedland as a response to the challenge at """
""" http://www.reddit.com/r/dailyprogrammer/comments/149kec/1242012_challenge_114_easy_word_ladder_steps/ """

import urllib2


word_list = []

def get_list(): 
    words = urllib2.urlopen("http://pastebin.com/raw.php?i=zY4Xt7iB").readlines()
    words = [w.replace("\r\n", "") for w in words]
    return words



def ladder(word): 
    global word_list
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ret = []
    for i, l in enumerate(word): 
        palette = alphabet.replace(l, "")
        test_word_list = list(word)
        
        for letter in palette: 
            test_word_list[i] = letter
            test_word = "".join(test_word_list)

            if test_word in word_list: 
                ret.append(test_word)

    return ret

def bonus_1(): 
    global word_list
    for word in word_list: 
        print "Checking word: %s" % word
        lad = ladder(word)
        print len(lad)
        if len(lad) == 33: 
            print word
            return word
        

            




def main(): 
    global word_list
    word_list = get_list()
    ladder("puma")
    bonus_1()

if __name__ == '__main__': 
    main()
