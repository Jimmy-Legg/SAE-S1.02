import os
import random
import time

#----------------------------------------
#change le tour
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : int
#
#Sortie : int
#----------------------------------------
def __changeTurn(turn : int)->int:
    if(turn == 1): return 2
    else: return 1

#----------------------------------------
#retourne le code couleur d'un symbole sous forme str
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : str
#
#Sortie : str
#----------------------------------------
def __couleur(symbole : str)->str:

    B  = '\033[94m' # blue
    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)

    if(symbole == "X"):return B
    elif(symbole == "O"): return R
    else: return W

#----------------------------------------
#Vérifie le type de victoire si victoire il ya
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : list[str]
#
#Sortie : object (object[bool, int]) avec object[0] -> victoire ?; object[1] -> type de victoire
#----------------------------------------
def __checkEquality(cases : list[str])->bool:

    i : int
    equality : bool
    equality = True

    for i in range(0, len(cases)) :
        if(cases[i] == "."): equality = False

    if(equality):return True
    else: return False

#----------------------------------------
#Vérifie le type de victoire si victoire il ya
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : list[str]
#
#Sortie : list[bool | int]
#----------------------------------------
def __checkWin(cases : list[str])->list[bool | int]:

    winType : int
    gameFinished : bool

    gameFinished = False

    if(cases[0] == cases[4] and cases[4] == cases[8] and not cases[4] == "."):
        winType = 1
        gameFinished = True
    elif(cases[2] == cases[4] and cases[4] == cases[6] and not cases[4] == "."):
        winType = 2
        gameFinished = True
    elif(cases[0] == cases[1] and cases[1] == cases[2] and not cases[0] == "."):
        winType = 3
        gameFinished = True
    elif(cases[3] == cases[4] and cases[4] == cases[5] and not cases[3] == "."):
        winType = 4
        gameFinished = True
    elif(cases[6] == cases[7] and cases[7] == cases[8] and not cases[6] == "."):
        winType = 5
        gameFinished = True
    elif(cases[0] == cases[3] and cases[3] == cases[6] and not cases[0] == "."):
        winType = 6
        gameFinished = True
    elif(cases[1] == cases[4] and cases[4] == cases[7] and not cases[1] == "."):
        winType = 7
        gameFinished = True
    elif(cases[2] == cases[5] and cases[5] == cases[8] and not cases[2] == "."):
        winType = 8
        gameFinished = True
    else:
        winType = 0
        gameFinished = False

    return [gameFinished, winType]

#----------------------------------------
#Affiche l'interface de jeu
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : str, str, int, int, list[str]
#
#Sortie : affichage
#----------------------------------------
def __afficherMenu(j1_name : str, j2_name : str, cases : list[str]):
    """Affiche l'interface de jeu

    Arguments :
        grille morpion : list
        personne qui a gagné : int

    Retour : rien

    Private : variable accessible uniquement dans le script actuel
    """
    os.system("cls")
    
    N  = '\033[90m' # noir
    W  = '\033[0m'  # white (normal)
    
    print("--------------------------------------------")
    print(N +"Schéma :")
    print("                 7 | 8 | 9")
    print("                 4 | 5 | 6")
    print("                 1 | 2 | 3" + W)
    print("---------------------------------------------")
    print("Partie :")
    print("                 " + __couleur(cases[6]) + cases[6] + W + " | " + __couleur(cases[7]) + cases[7] + W + " | " + __couleur(cases[8]) + cases[8] + W)
    print("                 " + __couleur(cases[3]) + cases[3] + W + " | " + __couleur(cases[4]) + cases[4] + W + " | " + __couleur(cases[5]) + cases[5] + W)
    print("                 " + __couleur(cases[0]) + cases[0] + W + " | " + __couleur(cases[1]) + cases[1] + W + " | " + __couleur(cases[2]) + cases[2] + W)
    print("---------------------------------------------")



