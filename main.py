from kandinsky import *
import random
import time

length_of_screen, width_of_screen, living_cells, died_cells = 320,200,0,0 #the width isn't the real width of the screen because we need room to place the generation counter

def init_map(width, length, map):#init map randomly
    for y in range(width):
        for x in range(length):
            map[y][x] = random.randint(0, 1)

def print_map(width, length, map):  # draw the map in an adaptive way to fit in the screen
    squale = (320/length)
    squale = int(squale)
    beginingX,beginingY,limitX,limitY = 0,0,squale,squale#size of each pixel
    pX, pY = 0, 0#the pointers
    for y in range(width):
        for x in range(length):
            if map[y][x] == 1:
                for pX in range(beginingX,limitX):
                    for pY in range(beginingY, limitY):
                        set_pixel(pX,pY, color(0, 0, 0))
            elif map[y][x] == 0:
                for pX in range(beginingX, limitX):
                    for pY in range(beginingY, limitY):
                        set_pixel(pX, pY, color(255, 255, 255))
            beginingX = beginingX + squale
            limitX = beginingX + squale
        beginingY = beginingY + squale
        limitY = beginingY + squale
        beginingX = 0  

def clean_map():#earase everything on the screen 
    for y in range(width_of_screen):
        for x in range(length_of_screen):
            set_pixel(x, y, color(255, 255, 255))

def logic(width, length, map, generation_counter):#aply the rules of the game 
    new_map = [[0 for x in range(length)] for y in range(width)]
    living_cells, died_cells = 0,0
    for y in range(width):
        for x in range(length):
            num = []
            if y == 0 and x == 0:  # en haut à gauche
                num.append(map[y][x+1])
                num.append(map[y+1][x+1])
                num.append(map[y+1][x])
            if y == 0 and x == length-1:  # en haut à droite
                num.append(map[y+1][x])
                num.append(map[y+1][x-1])
                num.append(map[y][x-1])
            if y == width-1 and x == length-1:  # en bas à droite
                num.append(map[y][x-1])
                num.append(map[y-1][x-1])
                num.append(map[y-1][x])
            if y == width-1 and x == 0:  # en bas à gauche
                num.append(map[y-1][x])
                num.append(map[y-1][x+1])
                num.append(map[y][x+1])
            elif y == 0 and x != 0 and x != length - 1:  # première ligne
                num.append(map[y][y+1])
                num.append(map[y+1][x+1])
                num.append(map[y+1][x])
                num.append(map[y+1][x-1])
                num.append(map[y][x-1])
            elif x == 0 and y != 0 and y != width - 1:  # première colonne
                num.append(map[y-1][x])
                num.append(map[y-1][x+1])
                num.append(map[y][x+1])
                num.append(map[y+1][x+1])
                num.append(map[y+1][x])
            elif y == width-1 and x != 0 and x != length - 1:  # dernière ligne
                num.append(map[y][x+1])
                num.append(map[y-1][x+1])
                num.append(map[y-1][x])
                num.append(map[y-1][x-1])
                num.append(map[y][x-1])
            elif x == length - 1 and y != 0 and y != width - 1:  # dernière colonne
                num.append(map[y+1][x])
                num.append(map[y-1][x])
                num.append(map[y-1][x-1])
                num.append(map[y][x-1])
                num.append(map[y+1][x-1])
            elif x != 0 and x != length-1 and y != 0 and y != width-1:
                num.append(map[y-1][x+1])
                num.append(map[y][x+1])
                num.append(map[y+1][x+1])
                num.append(map[y+1][x])
                num.append(map[y+1][x-1])
                num.append(map[y][x-1])
                num.append(map[y-1][x-1])
                num.append(map[y-1][x])
            living_cells_arround = num.count(1)
            diedCells = num.count(0)
            if living_cells_arround == 3:
                new_map[y][x] = 1
            if living_cells_arround == 2 and map[y][x] == 1:
                new_map[y][x] = 1
                living_cells += 1
            elif living_cells_arround != 2 and living_cells_arround != 3:
                new_map[y][x] = 0
                died_cells += 1
    for y in range(width):
        for x in range(length):
            map[y][x] = new_map[y][x]  # merge the older vers with the new one
    draw_string("gen {}".format(generation_counter), 10, 204)
    draw_string("died {}".format(died_cells), 80, 204)
    draw_string("living {}".format(living_cells), 180, 204)

def start(generations = 8,length = 32, width = 20):#40*25
    map = [[0 for x in range(length)] for y in range(width)]
    generation_counter = 1
    init_map(width, length, map)
    print_map(width, length, map)
    draw_string("gen 0",10,204)
    for i in range(1,generations):
        time.sleep(1.16)
        logic(width, length, map, generation_counter)
        clean_map()
        print_map(width, length, map)
        generation_counter += 1 ;