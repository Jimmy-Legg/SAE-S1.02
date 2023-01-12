import os
import random
import time


def __couleur(symbole : str, index : int, winCases: list[int])->str:
    """Fonction qui va retourner la couleur d'un symbole en fonction de son identité et de s'il est une case gagnantes.

    Arguments :
        Symbole : str
        Index : int (numéro de la case)
        Cases gagnantes : list[int]

    Retour : Code couleur associé : str

    Private : Cette fonction n'est utile que pour ce script
    """

    W  = '\033[0m'  # white (normal)
    R  = '\033[91m' # red
    B  = '\033[94m' # blue
    G  = '\033[92m' # green

    if(index in winCases): return G
    elif(symbole == "0"): return B
    elif(symbole == "O"): return R
    else: return W

def __changeTurn(turn : int)->int:
    """Fonction qui va regarder le tour actuel et retourner la valeur du tour suivant

    Arguments :
        Tour : int (soit 1 soit 2)

    Retour : Tour suivant : int (soit 1 soit 2)

    Private : Cette fonction n'est utile que pour ce script
    """
    if(turn == 1): turn = 2
    else: turn = 1
    return turn

def __checkWin(cases : list[list[str]])->list[int]:
    """Fonction qui va regarder si il y a une victoire puis retourner les cases gagnantes si victoire il y a

    Arguments :
        Cases : list[list[str]]

    Retour : Cases gagnantes : list[int]

    Private : Cette fonction n'est utile que pour ce script
    """
    winCases : list[int]

    winCases = []

    for i in range(0,4):
        for j in range(6,2,-1):
            if (cases[i][j] == cases[i+1][j-1] and cases[i+1][j-1] == cases[i+2][j-2] and cases[i+2][j-2] == cases[i+3][j-3] and not cases[i+1][j-1] == "."):

                winCases.append(i * 7 + j)
                winCases.append((i+1) * 7 + j-1)
                winCases.append((i+2) * 7 + j-2)
                winCases.append((i+3) * 7 + j-3)

    for i in range(0,4):
        for j in range(0,7):
            if (cases[j][i] == cases[j][i+1] and cases[j][i+1] == cases[j][i+2] and cases[j][i+2] == cases[j][i+3] and not cases[j][i] == "."):

                winCases.append(j * 7 + i)
                winCases.append(j * 7 + i+1)
                winCases.append(j * 7 + i+2)
                winCases.append(j * 7 + i+3)

    for i in range(0,4):
        for j in range(0,7):
            if (cases[i][j] == cases[i+1][j] and cases[i+1][j] == cases [i+2][j] and cases[i+2][j] == cases[i+3][j] ) and (not cases[i][j] == "." and not cases[i+1][j] == "." and not cases[i+2][j] == "." and not cases[i+3][j] == "."):

                winCases.append(i * 7 + j)
                winCases.append((i+1) * 7 + j)
                winCases.append((i+2) * 7 + j)
                winCases.append((i+3) * 7 + j)

    for i in range(0,4):
        for j in range(0,4):
            if ((cases[i][j] == cases[i+1][j+1] and cases[i+1][j+1] == cases [i+2][j+2] and cases[i+2][j+2] == cases[i+3][j+3]) and (not cases[i][j] == "." and not cases[i+1][j+1] == "." and not cases[i+2][j+2] == "." and not cases[i+3][j+3] == ".")):

                winCases.append(i * 7 + j)
                winCases.append((i+1) * 7 + j+1)
                winCases.append((i+2) * 7 + j+2)
                winCases.append((i+3) * 7 + j+3)

    return winCases

