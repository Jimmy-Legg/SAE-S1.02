import os
import random

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



#----------------------------------------
#Affiche la grille finale avec les couleurs de victoire (les cases de victoires sont en vert)
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : list[str], int
#
#Sortie : affichage
#----------------------------------------
def __affichageFin(cases : list[str], winType : int):

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

   
def bot_difficulte3(cases : list, joueur : int):
    choice : str
    liste = ["1","3","7","9"]
    choice = ""
    symboleautre : str
    symbole : str
    symboleautre = "X"
    symbole = "O"
    if joueur == 2 :
        symbole = "X"
        symboleautre = "O"


    #si joue sur la diagonal op
    if cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = str(random.choice(liste))
    #Lignes 1-2-3
    elif cases[7-1] == cases[4-1] and not cases[7-1] == "." and cases[1-1] == "." :
        choice = "1"
    elif cases[8-1] == cases[5-1] and not cases[5-1] == "." and cases[2-1] == "." :
        choice = "2"
    elif cases[9-1] == cases[6-1] and not cases[6-1] == "." and cases[3-1] == "." :
        choice = "3"
    #Lignes 4-5-6
    elif cases[7-1] == cases[1-1] and not cases[1-1] == "." and cases[4-1] == "." :
        choice = "4"
    elif cases[8-1] == cases[2-1] and not cases[2-1] == "." and cases[5-1] == "." :
        choice = "5"
    elif cases[9-1] == cases[3-1] and not cases[3-1] == "." and cases[6-1] == "." :
        choice = "6"
    #Lignes 7-8-9
    elif cases[4-1] == cases[1-1] and not cases[1-1] == "." and cases[7-1] == "." :
        choice = "7"
    elif cases[5-1] == cases[2-1] and not cases[5-1] == "." and cases[8-1] == "." :
        choice = "8"
    elif cases[3-1] == cases[6-1] and not cases[6-1] == "." and cases[9-1] == "." :
        choice = "9"
    #Colonnes 8-5-2
    elif cases[7-1] == cases[9-1] and not cases[7-1] == "." and cases[8-1] == "." :
        choice = "8"
    elif cases[6-1] == cases[4-1] and not cases[6-1] == "." and cases[5-1] == "." :
        choice = "5"
    elif cases[3-1] == cases[1-1] and not cases[3-1] == "." and cases[2-1] == "." :
        choice = "2"
    #Colonnes 7-4-1
    elif cases[8-1] == cases[9-1] and not cases[9-1] == "." and cases[7-1] == "." :
        choice = "7"
    elif cases[6-1] == cases[5-1] and not cases[5-1] == "." and cases[4-1] == "." :
        choice = "4"
    elif cases[2-1] == cases[3-1] and not cases[2-1] == "." and cases[1-1] == "." :
        choice = "1"
    #Colonnes 9-6-3
    elif cases[7-1] == cases[8-1] and not cases[8-1] == "." and cases[9-1] == "." :
        choice = "9"
    elif cases[4-1] == cases[5-1] and not cases[5-1] == "." and cases[6-1] == "." :
        choice = "6"
    elif cases[1-1] == cases[2-1] and not cases[2-1] == "." and cases[3-1] == "." :
        choice = "3"
    #Diagonales 7-5-3
    elif cases[7-1] == cases[5-1] and not cases[5-1] == "." and cases[3-1] == "." :
        choice = "3"
    elif cases[7-1] == cases[3-1] and not cases[3-1] == "." and cases[5-1] == "." :
        choice = "5"
    elif cases[5-1] == cases[3-1] and not cases[3-1] == "." and cases[7-1] == "." :
        choice = "7"
    #Diagonales 1-5-9
    elif cases[9-1] == cases[5-1] and not cases[5-1] == "." and cases[1-1] == "." :
        choice = "1"
    elif cases[9-1] == cases[1-1] and not cases[1-1] == "." and cases[5-1] == "." :
        choice = "5"
    elif cases[5-1] == cases[1-1] and not cases[1-1] == "." and cases[9-1] == "." :
        choice = "9"

    
    elif (cases[0] == symboleautre or cases[0] == symbole) and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and (cases[1] == symboleautre or cases[1] == symbole) and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and (cases[2] == symboleautre or cases[2] == symbole) and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and (cases[3] == symboleautre or cases[3] == symbole) and cases[4] == "." and cases[5] == "." and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and (cases[5] == symboleautre or cases[5] == symbole) and cases[6] == "." and cases[7] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and (cases[6] == symboleautre or cases[6] == symbole) and cases[6] == "." and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "." and (cases[7] == symboleautre or cases[7] == symbole) and cases[8] == ".":
        choice = "5"
    elif cases[0] == "." and cases[1] == "." and cases[2] == "." and cases[3] == "." and cases[4] == "." and cases[5] == "." and cases[6] == "."  and cases[7] == "."and (cases[8] == symboleautre or cases[8] == symbole):
        choice = "5"


    elif (cases[0] == symboleautre or cases[0] == symbole) and cases[1] == "." and cases[2] == "." and cases[3] == "." and (cases[4] == symbole or cases[4] == symboleautre ) and cases[5] == "." and cases[6] == "."  and cases[7] == "."and (cases[8] == symboleautre or cases[8] == symbole):
        choice = "2"
    elif cases[0] == "." and cases[1] == "." and (cases[2] == symboleautre or cases[2] == symbole) and cases[3] == "." and (cases[4] == symbole or cases[4] == symboleautre ) and cases[5] == "." and (cases[6] == symboleautre or cases[6] == symbole)  and cases[7] == "." and cases[8] == ".":
        choice = "4"

    else: choice = input("afgag")
    return str(choice)
