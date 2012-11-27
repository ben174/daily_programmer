def star_delete(input): 
    ret = []
    for i in input: 
        ret.append(good_alph[badd_alph.find(i.lower())])
    output = ''.join(ret)
    return output
    

alphabet = "abcdefghijklmnopqrustuvwxyz"

def main(): 

    f = open("enable1.txt")
    index = 0
    for line in f.readlines(): 
        line = line.strip()
        for letter in line: 
            while alphabet[index] != letter: 
                index += 1

        print line.strip()
        if index > 26: 
            print " bad word!"
        else: 
            print " alphabetical!"


if __name__ == '__main__':
    main()
