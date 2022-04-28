import random

from tkinter import *
from tkinter import ttk

fenetre = Tk()

frm = ttk.Frame(fenetre, padding=10)
frm.grid()
ttk.Label(frm, text="veuillez choisir entre pierre, feuille et ciseaux !").grid(
    column=0, row=0)
# nbr = random.randint(0, 10)
# while entre != nbr:
#     entre = input()
#     print("choisissez un nombre !")
#     if entre == nbr:
#         print("bravo!")
#     else:
#         print("perdu le nombre etait")


def rpsplay():
    joueur = input(
        "Choisissez entre Pierre, Papier ou Ciseaux\nLe permier arriver a 5 point gagne bonne chance !! \n")
    while joueur not in ["pierre", "papier", "ciseaux"]:
        joueur = input("Choisissez entre Pierre, Papier ou Ciseaux\n")
    return(joueur)


def rpscomp():
    my_liste = ["pierre", "papier", "ciseaux"]
    play = random.choice(my_liste)
    return(play)


# def rpsreplay():
#     replay = input("Voulez vous rejouer entrer oui ou non\n")
#     while replay not in ["oui", "non"]:
#         replay = input("Voulez vous rejouer entrer oui ou non\n")
#     return(replay)


# def pointcom():
#     a = 0
#     a + 1
#     print(a)
#     return(a)


# def pointplayer():
#     b = 0
#     b + 1
#     print(b)
#     return(b)


com_point = 0
player_point = 0


while com_point or player_point < 5:
    a = rpscomp()
    b = rpsplay()
    c = "Le joueur adverse a jouer " + str(a)
    if a == b:
        print("egalité", c)
        print("vous avez " + str(player_point),
              "L'ordinateur a " + str(com_point))
    if a == "papier" and b == "ciseaux":
        print("vous avez gagner !", c)
        player_point += 1
        print("vous avez " + str(player_point))
    elif a == "ciseaux" and b == "pierre":
        print("vous avez gagner! ", c)
        player_point += 1
        print("vous avez " + str(player_point))
    elif a == "pierre" and b == "papier":
        print("vous avez gagner !", c)
        player_point += 1
        print("vous avez " + str(player_point))
    elif a == "pierre" and b == "ciseaux":
        print("vous avez perdu !", c)
        com_point += 1
        print("L'ordinateur a " + str(com_point))
    elif a == "ciseaux" and b == "papier":
        print("vous avez perdu !", c)
        com_point += 1
        print("L'ordinateur a " + str(com_point))
    elif a == "papier" and a == "pierre":
        print("vous avez perdu ! ", c)
        com_point += 1
        print("L'ordinateur a " + str(com_point))
    if player_point == 5:
        print("vous avez gagner felicitation !!!")
    if com_point == 5:
        print("Vous avez perdu l'ordinateur a gagner !! ")
