from array import *
import random

a, b = 5, 5
T = [[0 for x in range(a)] for y in range(b)]

for r in T:
    for c in r:
        print(random.randint(0,1))
    print()

# Comment jmet en mode tableau ? :'( c'est un SOS