def __affichageFin(cases : list[str], winType : int):
    """Affiche la grille finale avec les couleurs de victoire (les cases de victoires sont en vert)

    Arguments :
        grille morpion : list
        personne qui a gagné : int

    Retour : rien

    Private : variable accessible uniquement dans le script actuel
    """
    mot : str

    W  = '\033[0m'  # white (normal)
    G  = '\033[92m' # green
    N  = '\033[90m' # noir
    os.system("cls")
    print("--------------------------------------------")
    print( N + "Schéma :")
    print("                 7 | 8 | 9")
    print("                 4 | 5 | 6")
    print("                 1 | 2 | 3" + W)
    print("---------------------------------------------")
    print("Partie terminée : ")

    mot = "                 "
    if((winType == 2) or (winType == 5) or (winType == 6)): mot += G
    else: mot +=  __couleur(cases[6])
    mot += cases[6] + W + " | "
    if((winType == 5) or (winType == 7)): mot += G
    else: mot += __couleur(cases[7])
    mot += cases[7] + W + " | "
    if((winType == 1) or (winType == 5) or (winType == 8)): mot += G
    else: mot += __couleur(cases[8])
    mot += cases[8] + W
    print(mot)

    mot = "                 "
    if((winType == 4) or (winType == 6)): mot += G
    else: mot += __couleur(cases[3])
    mot += cases[3] + W + " | "
    if((winType == 1) or (winType == 2) or (winType == 4) or (winType == 7)): mot += G
    else: mot += __couleur(cases[4])
    mot += cases[4] + W + " | "
    if((winType == 4) or (winType == 8)): mot += G
    else: mot += __couleur(cases[5])
    mot += cases[5] + W
    print(mot)

    mot = "                 "
    if((winType == 1) or (winType == 3) or (winType == 6)): mot += G
    else: mot += __couleur(cases[0])
    mot += cases[0] + W + " | "
    if((winType == 3) or (winType == 7)): mot += G
    else: mot += __couleur(cases[1])
    mot += cases[1] + W + " | "
    if((winType == 2) or (winType == 3) or (winType == 8)): mot += G
    else: mot += __couleur(cases[2])
    mot += cases[2] + W
    print(mot)

    print("---------------------------------------------")

   