def __afficherMenu(cases : list[list[str]], winCases : list[int]):
    """Procédure qui va afficher l'interface de jeu

    Arguments :
        Cases : list[int]
        Cases gagnantes : list[int]

    Retour : affichage

    Private : Cette fonction n'est utile que pour ce script
    """

    W  = '\033[0m'  # white (normal)

    os.system("cls")
    print("---------------------------------------------")
    print("Schéma :")
    print("          " + __couleur(cases[0][0], 0, winCases) + cases[0][0] + W + " | " + __couleur(cases[0][1], 1, winCases) + cases[0][1] + W + " | " + __couleur(cases[0][2], 2, winCases) + cases[0][2] + W + " | " + __couleur(cases[0][3], 3, winCases) + cases[0][3] + W + " | " + __couleur(cases[0][4], 4, winCases) + cases[0][4] + W + " | " + __couleur(cases[0][5], 5, winCases) + cases[0][5] + W +  " | " + __couleur(cases[0][6], 6, winCases) + cases[0][6] + W)
    __afficherPartie(cases, winCases)

def __afficherPartie(cases : list[list[str]], winCases : list[int]):
    """Procédure qui va afficher la partie en cours et colorer les cases en fonction de leur joueur ou de si elles sont gagnantes

    Arguments :
        Cases : list[int]
        Cases gagnantes : list[int]

    Retour : affichage

    Private : Cette fonction n'est utile que pour ce script
    """
    W  = '\033[0m'  # white (normal)

    print("---------------------------------------------")
    print("Partie :")

    for i in range(1,7):
        print("          " + __couleur(cases[i][0], i*7, winCases) + cases[i][0] + W + " | " + __couleur(cases[i][1], i*7+1, winCases) + cases[i][1] + W + " | " + __couleur(cases[i][2], i*7+2, winCases) + cases[i][2] + W + " | " + __couleur(cases[i][3], i*7+3, winCases) + cases[i][3] + W + " | " + __couleur(cases[i][4], i*7+4, winCases) + cases[i][4] + W + " | " + __couleur(cases[i][5], i*7+5, winCases) + cases[i][5] + W +  " | " + __couleur(cases[i][6], i*7+6, winCases) + cases[i][6] + W)

    print("---------------------------------------------")

