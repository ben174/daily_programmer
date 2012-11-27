#!/usr/bin/python 

import logging

def main():
    run_test("+123", "int")
    run_test("-123", "int")
    run_test("0", "int")
    run_test("123.456", "float")
    run_test("20-11-2012", "date")
    run_test("Hello, world!", "text")

def run_test(input, desired_output): 
    ret = identify_datatype(input) 
    success = (desired_output == ret)
    print "  %s => %s (%s)" % (input, ret, str(success))
    

def identify_datatype(input): 
    try: 
        if "." in input:
            float(input)
            return "float"
        else: 
            int(input) 
            return "int"
    except: 
        pass

    dt_split = input.split("-")

    if len(dt_split) == 3: 
        if (len(dt_split[0]) == 2 and 
            len(dt_split[1]) == 2 and
            len(dt_split[2]) == 4): 
            try: 
                int(dt_split[0])
                int(dt_split[1])
                int(dt_split[2])
                return "date"
            except: 
                pass
    
    ret = "text"
    return ret

if __name__ == "__main__": 
    main()