def bot_difficulte2(cases : list,joueur :int):
    choice : str
    choice = ""
    #Lignes 1-2-3
    if cases[7-1] == cases[4-1] and not cases[7-1] == "." and cases[1-1] == "." :
        choice = "1"
    elif cases[8-1] == cases[5-1] and not cases[5-1] == "." and cases[2-1] == ".":
        choice = "2"
    elif cases[9-1] == cases[6-1] and not cases[6-1] == "." and cases[3-1] == ".":
        choice = "3"
    #Lignes 4-5-6
    elif cases[7-1] == cases[1-1] and not cases[1-1] == "." and cases[4-1] == ".":
        choice = "4"
    elif cases[8-1] == cases[2-1] and not cases[2-1] == "." and cases[5-1] == ".":
        choice = "5"
    elif cases[9-1] == cases[3-1] and not cases[3-1] == "." and cases[6-1] == ".":
        choice = "6"
    #Lignes 7-8-9
    elif cases[4-1] == cases[1-1] and not cases[1-1] == "." and cases[7-1] == ".":
        choice = "7"
    elif cases[5-1] == cases[2-1] and not cases[5-1] == "." and cases[8-1] == ".":
        choice = "8"
    elif cases[3-1] == cases[6-1] and not cases[6-1] == "." and cases[9-1] == ".":
        choice = "9"
    #Colonnes 8-5-2
    elif cases[7-1] == cases[9-1] and not cases[7-1] == "." and cases[8-1] == ".":
        choice = "8"
    elif cases[6-1] == cases[4-1] and not cases[6-1] == "." and cases[5-1] == ".":
        choice = "5"
    elif cases[3-1] == cases[1-1] and not cases[3-1] == "." and cases[2-1] == ".":
        choice = "2"
    #Colonnes 7-4-1
    elif cases[8-1] == cases[9-1] and not cases[9-1] == "." and cases[7-1] == ".":
        choice = "7"
    elif cases[6-1] == cases[5-1] and not cases[5-1] == "." and cases[4-1] == ".":
        choice = "4"
    elif cases[2-1] == cases[3-1] and not cases[2-1] == "." and cases[1-1] == ".":
        choice = "1"
    #Colonnes 9-6-3
    elif cases[7-1] == cases[8-1] and not cases[8-1] == "." and cases[9-1] == ".":
        choice = "9"
    elif cases[4-1] == cases[5-1] and not cases[5-1] == "." and cases[6-1] == ".":
        choice = "6"
    elif cases[1-1] == cases[2-1] and not cases[2-1] == "." and cases[3-1] == ".":
        choice = "3"
    #Diagonales 7-5-3
    elif cases[7-1] == cases[5-1] and not cases[5-1] == "." and cases[3-1] == ".":
        choice = "3"
    elif cases[7-1] == cases[3-1] and not cases[3-1] == "." and cases[5-1] == ".":
        choice = "5"
    elif cases[5-1] == cases[3-1] and not cases[3-1] == "." and cases[7-1] == ".":
        choice = "7"
    #Diagonales 1-5-9
    elif cases[9-1] == cases[5-1] and not cases[5-1] == "." and cases[1-1] == ".":
        choice = "1"
    elif cases[9-1] == cases[1-1] and not cases[1-1] == "." and cases[5-1] == ".":
        choice = "5"
    elif cases[5-1] == cases[1-1] and not cases[1-1] == "." and cases[9-1] == ".":
        choice = "9"

    else: choice = str(random.randint(1,9))
    return str(choice)
def bot(cases : list, difficulté : int,joueur):
    choice : str
    difficulté : int
    W  = '\033[0m'  # white (normal)
    B  = '\033[94m' # blue
    if difficulté == 1:
        choice = str(random.randint(1,9))
    elif difficulté == 2:
        choice = bot_difficulte2(cases,joueur)
    elif difficulté == 3:
        choice = bot_difficulte3(cases,joueur)
    return str(choice)

#----------------------------------------
#Lance la partie de morpion et retourne le vainqueur de la partie
#
#Entrée : j1_name : str, j2_name : str
#
#Sortie : str
#----------------------------------------
def LaunchGame_morpion(j1_name : str, j2_name : str, nb_joueurs : int,difficulté : int)->str:

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
            print(nb_joueurs)
            if nb_joueurs == 2:
                if(turn == 1): choice = str(input(B + j1_name + W + " choisissez votre case en suivant le schéma ci dessus : "))
                else : choice = str(input(R + j2_name + W + " choisissez votre case en suivant le schéma ci dessus : "))
            elif nb_joueurs == 1:
                if(turn == 1): choice = str(input(B + j1_name + W + " choisissez votre case en suivant le schéma ci dessus : "))
                else: choice = bot(cases,difficulté,turn)
            elif nb_joueurs == 0:
                if(turn == 1): choice = bot(cases,difficulté,turn)
                else: choice = bot(cases,2,turn)
            #vérifie la valeur de l'utilisateur
            if(not choice.isdigit()):print("Valeur impossible")
            elif(int(choice) < 1 or int(choice) > 9):print("Valeur impossible")
            elif(cases[int(choice) - 1] == "."): choiceIsOk = True
            else: print("Cette case est occupée")


        #ajoute le symbole dans la case souhaité
        if(turn == 1):cases[int(choice) - 1] = "X"
        elif(turn == 2):cases[int(choice) - 1] = "O"

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