def __completeFourLine(cases : list[list[str]], symbol : str)->int:
    """Fonction qui va regarder si le joueur peut gagner et retourne le choix gagnant s'il existe, sinon retourne 0

    Arguments :
        Cases : list[int]
        Symbole du joueur : str

    Retour : choix : int

    Private : Cette fonction n'est utile que pour ce script
    """
    #i : lines ; j : columns

    #check the possibility to win with verticals lines
    for i in range(1,4):
        for j in range(0,7):

            canPut = 0
            isPut = 0

            if(cases[i][j] == symbol): isPut += 1
            elif(cases[i][j] == "." and (cases[i+1][j] != ".")):canPut += 1

            if(cases[i+1][j] == symbol): isPut += 1
            elif(cases[i+1][j] == "." and (cases[i+2][j] != ".")):canPut += 1

            if(cases[i+2][j] == symbol): isPut += 1
            elif(cases[i+2][j] == "." and (cases[i+3][j] != ".")):canPut += 1

            if(cases[i+3][j] == symbol): isPut += 1
            elif(cases[i+3][j] == "." and (i+3 == 6 or cases[i+4][j] != ".")):canPut += 1

            if(isPut == 3 and canPut == 1):
                return j+1

    #check the possibility to win with horizontals lines
    for i in range(1,7):
        for j in range(0,4):

            canPut = 0
            isPut = 0
            choice = 0

            if(cases[i][j] == symbol): isPut += 1
            elif(cases[i][j] == "." and (i == 6 or cases[i+1][j] != ".")):
                canPut += 1
                choice = j+1

            if(cases[i][j+1] == symbol): isPut += 1
            elif(cases[i][j+1] == "." and (i == 6 or cases[i+1][j+1] != ".")):
                canPut += 1
                choice = j+2

            if(cases[i][j+2] == symbol): isPut += 1
            elif(cases[i][j+2] == "." and (i == 6 or cases[i+1][j+2] != ".")):
                canPut += 1
                choice = j+3

            if(cases[i][j+3] == symbol): isPut += 1
            elif(cases[i][j+3] == "." and (i == 6 or cases[i+1][j+3] != ".")):
                canPut += 1
                choice = j+4

            if(isPut == 3 and canPut == 1):
                return choice

    #check the possibility to win with descendant diagonals
    for i in range(1,4):
        for j in range(0,4):

            canPut = 0
            isPut = 0
            choice = 0

            if(cases[i][j] == symbol): isPut += 1
            elif(cases[i][j] == "." and (cases[i+1][j] != ".")):
                canPut += 1
                choice = j+1

            if(cases[i+1][j+1] == symbol): isPut += 1
            elif(cases[i+1][j+1] == "." and (cases[i+2][j+1] != ".")):
                canPut += 1
                choice = j+2

            if(cases[i+2][j+2] == symbol): isPut += 1
            elif(cases[i+2][j+2] == "." and (cases[i+3][j+2] != ".")):
                canPut += 1
                choice = j+3

            if(cases[i+3][j+3] == symbol): isPut += 1
            elif(cases[i+3][j+3] == "." and (i == 3 or cases[i+4][j+3] != ".")):
                canPut += 1
                choice = j+4

            if(isPut == 3 and canPut == 1):
                return choice

    #check the possibility to win with ascendant diagonals
    for i in range(4,7):
        for j in range(0,4):

            canPut = 0
            isPut = 0
            choice = 0

            if(cases[i][j] == symbol): isPut += 1
            elif(cases[i][j] == "." and (i == 6 or cases[i+1][j] != ".")):
                canPut += 1
                choice = j+1

            if(cases[i-1][j+1] == symbol): isPut += 1
            elif(cases[i-1][j+1] == "." and (cases[i][j+1] != ".")):
                canPut += 1
                choice = j+2

            if(cases[i-2][j+2] == symbol): isPut += 1
            elif(cases[i-2][j+2] == "." and (cases[i-1][j+2] != ".")):
                canPut += 1
                choice = j+3

            if(cases[i-3][j+3] == symbol): isPut += 1
            elif(cases[i-3][j+3] == "." and (cases[i-2][j+3] != ".")):
                canPut += 1
                choice = j+4

            if(isPut == 3 and canPut == 1 ):
                return choice

    return 0

