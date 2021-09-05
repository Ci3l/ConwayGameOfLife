import random
import os
import time
#the x and the y are inverted...I got to change this. @Ci3l (17/06/21)

living_cells = 0

def init_map():
    for x in range(length):
        for y in range(width):
            map[x][y] = random.randint(0,1)

def print_map():
   for x in range(length):
        for y in range(width):
            print(' ' + str( map[x][y]),end= '')
        print()

def logic(map,i,width,length):
    new_map = [[0 for x in range(length)] for y in range(width)]
    living_cells = 0
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
            living_cells_arround = num.count(1)
            died_cells_around = num.count(0)
            if living_cells_arround == 3 :
                new_map[x][y] = 1
                living_cells += 1
            if living_cells_arround == 2 and map[x][y] == 1:
                new_map[x][y] = 1
                living_cells += 1
            elif living_cells_arround != 2 and living_cells_arround != 3:
                new_map[x][y] = 0
    for x in range(length):
        for y in range(width):
            map[x][y] = new_map[x][y]
    print("gen : {}  died cells : {}  living cells : {}".format(i, (width*length)-living_cells, living_cells))

generations = input("Enter the number of generations you want ")
length = input("Enter the length of your board ")
width = input("Enter the width of your board ")
length,width,generations = int(length),int(width), int(generations)
map = [[0 for x in range(length)] for y in range(width)]
init_map()
for i in range(generations) :
    time.sleep(1.16)
    os.system('cls')
    logic(map,i,width,length)
    print()
    print_map()