def __bot_difficulte3(cases : list[str],turn : int):
    """lance le bot difficulté 3

    Arguments :
        grille morpion : list
        qui joue :

    Retour : retourn le choix du bot
    """
    choice : str
    start :list[str]
    chancemax : int
    wincases : str
    winchoices : list[int]
    start = ["1","3","7","9"]
    winchoices = [0,0,0,0,0,0,0,0,0]
    choice = ""
    if turn == 1:
        wincases = "X"
    elif turn == 2:
        wincases = "O"
    #si joue sur la diagonal op
    if cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = random.choice(start)
    #Lignes 1-2-3
    if cases[7-1] == cases[4-1] and not cases[7-1] == "." and cases[1-1] == "." :
        if cases[7-1] == wincases:
            winchoices[0] = 99
        elif cases[7-1] != wincases and winchoices[0] != 99:
            winchoices[0] = -99
    if cases[8-1] == cases[5-1] and not cases[8-1] == "." and cases[2-1] == "." :
        if cases[8-1] == wincases:
            winchoices[1] = 99
        elif cases[8-1] != wincases and winchoices[1] != 99:
            winchoices[1] = -99
    if cases[9-1] == cases[6-1] and not cases[9-1] == "." and cases[3-1] == "." :
        if cases[9-1] == wincases:
            winchoices[2] = 99
        elif cases[9-1] != wincases and winchoices[2] != 99:
            winchoices[2] = -99
    #Lignes 4-5-6
    if cases[7-1] == cases[1-1] and not cases[1-1] == "." and cases[4-1] == "." :
        if cases[7-1] == wincases:
            winchoices[3] = 99
        elif cases[7-1] != wincases and winchoices[3] != 99:
            winchoices[3] = -99
    if cases[8-1] == cases[2-1] and not cases[2-1] == "." and cases[5-1] == "." :
        if cases[8-1] == wincases:
            winchoices[4] = 99
        elif cases[8-1] != wincases and winchoices[4] != 99:
            winchoices[4] = -99
    if cases[9-1] == cases[3-1] and not cases[3-1] == "." and cases[6-1] == "." :
        if cases[9-1] == wincases:
            winchoices[5] = 99
        elif cases[9-1] != wincases and winchoices[5] != 99:
            winchoices[5] = -99
    #Lignes 7-8-9
    if cases[4-1] == cases[1-1] and not cases[1-1] == "." and cases[7-1] == "." :
        if cases[4-1] == wincases:
            winchoices[6] = 99
        elif cases[4-1] != wincases and winchoices[6] != 99:
            winchoices[6] = -99
    if cases[5-1] == cases[2-1] and not cases[5-1] == "." and cases[8-1] == "." :
        if cases[5-1] == wincases:
            winchoices[7] = 99
        elif cases[5-1] != wincases and winchoices[7] != 99:
            winchoices[7] = -99
    if cases[3-1] == cases[6-1] and not cases[6-1] == "." and cases[9-1] == "." :
        if cases[3-1] == wincases:
            winchoices[8] = 99
        elif cases[3-1] != wincases and winchoices[8] != 99:
            winchoices[8] = -99
    #Colonnes 8-5-2
    if cases[7-1] == cases[9-1] and not cases[7-1] == "." and cases[8-1] == "." :
        if cases[7-1] == wincases:
            winchoices[7] = 99
        elif cases[7-1] != wincases and winchoices[7] != 99:
            winchoices[7] = -99
    if cases[6-1] == cases[4-1] and not cases[6-1] == "." and cases[5-1] == "." :
        if cases[6-1] == wincases:
            winchoices[4] = 99
        elif cases[6-1] != wincases and winchoices[4] != 99:
            winchoices[4] = -99
    if cases[3-1] == cases[1-1] and not cases[3-1] == "." and cases[2-1] == ".":
        if cases[3-1] == wincases:
            winchoices[1] = 99
        elif cases[3-1] != wincases and winchoices[1] != 99:
            winchoices[1] = -99
    #Colonnes 7-4-1
    if cases[8-1] == cases[9-1] and not cases[9-1] == "." and cases[7-1] == "." :
        if cases[8-1] == wincases:
            winchoices[6] = 99
        elif cases[8-1] != wincases and winchoices[6] != 99:
            winchoices[6] = -99
    if cases[6-1] == cases[5-1] and not cases[5-1] == "." and cases[4-1] == "." :
        if cases[6-1] == wincases:
            winchoices[3] = 99
        elif cases[6-1] != wincases and winchoices[3] != 99:
            winchoices[3] = -99
    if cases[2-1] == cases[3-1] and not cases[2-1] == "." and cases[1-1] == "." :
        if cases[2-1] == wincases:
            winchoices[0] = 99
        elif cases[2-1] != wincases and winchoices[0] != 99:
            winchoices[0] = -99
    #Colonnes 9-6-3
    if cases[7-1] == cases[8-1] and not cases[8-1] == "." and cases[9-1] == "." :
        if cases[7-1] == wincases:
            winchoices[8] = 99
        elif cases[7-1] != wincases and winchoices[8] != 99:
            winchoices[8] = -99
    if cases[4-1] == cases[5-1] and not cases[5-1] == "." and cases[6-1] == "." :
        if cases[4-1] == wincases:
            winchoices[5] = 99
        elif cases[4-1] != wincases and winchoices[5] != 99:
            winchoices[5] = -99
    if cases[1-1] == cases[2-1] and not cases[2-1] == "." and cases[3-1] == "." :
        if cases[1-1] == wincases:
            winchoices[2] = 99
        elif cases[1-1] != wincases and winchoices[2] != 99:
            winchoices[2] = -99
    #Diagonales 3-5-7
    if cases[7-1] == cases[5-1] and not cases[5-1] == "." and cases[3-1] == "." :
        if cases[7-1] == wincases:
            winchoices[2] = 99
        elif cases[7-1] != wincases and winchoices[2] != 99:
            winchoices[2] = -99
    if cases[7-1] == cases[3-1] and not cases[3-1] == "." and cases[5-1] == "." :
        if cases[7-1] == wincases:
            winchoices[4] = 99
        elif cases[7-1] != wincases and winchoices[4] != 99:
            winchoices[4] = -99
    if cases[5-1] == cases[3-1] and not cases[3-1] == "." and cases[7-1] == "." :
        if cases[5-1] == wincases:
            winchoices[6] = 99
        elif cases[5-1] != wincases and winchoices[6] != 99:
            winchoices[6] = -99
    #Diagonales 1-5-9
    if cases[9-1] == cases[5-1] and not cases[5-1] == "." and cases[1-1] == "." :
        if cases[9-1] == wincases:
            winchoices[0] = 99
        elif cases[9-1] != wincases and winchoices[0] != 99:
            winchoices[0] = -99
    if cases[9-1] == cases[1-1] and not cases[1-1] == "." and cases[5-1] == "." :
        if cases[9-1] == wincases:
            winchoices[4] = 99
        elif cases[9-1] != wincases and winchoices[4] != 99:
            winchoices[4] = -99
    if cases[5-1] == cases[1-1] and not cases[1-1] == "." and cases[9-1] == "." :
        if cases[5-1] == wincases:
            winchoices[8] = 99
        elif cases[5-1] != wincases and winchoices[8] != 99:
            winchoices[8] = -99


    elif cases[0] != wincases and cases[0] != "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = 5
    elif cases[0] == "O" and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "X" and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "O" and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "X" and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "O" and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "X" and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "O" and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "X" and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "O" and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "X" and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "O" and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "X" and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "O" and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == "X":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == "O":
        choice = "5"
    
    elif cases[0] == wincases and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] != wincases and cases[4] != "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == wincases:
        choice = "5"

    elif cases[1-1] == "O" and cases[5-1] == "X" and cases[9-1] == ".":
        if turn == 1:
            choice = "9"
    elif cases[9-1] == "O" and cases[5-1] == "X" and cases[1-1] == ".":
        if turn == 1:
            choice = "1"
    elif cases[7-1] == "O" and cases[5-1] == "X" and cases[3-1] == ".":
        if turn == 1:
            choice = "3"
    elif cases[3-1] == "O" and cases[5-1] == "X" and cases[7-1] == ".":
        if turn == 1:
            choice = "7"
    elif cases[1-1] == "X" and cases[5-1] == "O" and cases[9-1] == ".":
        if turn == 2:
            choice = "9"
    elif cases[9-1] == "X" and cases[5-1] == "O" and cases[1-1] == ".":
        if turn == 2:
            choice = "1"
    elif cases[7-1] == "X" and cases[5-1] == "O" and cases[3-1] == ".":
        if turn == 2:
            choice = "3"
    elif cases[3-1] == "X" and cases[5-1] == "O" and cases[7-1] == ".":
        if turn == 2:
            choice = "7"
    chancemax = 0


    for i in range(len(winchoices)):
        if int(winchoices[i]) > int(chancemax):
            chancemax = winchoices[i]
    if chancemax == 99:
        for i in range(len(winchoices)):
            if winchoices[i] == 99:
                choice = str(i + 1)
    else:
        for i in range(len(winchoices)):
            if winchoices[i] == -99:
                choice = str(i + 1)



    if choice == "":
        choices = [0,1,2,3,4,5,6,7,8]
        for _i in choices:
            if cases[choices[_i]] == ".":
                choice = choices[_i]+1
                break

    return str(choice)
