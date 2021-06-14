from array import *
import random

def init():
    for x in map:
        for y in x:
            print( str(y) + " ",end='')
            y = random.randint(0, 10)
            print(str(y))

length, width = 10, 10
map = [[0 for x in range(length)] for y in range(width)]
init()
print(map)