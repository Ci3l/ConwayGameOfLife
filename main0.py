from array import *
import random
import os 
import time

length, width = 30, 30
map = [[0 for x in range(length)] for y in range(width)]

def initMap():
    for y in range(width):
        for x in range(length):
            map[y][x] = random.randint(0,1)

def printMap():
    for y in range(width):
        for x in range(length):
            print(' ' + str( map[y][x]),end= '')
        print()

def logic(map):
    newMap = [[0 for x in range(length)] for y in range(width)]
    for y in range(width):
        for x in range(length):
            num = []
            if y == 0 and x == 0 :#en haut à gauche
                num.append(map[y][x+1])
                num.append(map[y+1][x+1])
                num.append(map[y+1][x])
            if y == 0 and x == width-1 :#en haut à droite 
                num.append(map[y+1][x])
                num.append(map[y+1][x-1])
                num.append(map[y][x-1])
            if y == length-1 and x == width-1 :#en bas à droite
                num.append(map[y][x-1])
                num.append(map[y-1][x-1])
                num.append(map[y-1][x])
            if y == length-1 and x == 0: #en bas à gauche
                num.append(map[y-1][x])
                num.append(map[y-1][x+1])
                num.append(map[y][x+1])
            elif y == 0 and x != 0 and x != width - 1:#première ligne
                num.append(map[y][y+1])
                num.append(map[y+1][x+1])
                num.append(map[y+1][x])
                num.append(map[y+1][x-1])
                num.append(map[y][x-1])
            elif x == 0 and y != 0 and y != length -1:#première colonne
                num.append(map[y-1][x])
                num.append(map[y-1][x+1])
                num.append(map[y][x+1])
                num.append(map[y+1][x+1])
                num.append(map[y+1][x])
            elif y == width-1 and x != 0 and x != width - 1:#dernière ligne
                num.append(map[y][x+1])
                num.append(map[y-1][x+1])
                num.append(map[y-1][x])
                num.append(map[y-1][x-1])
                num.append(map[y][x-1])
            elif x == length -1 and y != 0 and y != length - 1:#dernière colonne
                num.append(map[y+1][x])
                num.append(map[y-1][x])
                num.append(map[y-1][x-1])
                num.append(map[y][x-1])
                num.append(map[y+1][x-1])
            elif x != 0 and x != width-1 and y != 0 and y != length-1:
                num.append(map[y-1][x+1])
                num.append(map[y][x+1])
                num.append(map[y+1][x+1])
                num.append(map[y+1][x])
                num.append(map[y+1][x-1])
                num.append(map[y][x-1])
                num.append(map[y-1][x-1])
                num.append(map[y-1][x])
            livingCells = num.count(1)
            diedCells = num.count(0)
            if livingCells == 3 :
                newMap[y][x] = 1
            if livingCells == 2 and map[y][x] == 1:
                newMap[y][x] = 1
            elif livingCells != 2 and livingCells != 3:
                newMap[y][x] = 0
    for y in range(width):
        for x in range(length):
            map[y][x] = newMap[y][x]



initMap()
generations = input()
i = 0
while i <= int(generations) :
    time.sleep(1.16)
    os.system('cls')
    logic(map)
    print()
    printMap()
    i += 1 
