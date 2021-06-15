from array import *
import random

def initMap():
    for x in range(length):
        for y in range(width):
            map[x][y] = random.randint(0,9)

def printMap():
   for x in range(length):
        for y in range(width):
            print(' ' + str( map[x][y]),end= '')
        print()

def logic():
    newMap = [[0 for x in range(length)] for y in range(width)]
    for x in range(length):
        for y in range(width):
            num = []
            if x == 0:
                num.append(map[x-1][y+1])
                num.append(map[x][y+1])
                num.append(map[x+1][y+1])
                num.append(map[x+1][y])
                num.append(map[x-1][y])
            if x == length:
                num.append(map[x+1][y])
                num.append(map[x+1][y-1])
                num.append(map[x][y-1])
                num.append(map[x-1][y-1])
                num.append(map[x-1][y])
            if y == 0:
                num.append(map[x][y+1])
                num.append(map[x+1][y+1])
                num.append(map[x+1][y])
                num.append(map[x+1][y-1])
                num.append(map[x][y-1])
            if y == width:
                num.append(map[x-1][y+1])
                num.append(map[x][y+1])
                num.append(map[x][y-1])
                num.append(map[x-1][y-1])
                num.append(map[x-1][y])
            else:
                num.append(map[x-1][y+1])
                num.append(map[x][y+1])
                num.append(map[x+1][y+1])
                num.append(map[x+1][y])
                num.append(map[x+1][y-1])
                num.append(map[x][y-1])
                num.append(map[x-1][y-1])
                num.append(map[x-1][y])
            livingCells = num.count(1)
            diedCells = num.count(0)
            if livingCells == 3:
                newMap[x][y] = 1
            if diedCells != 2 or diedCells != 3:
                newMap[x][y] = 0
    map = newMap

length, width = 10, 10
map = [[0 for x in range(length)] for y in range(width)] 
initMap()
printMap()
logic()
printMap()



