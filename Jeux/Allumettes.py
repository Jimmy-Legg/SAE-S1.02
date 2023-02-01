import os
import random
import time

def __afficherFin(winner: str, couleur: str):
    """Fonction qui affiche l'ecran de fin

    Arguments :
        nom du gagnant : str
        couleur du gagnant : str

    Retour : rien

    Private : Cette fonction n'est utile que pour ce script
    """
    W  = '\033[0m'  # white (normal)

    os.system("cls")
    print("---------------------")
    print("")
    print(couleur + winner + W + " a gagné la manche")
    print("")
    print("---------------------")

def __getAmountbot(bot : str,table : list[str], dif : int,C : str):
    """Fonction fait jouer les bot en fonction de la difficulté

    Arguments :
        nom du bot : str
        liste des allumettes : list[str]
        difficulté: int
        couleur du bot :str

    Retour : le choix du bot

    Private : Cette fonction n'est utile que pour ce script
    """
    mot : str
    _i : int
    choix : int
    perdu : int

    W  = '\033[0m'  # white (normal)

    mot = ""
    perdu = 4
    choix = 1

    os.system("cls")
    print("---------------------")
    print("")
    for _i in range(0, len(table)):
        if(table[_i] == "|"): mot += " |"
        else: mot += "  "
    print(mot)
    print("")
    print("---------------------")
    print("")
    print(C + bot  + W + " choisi un nombre...")
    time.sleep(0.5)
    choices = [1,2,3,2,1,2,3,2,1,2,3,2,1,2,3,2,1,2,3]
    if dif == 1:
        choix = random.randint(1, 3)
    elif dif == 2:
        choix = choices[len(table) - 2]
    elif dif == 3:
        choix = choices[len(table) - 2]
        if random.randint(1, 4) == 1:
            choix = random.randint(1, 3)

    print("il choisi : " + str(choix))
    time.sleep(.65)
    return int(choix)


def __getAmount(table : list[str], j_name : str, couleur :str)->int:
    """Fonction qui affiche le jeu et verifie que la valeur entré par l'utilisateur est bonne

    Arguments :
        table : list[str]
        nom du joueur : str
        couleur: str

    Retour : le choix de la personne

    Private : Cette fonction n'est utile que pour ce script
    """
    mot : str
    _i : int
    choix = str

    W  = '\033[0m'  # white (normal)
    R = '\033[91m' # red

    choix = "0"
    while not choix.isdigit() or int(choix) < 1 or int(choix) > 3:

        mot = ""
        os.system("cls")

        print("---------------------")
        print("")

        for _i in range(0, len(table)):

            if(table[_i] == "|"): mot += " |"
            else: mot += "  "

        print(mot)
        print("")
        print("---------------------")
        print("")

        print("Tour de " + couleur +  j_name + W + ", Choix restants : ")

        print("")

        choix = input("Entrez le nombre d'allumettes à enlever : (1-3) : ")

        if(not choix.isdigit()):

            print(R + "Valeur impossible" + W)
            os.system("pause")

        elif(int(choix) < 1 or int(choix) > 3):

            print(R + "Choisissez un nombre entre 1 et 3 !" + W)
            os.system("pause")

    return int(choix)


def __changeTurn(turn : int)->int:
    """Fonction qui change qui joue

    Arguments :
        toure 1 ou 2 : int

    Retour : turn : int

    Private : Cette fonction n'est utile que pour ce script
    """
    if(turn == 1): turn = 2
    else: turn = 1
    return turn


def LaunchGame_allumettes(j1_name : str, j2_name : str,nb_humans : int, difficulty : list[int]):
    """Fonction lance le jeu d'allumette avec le nombre de bot choisi

    Arguments :
        Nom du joueur 1 : str
        Nom du joueur 2 : str
        Nombre d'humains : int
        difficulté : list[int]

    Retour : personne qui gagne

    Private : Cette fonction n'est utile que pour ce script
    """
    turn : int
    nb_allumettes : int
    amount : int

    table : list[str]

    nb_allumettes = 20
    turn = random.randint(1,2)

    table = []

    for _i in range(0, nb_allumettes):
        table.append("|")

    B = '\033[94m' # blue
    R = '\033[91m' # red

    while True:
        print("ok")
        if nb_humans == 2:
            if(turn == 1): amount = __getAmount(table, j1_name, B)
            else: amount = __getAmount(table, j2_name, R)
        elif nb_humans == 1:
            print("ko")
            if(turn == 1): amount = __getAmount(table, j1_name, B)
            else: amount = __getAmountbot(j2_name,table,difficulty[1],R)
        elif nb_humans == 0:
            if(turn == 1): amount = __getAmountbot(j1_name,table,int(difficulty[0]),B)
            else: amount = __getAmountbot(j2_name,table,int(difficulty[1]),R)
        for _i in range(0, amount):
            if(len(table) >= 1):
                table.remove("|")

        if(len(table)<=1): break
        else: turn = __changeTurn(turn)

    if(len(table) == 1):
        if(turn == 2): #pyright: reportUnnecessaryComparison=false
            __afficherFin(j2_name, R)
            winner = j2_name
        else:
            __afficherFin(j1_name, B)
            winner = j1_name
    else:
        if(turn == 2): #pyright: reportUnnecessaryComparison=false
            __afficherFin(j1_name, B)
            winner = j1_name
        else:
            __afficherFin(j2_name, R)
            winner = j2_name

    os.system("pause")

    return winner