def __bot_difficulte2(cases : list[str], turn : int):
    """lance le bot difficulté 2

    Arguments :
        grille morpion : list

    Retour : retourn le choix du bot
    """

    a : int
    bon : bool
    choices = list[int]
    choice = ""
    a = random.randint(1,2)
    if a == 1:
        if choice == "":
            choices = [0,1,2,3,4,5,6,7,8]
            for _i in choices:
                if cases[choices[_i]] == ".":
                    choice = choices[_i]+1
                    break
    else:
        choice = str(__bot_difficulte3(cases, turn))
    return str(choice)

def __bot(cases : list[str], difficulte : int ,player : str,C : str,turn :int):
    """lance le bot en fonction de la difficulté

    Arguments :
        grille morpion : list

    Retour : retourn le choix du bot
    """
    choice = ""
    W  = '\033[0m'  # white (normal)
    if difficulte == 1:
        choice = str(random.randint(1,9))
        print(C + player +  W + " choisi une case")
        time.sleep(0.5)
        if choice == "":
            choices = [0,1,2,3,4,5,6,7,8]
            for _i in choices:
                if cases[choices[_i]] == ".":
                    choice = choices[_i]+1
                    break
    elif difficulte == 2:
        print(C + player +  W + " choisi une case")
        time.sleep(0.5)
        choice = __bot_difficulte2(cases,turn)
    elif difficulte == 3:
        print(C + player +  W +" choisi une case")
        time.sleep(0.5)
        choice = __bot_difficulte3(cases,turn)
    return str(choice)


