#appel le main c mieux
from array import *
import random

a, b = 5, 5#des noms explicites par pitié
T = [[0 for x in range(a)] for y in range(b)]#on évite les noms peu éloquant comme T :/

for r in T:#des noms explicites (pr les variables)
    for c in r:#des noms explicites
        print(random.randint(0,1))#t'as l'air d'avoir saisie comment fonctionne random sauf que là il ne définie rien il ne fait que print des chiffres
    print()

# Comment jmet en mode tableau ? :'( c'est un SOS
#-> pr ça il te suffie t'ajouter un arg à print comme ça : print("a",end='') le end='' va empêcher le passage de ligne
#T[ligne][colonne]