def __completeWiningMove(cases : list[list[str]], symbol : str)->int:
    """Fonction qui va regarder si un coup gagnant (c'est a dire un coup qui entraine une victoire sur le tour suivant, soit la création de deux lignes de 3 qui peuvent être complétée au tour suivant) est faisable et le retourne s'il existe, sinon retourne 0

    Arguments :
        Cases : list[int]
        Symbole du joueur : str

    Retour : choix : int

    Private : Cette fonction n'est utile que pour ce script
    """
    #check the possibility to win with horizontals lines
    for i in range(1,7):
        for j in range(1,4):

            canPut = 0
            isPut = 0
            choice = 0

            if(cases[i][j] == symbol): isPut += 1
            elif(cases[i][j] == "." and (i == 6 or cases[i+1][j] != ".")):
                canPut += 1
                choice = j+1

            if(cases[i][j+1] == symbol): isPut += 1
            elif(cases[i][j+1] == "." and (i == 6 or cases[i+1][j+1] != ".")):
                canPut += 1
                choice = j+2

            if(cases[i][j+2] == symbol): isPut += 1
            elif(cases[i][j+2] == "." and (i == 6 or cases[i+1][j+2] != ".")):
                canPut += 1
                choice = j+3

            if(cases[i][j+3] == "." and (i == 6 or cases[i+1][j+3] != ".")):
                canPut += 1

            if(cases[i][j-1] == "." and (i == 6 or cases[i+1][j-1] != ".")):
                canPut += 1

            if(isPut == 2 and canPut == 3):
                return choice

    #check the possibility to win with descendant diagonals
    for i in range(2,4):
        for j in range(1,4):

            canPut = 0
            isPut = 0
            choice = 0

            if(cases[i][j] == symbol): isPut += 1
            elif(cases[i][j] == "." and (cases[i+1][j] != ".")):
                canPut += 1
                choice = j+1

            if(cases[i+1][j+1] == symbol): isPut += 1
            elif(cases[i+1][j+1] == "." and (cases[i+2][j+1] != ".")):
                canPut += 1
                choice = j+2

            if(cases[i+2][j+2] == symbol): isPut += 1
            elif(cases[i+2][j+2] == "." and (cases[i+3][j+2] != ".")):
                canPut += 1
                choice = j+3

            if(cases[i-1][j-1] == "." and (cases[i][j-1] != ".")):
                canPut += 1

            if(cases[i+3][j+3] == "." and (i == 3 or cases[i+4][j+3] != ".")):
                canPut += 1

            if(isPut == 2 and canPut == 3):
                return choice

    #check the possibility to win with ascendant diagonals
    for i in range(4,6):
        for j in range(1,4):

            canPut = 0
            isPut = 0
            choice = 0

            if(cases[i][j] == symbol): isPut += 1
            elif(cases[i][j] == "." and (cases[i+1][j] != ".")):
                canPut += 1
                choice = j+1

            if(cases[i-1][j+1] == symbol): isPut += 1
            elif(cases[i-1][j+1] == "." and (cases[i][j+1] != ".")):
                canPut += 1
                choice = j+2

            if(cases[i-2][j+2] == symbol): isPut += 1
            elif(cases[i-2][j+2] == "." and (cases[i-1][j+2] != ".")):
                canPut += 1
                choice = j+3

            if(cases[i+1][j-1] == "." and (i == 5 or cases[i+2][j-1] != ".")):
                canPut += 1

            if(cases[i-3][j+3] == "." and (cases[i-2][j+3] != ".")):
                canPut += 1

            if(isPut == 2 and canPut == 3):
                return choice
    return 0

def __tryMenace(cases : list[list[str]], line : int, column : int, symbol : str)->int:
    """Regarde si un coup est possible pour un joueur qui permettrait de menacer de gagner en placant un autre pion sur une case donnée
    En d'autres termes : regarde si il est possible de faire des lignes de 3 pions autour d'une case donnée, case donnée non-comprise
    Retourne le choix s'il existe sinon retourne 0

    Arguments :
        Cases : list[int]
        Ligne : int (entre 1 et 6, 6 étant celle du bas)
        Colonne : int (entre 0 et 6, 6 étant celle de droite)
        Symbole du joueur : str

    Retour : choix : int

    Private : Cette fonction n'est utile que pour ce script
    """
    if(cases[line][column]!="."): return 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            isPut = 0
            canPut = 0
            for y in range(1, 4):
                if(i != 0 or j != 0):
                    if(line + i*y > 0 and line + i*y < 7 and column + j*y >= 0 and column + j*y < 7):
                        if(cases[line + i*y][column + j*y] == symbol): isPut += 1
                        elif((line + i*y == 6 or cases[line + i*y + 1][column + j*y] != ".") and cases[line + i*y][column + j*y] == "."):
                            canPut += 1
                            choice = column + j*y + 1

            if(isPut == 2 and canPut == 1):
                return choice
    return 0

def __completeWinningPattern(cases : list[list[str]], mySymbol : str, oponentSymbol : str)->int:
    """Fonction qui va regarder si un "patern gagnant" (deux coup gagnant sur des lignes consécutives et sur une même colonne) est faisable et le retourne s'il existe, sinon retourne 0

    Arguments :
        Cases : list[int]
        Symbole du joueur : str
        Symbole de l'adversaire : str

    Retour : choix : int

    Private : Cette fonction n'est utile que pour ce script
    """
    choice = 0
    for i in range(1,7):
        for j in range(0,7):
            if(__isThisCaseWinnable(cases, i, j, mySymbol)):
                if(i > 1): choice = __tryMenace(cases, i-1, j, mySymbol)
                if(choice == 0 and i < 6 and cases[i+1][j] == "."): choice = __tryMenace(cases, i+1, j, mySymbol)
                if(choice != 0 and not __isASuicideMove(cases, choice, oponentSymbol)): return choice
    return 0

