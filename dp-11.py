#!/usr/bin/python

import datetime 
import sys

def main(): 
    myr = sys.argv[1].split('/')

    month = int(myr[0])
    year = int(myr[1])

    dt = datetime.date(year, month, 1)
    bar =  "+%s+" % ("-"*20)                     
    month_name = dt.strftime("%B")
    start_space = (10 - (len(month_name) / 2))
    end_space = (20 - (start_space+len(month_name)))
    
    print bar 
    print "|%s%s%s|" % (" "*start_space, month_name, " "*end_space)
    print bar 
    print "|S |M |T |W |T |F |S |"
    print bar

    line = "|"

    for i in xrange(dt.weekday()): 
        line += "  |"

    start_index = dt.weekday() 
    while True: 
        for i in xrange(start_index, 7): 
            if dt.month == month: 
                num = str(dt.day).zfill(2)
            else: 
                num = "  " 
            line += "%s|" % num 
            dt += datetime.timedelta(days=1)
        print line
        start_index = 0
        line = "|"
        if dt.month > month: 
            break 

    print bar


if __name__ == '__main__': 
    main()