def LaunchGame_morpion(j1_name : str, j2_name : str, nb_joueurs : int,difficulte : list[int])->str:
    """Lance la partie de morpion et retourne le vainqueur de la partie

    Arguments :
        Nom joueur 1 : str
        Nom du joueur 2 : str
        Nombre de joueurs : int
        liste des difficulté : list[difficulté bot1, difficulté bot2]

    Retour : gagnant de la partie sous forme de str
    """
    cases : list[str]

    winner : str
    choice : str

    gameFinished : bool
    choiceIsOk : bool

    winType : int
    turn : int

    result_checkWin : list[bool | int]

    W  = '\033[0m'  # white (normal)
    R  = '\033[91m' # red
    B  = '\033[94m' # blue

    #initialise le tableau
    cases = [".",".",".",".",".",".",".",".","."]

    #intialise les données
    turn = random.randint(1,2)
    gameFinished = False

    winner = ""

    winType = 0
    #boucle principale
    while not gameFinished:

        choice = ""
        choiceIsOk = False
        while not choiceIsOk:

            #affiche le menu
            __afficherMenu(j1_name, j2_name, cases)

            #demande le choix de l'utilisateur
            if nb_joueurs == 2:
                if(turn == 1): choice = str(input(B + j1_name + W + " choisissez votre case en suivant le schéma ci dessus : "))
                else : choice = str(input(R + j2_name + W + " choisissez votre case en suivant le schéma ci dessus : "))
            elif nb_joueurs == 1:
                if(turn == 1): choice = str(input(B + j1_name + W + " choisissez votre case en suivant le schéma ci dessus : "))
                else: choice = __bot(cases,int(difficulte[1]),j2_name,R,turn)
            elif nb_joueurs == 0:
                if(turn == 1): choice = __bot(cases,int(difficulte[0]),j1_name,B,turn)
                else: choice = __bot(cases,int(difficulte[1]),j2_name,R,turn)
            #vérifie la valeur de l'utilisateur
            if(not choice.isdigit()):print("Valeur impossible")
            elif(int(choice) < 1 or int(choice) > 9):print("Valeur impossible")
            elif(cases[int(choice) - 1] == "."): choiceIsOk = True
            else: print("Cette case est occupée")


        #ajoute le symbole dans la case souhaité
        if(turn == 1):
            if nb_joueurs == 0:
                print(B + j1_name +  W + " à choisi la case : " + choice);time.sleep(0.5)
            cases[int(choice) - 1] = "X"
            
        elif(turn == 2):
            if nb_joueurs == 0:
                print(R + j2_name +  W + " à choisi la case : " + choice);time.sleep(0.5)
            elif nb_joueurs == 1:
                print(R + j2_name +  W + " à choisi la case : " + choice);time.sleep(0.5)
            cases[int(choice) - 1] = "O"
    

        #Vérification de victoire :
        result_checkWin = __checkWin(cases)

        gameFinished = bool(result_checkWin[0])
        winType = int(result_checkWin[1])

        #Changement de tour :
        turn =__changeTurn(turn)

        #Vérification d'égalité si pas de victoire :
        if(not gameFinished):
            gameFinished = __checkEquality(cases)
            if(gameFinished): winType = -1

        #Fin de Partie:
        if(gameFinished):
            #Affichage de la ligne gagnante en vert
            __affichageFin(cases, winType)

            #Affichage du vainqueur ou affichage du texte d'égalité
            if(winType == -1):
                print("égalité !")
            elif(turn == 2):
                print(B + j1_name + W + " a gagné ")
            elif(turn == 1):
                print(R + j2_name + W + " a gagné ")
            print("---------------------------------------------")


    os.system("pause")

    #Définition du vainqueur
    if(winType == -1):
        winner = ""
    elif(turn == 2):
        winner = j1_name
    elif(turn == 1):
        winner = j2_name

    #Retour
    return winner