from array import *
import random

def initMap():
    for x in range(length):
        for y in range(width):
            map[x][y] = random.randint(0,1)

def setPixel(x, y, newValue):
    map[x][y] = newValue

def getPixel(x, y):
    return map[x][y]

def printMap():
   for x in range(length):
        for y in range(width):
            print(' ' + str( map[x][y]),end= '')
        print()

length, width = 10, 10
map = [[0 for x in range(length)] for y in range(width)] 
initMap()
printMap()
