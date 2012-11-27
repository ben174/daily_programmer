#!/usr/bin/python

import random
import math

bomb_count = 20 
field_size = 15 
field = []

def main(): 
    create_field()
    place_bombs() 
    place_flags()
    print_field()

def create_field(): 
    for i in range(field_size): 
        row = []
        for j in range(field_size):  
            row.append(0)
        field.append(row)

def place_bombs(): 
    bombs_placed = 0
    while True: 
        i = random.randint(0, (field_size*field_size)-1)
        x = int(math.floor(i / field_size))
        y = int(i % field_size)
        if field[x][y] != "X": 
            field[x][y] = "X"
            bombs_placed += 1
        if bombs_placed == bomb_count: 
            break

def place_flags(): 
    for x in range(field_size): 
        for y in range(field_size):  
            if field[x][y] == "X": 
                for a in range(-1, 2): 
                    for b in range(-1, 2): 
                        try:
                            field[x+a][y+b] += 1
                        except: 
                            pass
    for x in range(field_size): 
        for y in range(field_size):  
            if field[x][y] == 0: 
                field[x][y] = "-" 

def print_field(): 
    for row in field:
        line = ""
        for cell in row: 
            line += str(cell) + " " 
        print line

if __name__ == '__main__': 
    main()