def __makeAThreeLine(cases : list[list[str]], symbol : str, oponentSymbol : str)->int:
    """Fonction qui va regarder si une ligne de trois symbole est possible et si elle n'est pas un coup perdant et retourner le choix en question s'il existe, sinon retourne 0

    Arguments :
        Cases : list[int]
        Symbole du joueur : str
        Symbole de l'adversaire : str

    Retour : choix : int

    Private : Cette fonction n'est utile que pour ce script
    """
    choice = 0
    for i in range(1,7):
        for j in range(0,7):
            choice = __tryMenace(cases, i, j, symbol)
            if(choice != 0 and not __isASuicideMove(cases, choice, oponentSymbol)): return choice
    return 0

def __isASuicideMove(cases : list[list[str]], choice : int, oponentSymbol : str)->bool:
    """Fonction qui va regarder si un choix est perdant pour un joueur donné

    Arguments :
        Cases : list[int]
        Choix : int
        Symbole de l'adversaire : str

    Retour : isAsuicideMoove : bool

    Private : Cette fonction n'est utile que pour ce script
    """
    column = choice - 1

    #trouve la ligne associée
    line = 6
    choiceIsOk = False
    while not choiceIsOk:

        if(line <= 0):
            print("error")
            os.system("pause")
            return False

        elif(cases[line][int(column)] == "0" or cases[line][int(column)] == "O"):
            line -= 1

        else: choiceIsOk = True

    if(line > 1):

        #check si c'est un suicide par diagonales ascendantes
        for j in range(-3,1):

            isPut = 0

            if(line - 1 - j < 7 and column + j >= 0 and cases[line - 1 - j][column + j] == oponentSymbol): isPut += 1

            if(line - 1 - j - 1 > 0 and line - 1 - j - 1 < 7 and column + j + 1 >= 0 and column + j + 1 < 7 and cases[line - 1 - j - 1][column + j + 1] == oponentSymbol): isPut += 1

            if(line - 1 - j - 2 > 0 and line - 1 - j - 2 < 7 and column + j + 2 >= 0 and column + j + 2 < 7 and cases[line - 1 - j - 2][column + j + 2] == oponentSymbol): isPut += 1

            if(line - 1 - j - 3 > 0 and column + j + 3 < 7 and cases[line - 1 - j - 3][column + j + 3] == oponentSymbol): isPut += 1

            if(isPut == 3):
                return True

        #check si c'est un suicide par ligne diagonale descendante
        for j in range(-3,1):
            isPut = 0

            if(line - 1 + j > 0 and column + j >= 0 and cases[line - 1 + j][column + j] == oponentSymbol): isPut += 1
            if(line - 1 + j + 1 < 7 and line - 1 + j + 2 > 0 and column + j + 1 >= 0 and column + j + 1 < 7 and cases[line - 1 + j + 1][column + j + 1] == oponentSymbol): isPut += 1
            if(line - 1 + j + 2 < 7 and line - 1 + j + 2 > 0 and column + j + 2 >= 0 and column + j + 2 < 7 and cases[line - 1 + j + 2][column + j + 2] == oponentSymbol): isPut += 1
            if(line - 1 + j + 3 < 7 and column + j + 3 < 7 and cases[line - 1 + j + 3][column + j + 3] == oponentSymbol): isPut += 1

            if(isPut == 3):

                return True

        #check si c'est un suicide par ligne horizontale
        for j in range(-3,1):
            isPut = 0

            if(column + j >= 0 and cases[line - 1][column + j] == oponentSymbol): isPut += 1

            if(column + j + 2 >= 0 and column + j + 1 < 7 and cases[line - 1][column + j + 1] == oponentSymbol): isPut += 1

            if(column + j + 2 >= 0 and column + j + 2 < 7 and cases[line - 1][column + j + 2] == oponentSymbol): isPut += 1

            if(column + j + 3 < 7 and cases[line - 1][column + j + 3] == oponentSymbol): isPut += 1


            if(isPut == 3):
                return True

    return False

