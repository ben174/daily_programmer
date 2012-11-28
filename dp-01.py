#!/usr/bin/env python

""" Written by Ben Friedland as a response to the challenge at """
""" http://www.reddit.com/r/dailyprogrammer/comments/12k3xr/1132012_challenge_110_easy_keyboard_shift/ """

badd_alph = "snvfrghjokl;,mp[wtdyibecux "
good_alph = "abcdefghijklmnopqrstuvwxyz "

def star_delete(input): 
    ret = []
    for i in input: 
        ret.append(good_alph[badd_alph.find(i.lower())])
    output = ''.join(ret)
    return output
    


def main(): 
    print "Running tests... "
    print star_delete("Jr;;p ept;f") 

if __name__ == '__main__':
    main()
