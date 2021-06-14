from array import *
import random

def initMap():
    for x in range(length):
        for y in range(width):
            map[x][y] = random.randint(0,9)

def setPixel(x, y, newValue):
    map[x][y] = newValue

def getPixel(x, y):
    num = []
    num.append(map[x][y])
    num.append(map[x-1][y+1])
    num.append(map[x][y+1])
    num.append(map[x+1][y+1])
    num.append(map[x+1][y])
    num.append(map[x+1][y-1])
    num.append(map[x][y-1])
    num.append(map[x-1][y-1])
    num.append(map[x-1][y])
    return num

def printMap():
   for x in range(length):
        for y in range(width):
            print(' ' + str( map[x][y]),end= '')
        print()

length, width = 10, 10
map = [[0 for x in range(length)] for y in range(width)] 
initMap()
printMap()
print(getPixel(4,4))