def __isThisCaseWinnable(cases : list[list[str]], line : int, column : int, symbol : str)->bool:
    """Fonction qui va regarder si une case donnée est gagante pour un joueur donné

    Arguments :
        Cases : list[int]
        Ligne : int (entre 1 et 6, 6 étant celle du bas)
        Colonne : int (entre 0 et 6, 6 étant celle du droite)
        Symbole du joueur : str

    Retour : Case gagnante : bool

    Private : Cette fonction n'est utile que pour ce script
    """
    if(cases[line][column] != "."): return False
    for i in range(-1, 2):
        for j in range(-1, 2):
            isPut = 0
            for y in range(1, 4):
                if(i != 0 or j != 0):
                    if(line + i*y > 0 and line + i*y < 7 and column + j*y >= 0 and column + j*y < 7):
                        if(cases[line + i*y][column + j*y] == symbol): isPut += 1

            if(isPut == 3): return True
    return False

def __hasAWinningColumn(cases : list[list[str]], symbol : str, oponentSymbol : str)->int:
    """Fonction qui va regarder si le joueur possède une "colonne gagnante" (c'est a dire une colonne où le joueur peut gagner sur deux lignes consécutives) et retourne cette colonne

    Arguments :
        Cases : list[int]
        Symbole du joueur : str
        Symbole de l'adversaire : str

    Retour : colonne : int (entre 1 et 7, 7 étant celle du droite)

    Private : Cette fonction n'est utile que pour ce script
    """
    for j in range(0,7):
        for i in range(6, 1, -1):
            if(cases[i][j] == "." and __isThisCaseWinnable(cases, i, j, symbol) and cases[i+1][j] == "." and __isThisCaseWinnable(cases, i+1, j, symbol) and not __isASuicideMove(cases, j, oponentSymbol)):
                return j+1
    return 0

def __isMovePossible(cases : list[list[str]], choice : int)->bool:
    """Fonction qui va regarder si un pion est placable sur la colonne désignée

    Arguments :
        Cases : list[int]
        choice : int (doit être entre 1 et 7)

    Retour : isMovePossible : int

    Private : Cette fonction n'est utile que pour ce script
    """
    column = choice - 1

    #trouve la ligne associée
    line = 6
    choiceIsOk = False
    while not choiceIsOk:

        if(line <= 0):
            return False

        elif(cases[line][int(column)] == "0" or cases[line][int(column)] == "O"):
            line -= 1

        else: choiceIsOk = True
    return True

def __putRandom(cases : list[list[str]], oponentSymbol : str)->int:
    """Fonction qui va choisir une colonne au hasard en évitant les colonnes perdantes ou impossibles

    Arguments :
        Cases : list[int]
        Symbole de l'adversaire

    Retour : choix : int (entre 1 et 7)

    Private : Cette fonction n'est utile que pour ce script
    """
    l1 : list[int]
    l2 : list[int]
    choices : list[int]

    l1 = [3,4,5]
    l2 = [1,2,6,7]
    random.shuffle(l1)
    random.shuffle(l2)
    choices = l1 + l2

    for choice in choices:
        if(__isMovePossible(cases, choice) and not __isASuicideMove(cases, choice, oponentSymbol)): return choice

    return choice

