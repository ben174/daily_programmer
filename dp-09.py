#!/usr/bin/python 



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
