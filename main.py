from array import *
import random

def init():
    for x in range(length):
        for y in range(width):
            map[x][y] = random.randint(1,10)

def setPixel(x, y, newValue):
    map[x][y] = newValue

def getPixel(x, y):
    return map[x][y]

def printMap():
    print()


length, width = 10, 10
map = [[0 for x in range(length)] for y in range(width)] 
init()
print(map)