from random import randrange
import package.Fonctions as f

print("7|8|9\n4|5|6\n1|2|3\n")

nomj = input("Tapez le nom du joueur ")
recommencer = "o"



while recommencer.lower() == "o":

    plateau = [[0,0,0],[0,0,0],[0,0,0]]
    alea = randrange(0,9)
    i = 0
    difficulty = int(input("difficulte (0 = impossible ---> 8 = tres facile): "))

    while f.winner(plateau) == 0 and i < 9:
        j = (i + alea)%2+1

        if j == 1:
            print("A",nomj,"de jouer.")
            f.choixjoueur(plateau)
        else:
            print("A l'ordinateur de jouer.")
            f.iajouer(9-(i + difficulty),plateau)

        f.affplat(plateau)
        i += 1

    if f.winner(plateau) == 3:
        print("Match nul")
    elif f.winner(plateau) == 1:
        print("Defaite")
    else:
        print("Victoire")

    recommencer = input("Voulez-vous recommencer ? (o/n) ")
