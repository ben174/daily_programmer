#!/usr/bin/env python

""" Written by Ben Friedland as a response to the challenge at """
""" -- hmm? --- """
""" I don't think I ever finished this one. I should figure out where it came from. """

def main(): 
    input = "123"

    for i, d in enumerate(input): 
        print "%d: %s" % (i, d)
        if d == "1" or d == "2": 
            try: 
                print "also %s" % (d + input[i+1])
            except:     
                pass

if __name__ == '__main__': 
    main()