def __askForIAAction(cases : list[list[str]], mySymbol : str, oponentSymbol : str, difficulty : int)->list[int]:
    """Fonction qui génère le choix d'un bot en fonction de sa difficulté et de la partie en cours

    Arguments :
        Cases : list[int]
        Symbole du bot : str
        Symbole de l'adversaire : str
        Difficulté du bot : int

    Retour : choix du joueur (sous forme [colonne, ligne], avec colonne entre 1 et 6 et ligne entre 1 et 7) : list[int]

    Private : Cette fonction n'est utile que pour ce script
    """

    choice:int

    if(difficulty == 1):
        choice = __completeFourLine(cases, mySymbol)
        if(choice == 0):choice = __completeFourLine(cases, oponentSymbol)
        if(choice == 0): choice = random.randint(1,7)

    if(difficulty == 2):
        choice = __completeFourLine(cases, mySymbol)
        if(choice == 0):choice = __completeFourLine(cases, oponentSymbol)
        if(choice == 0): choice = __completeWiningMove(cases, mySymbol)
        if(choice == 0): choice = __completeWiningMove(cases, oponentSymbol)
        if(choice == 0): choice = __putRandom(cases, oponentSymbol)

    if(difficulty == 3):
        choice = __completeFourLine(cases, mySymbol)
        if(choice == 0):choice = __completeFourLine(cases, oponentSymbol)
        if(choice == 0): choice = __completeWiningMove(cases, mySymbol)
        if(choice == 0): choice = __completeWiningMove(cases, oponentSymbol)
        if(choice == 0): choice = __hasAWinningColumn(cases, mySymbol, oponentSymbol)
        if(choice == 0): choice = __completeWinningPattern(cases, oponentSymbol, mySymbol)
        if(choice == 0): choice = __completeWinningPattern(cases, mySymbol, oponentSymbol)
        if(choice == 0): choice = __makeAThreeLine(cases, mySymbol, oponentSymbol)
        if(choice == 0): choice = __makeAThreeLine(cases, oponentSymbol, mySymbol)
        if(choice == 0): choice = __putRandom(cases, oponentSymbol)

    if(difficulty == 4):
        choice = __makeAThreeLine(cases, mySymbol, oponentSymbol)
        if(choice == 0): choice = int(input("Choix du bot : "))
        

    lignes = 6
    choiceIsOk = False
    while not choiceIsOk:

        if(lignes <= 0):
            return []

        elif(cases[lignes][int(choice) - 1] == "0" or cases[lignes][int(choice) - 1] == "O"):
            lignes -= 1
        else: choiceIsOk = True

    return [choice, lignes]


def __askForPlayerAction(cases : list[list[str]], j_name : str, couleur : str)->list[int]:
    """Fonction qui demande a l'utilisateur d'entrer dans quelle colonne il veut placer son pion, si l'entrée n'est pas bonne le lui redemande

    Arguments :
        Cases : list[int]
        Nom du joueur : str
        Code couleur associé au joueur : str

    Retour : choix du joueur sous forme (sous forme [colonne, ligne], avec colonne entre 1 et 6 et ligne entre 1 et 7) : list[int]

    Private : Cette fonction n'est utile que pour ce script
    """

    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)

    choiceIsOk : bool
    choiceIsOk = False
    lignes : int
    choice : str

    while not choiceIsOk:

        #demande le choix de l'utilisateur
        choice = str(input(couleur + j_name + W + " choisissez votre case en suivant le schéma ci dessus : "))

        #vérifie la valeur de l'utilisateur

        if(not choice.isdigit()):
            print(R + "Valeur impossible !" + W)
            os.system("pause")
            return []

        elif(int(choice) < 1 or int(choice) > 7):
            print(R + "La colonne n'existe pas !" + W)
            os.system("pause")
            return []

        else:

            lignes = 6
            while not choiceIsOk:

                if(lignes <= 0):
                    print(R + "La colonne est pleine !" + W)
                    os.system("pause")
                    return []

                elif(cases[lignes][int(choice) - 1] == "0" or cases[lignes][int(choice) - 1] == "O"):
                    lignes -= 1
                else: choiceIsOk = True

    return[int(choice), lignes] #pyright: reportUnboundVariable=false

