#!/usr/bin/env python

""" Written by Ben Friedland as a response to the challenge at """
""" http://www.reddit.com/r/dailyprogrammer/comments/137f7t/11142012_challenge_112_easyget_that_url/ """

def main(): 
    parse_args("http://en.wikipedia.org/w/index.php?title=Main_Page&action=edit")


def parse_args(input): 
    args_line = input.split("?")[1]
    for arg_pair in args_line.split("&"): 
        aargs = arg_pair.split("=")
        print "key: %s\nvalue: %s\n" % (aargs[0], aargs[1])
        

if __name__ == "__main__": 
    main()
