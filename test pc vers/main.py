import random
import os
import time
#the x and the y are inverted...I got to change this. @Ci3l (17/06/21)

def initMap():
    for x in range(length):
        for y in range(width):
            map[x][y] = random.randint(0,1)

def printMap():
   for x in range(length):
        for y in range(width):
            print(' ' + str( map[x][y]),end= '')
        print()

def logic(map):
    newMap = [[0 for x in range(length)] for y in range(width)]
    for x in range(length):
        for y in range(width):
            num = []
            if x == 0 and y == 0 :#en haut à gauche
                num.append(map[x][y+1])
                num.append(map[x+1][y+1])
                num.append(map[x+1][y])
            if x == 0 and y == width-1 :#en haut à droite 
                num.append(map[x+1][y])
                num.append(map[x+1][y-1])
                num.append(map[x][y-1])
            if x == length-1 and y == width-1 :#en bas à droite
                num.append(map[x][y-1])
                num.append(map[x-1][y-1])
                num.append(map[x-1][y])
            if x == length-1 and y == 0: #en bas à gauche
                num.append(map[x-1][y])
                num.append(map[x-1][y+1])
                num.append(map[x][y+1])
            elif x == 0 and y != 0 and y != width - 1:#première ligne
                num.append(map[x][y+1])
                num.append(map[x+1][y+1])
                num.append(map[x+1][y])
                num.append(map[x+1][y-1])
                num.append(map[x][y-1])
            elif y == 0 and x != 0 and x != length -1:#première colonne
                num.append(map[x-1][y])
                num.append(map[x-1][y+1])
                num.append(map[x][y+1])
                num.append(map[x+1][y+1])
                num.append(map[x+1][y])
            elif x == width-1 and y != 0 and y != width - 1:#dernière ligne
                num.append(map[x][y+1])
                num.append(map[x-1][y+1])
                num.append(map[x-1][y])
                num.append(map[x-1][y-1])
                num.append(map[x][y-1])
            elif y == length -1 and x != 0 and x != length - 1:#dernière colonne
                num.append(map[x+1][y])
                num.append(map[x-1][y])
                num.append(map[x-1][y-1])
                num.append(map[x][y-1])
                num.append(map[x+1][y-1])
            elif y != 0 and y != width-1 and x != 0 and x != length-1:
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
            if livingCells == 3 :
                newMap[x][y] = 1
            if livingCells == 2 and map[x][y] == 1:
                newMap[x][y] = 1
            elif livingCells != 2 and livingCells != 3:
                newMap[x][y] = 0
    for x in range(length):
        for y in range(width):
            map[x][y] = newMap[x][y]

generations = input("Enter the number of generations you want ")
length = input("Enter the length of your board ")
width = input("Enter the width of your board ")
length,width = int(length),int(width)
map = [[0 for x in range(length)] for y in range(width)]
initMap()
i = 0
while i <= int(generations) :
    time.sleep(1.16)
    os.system('cls')
    logic(map)
    print()
    printMap()
    print("gen : {}".format(i))
    i += 1 