def __affichageFin(equality : bool, turn : int, j1_name : str, j2_name : str, cases : list[list[str]], winCases : list[int], humans : int)->str:
    """Fonction qui affiche l'ecran de fin de partie et retourne le gagnant de la partie

    Arguments :
        IsEquality : bool
        Tour : int
        Nom du joueur 1 : str
        Nom du joueur 2 : str
        Cases : list[list[str]]
        Cases gagnantes : list[int]

    Retour : Vainqueur : str (si le joueur est un bot, il ne sera pas renvoyé comme vainqueur afin de ne pas lui ajouter de score)

    Private : Cette fonction n'est utile que pour ce script
    """

    W  = '\033[0m'  # white (normal)
    R  = '\033[91m' # red
    B  = '\033[94m' # blue
    O  = '\033[93m' # yellow

    winner : str

    os.system("cls")

    print("---------------------------------------------")
    print("               " + O + "Partie terminée" + W)
    print("")

    __afficherPartie(cases, winCases)

    if(equality):
        print("égalité !")
        winner = ""
    elif(turn == 2 and not equality):
        print(B + j1_name + W + " a gagné ")
        if(humans > 0): winner = j1_name
        else: winner = ""
    elif(turn == 1 and not equality):
        print(R + j2_name + W + " a gagné ")
        if(humans == 2): winner = j2_name
        else: winner = ""
        print("---------------------------------------------")

    return winner

def LaunchGame_puissance4(j1_name : str, j2_name : str, nb_humans : int, difficulty : list[int])->str:
    """Fonction qui  demande a l’utilisateur le nombre de bots et d’humain et leur difficultés dans le cas d’un bot ou leur nom dans le cas d’un joueur

    Arguments :
        Nom du joueur 1 : str
        Nom du joueur 2 : str
        Nombre de joueurs humains : int
        Difficultés : list[int]

    Retour : Vainqueur : str
    """

    cases : list[list[str]]

    turn : int
    winner : str

    gameFinished : bool
    equality : bool
    lignes : int
    jeton : int

    winCases : list[int]
    listChoices : list[int]

    R  = '\033[91m' # red
    B  = '\033[94m' # blue

    #initialise le tableau

    cases = [["1","2","3","4","5","6","7"],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."]]
    winCases = []

    #intialise les données
    turn = random.randint(1,2)
    gameFinished = False
    equality = False

    lignes = 6
    winner = ""

    #boucle principale

    jeton = 42
    while not gameFinished:

        listChoices = []

        __afficherMenu(cases, winCases)
        time.sleep(0.5)

        while len(listChoices) == 0 :

            #affiche le menu
            __afficherMenu(cases, winCases)

            if(nb_humans == 0):
                if(turn == 1): listChoices = __askForIAAction(cases, "0", "O", difficulty[0])
                else:listChoices = __askForIAAction(cases, "O", "0", difficulty[1])
            elif(nb_humans == 1):
                if(turn == 1): listChoices = __askForPlayerAction(cases, j1_name, B)
                else:listChoices = __askForIAAction(cases, "O", "0", difficulty[1])
            else:
                if(turn == 1): listChoices = __askForPlayerAction(cases, j1_name, B)
                else:listChoices = __askForPlayerAction(cases, j2_name, R)

        choice = listChoices[0]
        lignes = listChoices[1]

        #ajoute le symbole dans la case souhaité
        if(turn == 1):
            cases[lignes][choice - 1] = '0'
            jeton -= 1
        elif(turn == 2):
            cases[lignes][choice - 1] = 'O'
            jeton -= 1

        #Vérification de victoire :
        winCases = __checkWin(cases)
        if(len(winCases) > 0): gameFinished = True

        #Changement de tour :
        turn = __changeTurn(turn)

        #Vérification d'égalité si pas de victoire :
        if(not gameFinished):
            equality = True
            if jeton < 1 :
                equality = True
            else:
                equality = False

            if(equality): gameFinished = True

        #Fin de Partie:
        if(gameFinished):
            winner = __affichageFin(equality, turn, j1_name, j2_name, cases, winCases, nb_humans)

    os.system("pause")
    return winner

