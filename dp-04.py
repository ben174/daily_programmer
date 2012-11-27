#!/usr/bin/python

def main(): 
    parse_args("http://en.wikipedia.org/w/index.php?title=Main_Page&action=edit")


def parse_args(input): 
    args_line = input.split("?")[1]
    for arg_pair in args_line.split("&"): 
        aargs = arg_pair.split("=")
        print "key: %s\nvalue: %s\n" % (aargs[0], aargs[1])
        

if __name__ == "__main__": 
    main()
