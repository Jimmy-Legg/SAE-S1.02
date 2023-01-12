import os
from typing import Optional
import Jeux.Morpion as Morpion
import Jeux.Allumettes as Allumettes
import Jeux.P4 as P4
import Jeux.Devinette as Devinette
from Classes.Joueur import joueur

def __getJoueurs(fichier : str)->list[joueur]:
    """Récupère dans le fichier donné en entrée les joueurs et en fait un liste

    Arguments :
        Chemin du fichier : str

    Retour : list[joueur]

    Private : Cette fonction n'est utile que pour ce script
    """

    datas : list[str]

    listJoueurs : list[joueur]

    f = open (fichier,"r")
    lines = f.readlines()

    listJoueurs = []

    for _i in range(0,len(lines)):
        datas = lines[_i].split()
        if(len(datas)==5):
            j = joueur(str(datas[0]), int(datas[1].split("|")[0]), int(datas[1].split("|")[1]), int(datas[2].split("|")[0]), int(datas[2].split("|")[1]), int(datas[3].split("|")[0]), int(datas[3].split("|")[1]), int(datas[4].split("|")[0]), int(datas[4].split("|")[1]))
            listJoueurs.append(j)
            j.showScoreAllumettes()

    f.close()

    return listJoueurs

def getPlayerData()->list[str]:
    """Demandes les données des joueurs et les retourne sous la forme [nombre de joueurs humains, difficulté du bot 1, nom du bot 1, difficulté du bot 2, nom du bot 2]

    Arguments :
        Aucuns

    Retour : list[str]

    Private : Cette fonction n'est utile que pour ce script
    """

    data : list[str]
    choice : str

    W  = '\033[0m'  # white (normal)
    B  = '\033[94m' # blue
    R  = '\033[91m' # red

    data = []
    choice = ""
    while choice not in ["1","2","3"]:

        os.system("cls")
        print("-----------------------")
        print("      Bienvenue !      ")
        print("                       ")
        print("  1 - Joueur VS Joueur ")
        print("  2 - Joueur VS IA     ")
        print("  3 - IA VS IA         ")
        print("                       ")
        print("-----------------------")
        choice = input("Choisissez qui seront les joueurs : ")

        if(choice == "1") : data.append("2")
        elif(choice == "2") : data.append("1")
        elif(choice == "3") : data.append("0")
        else:
            print(R + "Choix impossible !" + W)
            os.system("pause")

    if(int(data[0])==0):
        choice = ""
        while choice not in ["1","2","3"]:

            os.system("cls")
            print("---------------------")
            print("     Difficulté du bot 1 :")
            print("                     ")
            print("  1 - Facile         ")
            print("  2 - Moyen          ")
            print("  3 - Difficile      ")
            print("                     ")
            print("---------------------")
            choice = input("Choisissez la difficulté : ")
            if(choice == "1") : data.append("1")
            elif(choice == "2") : data.append("2")
            elif(choice == "3") : data.append("3")
            else:
                print(R + "Choix impossible !" + W)
                os.system("pause")

        os.system("cls")
        if(data[0] == "0"):
            if(data[1] == "1"): data.append("Zamite")
            if(data[1] == "2"): data.append("Rajang")
            if(data[1] == "3"): data.append("Kirin")

            print("Le bot 1 s'appellera " + B + data[2] + W)
            os.system("pause")
    else:
        os.system("cls")
        data.append("0")
        data.append(input("Choisissez le nom du " + B + "joueur 1" + W + " : "))

    if(int(data[0])<2):

        choice = ""
        while choice not in ["1","2","3"]:

            os.system("cls")
            print("---------------------")
            if(data[0]=="1"):print("     Difficulté du bot :")
            else: print("     Difficulté du bot 2 :")
            print("                     ")
            print("  1 - Facile         ")
            print("  2 - Moyen          ")
            print("  3 - Difficile      ")
            print("                     ")
            print("---------------------")
            choice = input("Choisissez la difficulté : ")
            if(choice == "1") : data.append("1")
            elif(choice == "2") : data.append("2")
            elif(choice == "3") : data.append("3")
            else:
                print(R + "Choix impossible !" + W)
                os.system("pause")

        os.system("cls")
        if(data[3] == "1"): data.append("Najarala")
        if(data[3] == "2"): data.append("Akantor")
        if(data[3] == "3"): data.append("Nerscylla")

        if(data[0] == "0"): print("Le bot 2 s'appellera " + R + data[4] + W)
        if(data[0] == "1"): print("Le bot s'appellera " + R + data[4] + W)
        os.system("pause")


    else:
        data.append("0")
        os.system("cls")
        data.append(input("Choisissez le nom du" + R + " joueur 2" + W + " : "))

    return data

def __afficher_profils(j1_name : str, j2_name : str, nb_humans : int, listJoueurs : list[joueur], difficulty : list[int]):
    """Affiche les profils des joueurs actuels

    Arguments :
        Nom du joueur 1 : str
        Nom du joueur 2 : str
        Nombre de joueur humains : int (entre 0 et 2)
        Liste des joueurs : list[joueur]
        Difficulté : list[int] (en position 0 celle du joueur 1 et en position 1 celle du joueur 2)

    Retour : affichage

    Private : Cette fonction n'est utile que pour ce script
    """

    j1 : Optional[joueur]
    j2 : Optional[joueur]

    j1 = None
    j2 = None

    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)
    G  = '\033[92m' # green
    O  = '\033[93m' # yellow

    os.system("cls")

    if(nb_humans == 2):
        i = 0
        while i < len(listJoueurs) and not (j1 != None and j2 != None):
            if(listJoueurs[i].getName() == j1_name): j1 = listJoueurs[i]
            if(listJoueurs[i].getName() == j2_name): j2 = listJoueurs[i]
            i += 1

        if(j1 == None): j1 = joueur(j1_name, 0, 0, 0, 0, 0, 0, 0, 0)
        if(j2 == None): j2 = joueur(j2_name, 0, 0, 0, 0, 0, 0, 0, 0)

        print("--------------------------------------------------------------------")
        print("                             Profils :                              ")
        print("          Joueur 1 :                          Joueur 2 :            ")
        print()
        print(j1_name + (35 - len(j1_name)) * " " + "|  "  + j2_name + (35 - len(j1_name)) * " ")
        print()
        print("Scores :" + 27 * " " + "|  " + "Scores :" + 27 * " ")
        print()

        #afficher score devinette:
        if(j1.getGameDevinette() == 0 and j2.getGameDevinette() == 0):
            print("Devinettes :  " + G + str(j1.getScoreDevinette()) + W + "/" + R + str(j1.getGameDevinette() - j1.getScoreDevinette()) + " " + O + "100%" + W + (21 - (len(str(j1.getScoreDevinette()) + "/" + str(j1.getGameDevinette() - j1.getScoreDevinette())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getScoreDevinette()) + "/" + R + str(j2.getGameDevinette() - j2.getScoreDevinette()) + O + " 100%" + W)
        elif(j1.getGameDevinette() == 0):
            print("Devinettes :  " + G + str(j1.getScoreDevinette()) + W + "/" + R + str(j1.getGameDevinette() - j1.getScoreDevinette()) + " " + O + "100%" + W +  (21 - (len(str(j1.getScoreDevinette()) + "/" + str(j1.getGameDevinette() - j1.getScoreDevinette())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getScoreDevinette()) + "/" + R + str(j2.getGameDevinette() - j2.getScoreDevinette()) + O + " " + str(round((j2.getScoreDevinette()/j2.getGameDevinette()) * 100)) + "%" + W)
        elif(j2.getGameDevinette() == 0):
            print("Devinettes :  " + G + str(j1.getScoreDevinette()) + W + "/" + R + str(j1.getGameDevinette() - j1.getScoreDevinette()) + " " + O + str(round((j1.getScoreDevinette()/j1.getGameDevinette()) * 100)) + "%"  + W + (21 - (len(str(j1.getScoreDevinette()) + "/" + str(j1.getGameDevinette() - j1.getScoreDevinette())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getScoreDevinette()) + "/" + R + str(j2.getGameDevinette() - j2.getScoreDevinette()) + O + " 100%" + W)
        else:
            print("Devinettes :  " + G + str(j1.getScoreDevinette()) + W + "/" + R + str(j1.getGameDevinette() - j1.getScoreDevinette()) + " " + O + str(round((j1.getScoreDevinette()/j1.getGameDevinette()) * 100)) + "%"  + W + (21 - (len(str(j1.getScoreDevinette()) + "/" + str(j1.getGameDevinette() - j1.getScoreDevinette())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getScoreDevinette()) + "/" + R + str(j2.getGameDevinette() - j2.getScoreDevinette()) + " " + O + str(round((j2.getScoreDevinette()/j2.getGameDevinette()) * 100)) + "%" + W)

        #afficher score devinette:
        if(j1.getGameAllumettes() == 0 and j2.getGameAllumettes() == 0):
            print("Devinettes :  " + G + str(j1.getScoreAllumettes()) + W + "/" + R + str(j1.getGameAllumettes() - j1.getScoreAllumettes()) + " " + O + "100%" + W + (21 - (len(str(j1.getScoreAllumettes()) + "/" + str(j1.getGameAllumettes() - j1.getScoreAllumettes())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getScoreAllumettes()) + "/" + R + str(j2.getGameAllumettes() - j2.getScoreAllumettes()) + O + " 100%" + W)
        elif(j1.getGameAllumettes() == 0):
            print("Devinettes :  " + G + str(j1.getScoreAllumettes()) + W + "/" + R + str(j1.getGameAllumettes() - j1.getScoreAllumettes()) + " " + O + "100%" + W +  (21 - (len(str(j1.getScoreAllumettes()) + "/" + str(j1.getGameAllumettes() - j1.getScoreAllumettes())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getScoreAllumettes()) + "/" + R + str(j2.getGameAllumettes() - j2.getScoreAllumettes()) + O + " " + str(round((j2.getScoreAllumettes()/j2.getGameAllumettes()) * 100)) + "%" + W)
        elif(j2.getGameAllumettes() == 0):
            print("Devinettes :  " + G + str(j1.getScoreAllumettes()) + W + "/" + R + str(j1.getGameAllumettes() - j1.getScoreAllumettes()) + " " + O + str(round((j1.getScoreAllumettes()/j1.getGameAllumettes()) * 100)) + "%"  + W + (21 - (len(str(j1.getScoreAllumettes()) + "/" + str(j1.getGameAllumettes() - j1.getScoreAllumettes())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getScoreAllumettes()) + "/" + R + str(j2.getGameAllumettes() - j2.getScoreAllumettes()) + O + " 100%" + W)
        else:
            print("Devinettes :  " + G + str(j1.getScoreAllumettes()) + W + "/" + R + str(j1.getGameAllumettes() - j1.getScoreAllumettes()) + " " + O + str(round((j1.getScoreAllumettes()/j1.getGameAllumettes()) * 100)) + "%"  + W + (21 - (len(str(j1.getScoreAllumettes()) + "/" + str(j1.getGameAllumettes() - j1.getScoreAllumettes())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getScoreAllumettes()) + "/" + R + str(j2.getGameAllumettes() - j2.getScoreAllumettes()) + " " + O + str(round((j2.getScoreAllumettes()/j2.getGameAllumettes()) * 100)) + "%" + W)

        #afficher score morpion:
        if(j1.getGameMorpion() == 0 and j2.getGameMorpion() == 0):
            print("Devinettes :  " + G + str(j1.getScoreMorpion()) + W + "/" + R + str(j1.getGameMorpion() - j1.getScoreMorpion()) + " " + O + "100%" + W + (21 - (len(str(j1.getScoreMorpion()) + "/" + str(j1.getGameMorpion() - j1.getScoreMorpion())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getScoreMorpion()) + "/" + R + str(j2.getGameMorpion() - j2.getScoreMorpion()) + O + " 100%" + W)
        elif(j1.getGameMorpion() == 0):
            print("Devinettes :  " + G + str(j1.getScoreMorpion()) + W + "/" + R + str(j1.getGameMorpion() - j1.getScoreMorpion()) + " " + O + "100%" + W +  (21 - (len(str(j1.getScoreMorpion()) + "/" + str(j1.getGameMorpion() - j1.getScoreMorpion())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getScoreMorpion()) + "/" + R + str(j2.getGameMorpion() - j2.getScoreMorpion()) + O + " " + str(round((j2.getScoreMorpion()/j2.getGameMorpion()) * 100)) + "%" + W)
        elif(j2.getGameMorpion() == 0):
            print("Devinettes :  " + G + str(j1.getScoreMorpion()) + W + "/" + R + str(j1.getGameMorpion() - j1.getScoreMorpion()) + " " + O + str(round((j1.getScoreMorpion()/j1.getGameMorpion()) * 100)) + "%"  + W + (21 - (len(str(j1.getScoreMorpion()) + "/" + str(j1.getGameMorpion() - j1.getScoreMorpion())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getScoreMorpion()) + "/" + R + str(j2.getGameMorpion() - j2.getScoreMorpion()) + O + " 100%" + W)
        else:
            print("Devinettes :  " + G + str(j1.getScoreMorpion()) + W + "/" + R + str(j1.getGameMorpion() - j1.getScoreMorpion()) + " " + O + str(round((j1.getScoreMorpion()/j1.getGameMorpion()) * 100)) + "%"  + W + (21 - (len(str(j1.getScoreMorpion()) + "/" + str(j1.getGameMorpion() - j1.getScoreMorpion())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getScoreMorpion()) + "/" + R + str(j2.getGameMorpion() - j2.getScoreMorpion()) + " " + O + str(round((j2.getScoreMorpion()/j2.getGameMorpion()) * 100)) + "%" + W)

        #afficher score puissance 4:
        if(j1.getGamePuissance4() == 0 and j2.getGamePuissance4() == 0):
            print("Devinettes :  " + G + str(j1.getGamePuissance4()) + W + "/" + R + str(j1.getGamePuissance4() - j1.getGamePuissance4()) + " " + O + "100%" + W + (21 - (len(str(j1.getGamePuissance4()) + "/" + str(j1.getGamePuissance4() - j1.getGamePuissance4())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getGamePuissance4()) + "/" + R + str(j2.getGamePuissance4() - j2.getGamePuissance4()) + O + " 100%" + W)
        elif(j1.getGamePuissance4() == 0):
            print("Devinettes :  " + G + str(j1.getGamePuissance4()) + W + "/" + R + str(j1.getGamePuissance4() - j1.getGamePuissance4()) + " " + O + "100%" + W +  (21 - (len(str(j1.getGamePuissance4()) + "/" + str(j1.getGamePuissance4() - j1.getGamePuissance4())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getGamePuissance4()) + "/" + R + str(j2.getGamePuissance4() - j2.getGamePuissance4()) + O + " " + str(round((j2.getGamePuissance4()/j2.getGamePuissance4()) * 100)) + "%" + W)
        elif(j2.getGamePuissance4() == 0):
            print("Devinettes :  " + G + str(j1.getGamePuissance4()) + W + "/" + R + str(j1.getGamePuissance4() - j1.getGamePuissance4()) + " " + O + str(round((j1.getGamePuissance4()/j1.getGamePuissance4()) * 100)) + "%"  + W + (21 - (len(str(j1.getGamePuissance4()) + "/" + str(j1.getGamePuissance4() - j1.getGamePuissance4())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getGamePuissance4()) + "/" + R + str(j2.getGamePuissance4() - j2.getGamePuissance4()) + O + " 100%" + W)
        else:
            print("Devinettes :  " + G + str(j1.getGamePuissance4()) + W + "/" + R + str(j1.getGamePuissance4() - j1.getGamePuissance4()) + " " + O + str(round((j1.getGamePuissance4()/j1.getGamePuissance4()) * 100)) + "%"  + W + (21 - (len(str(j1.getGamePuissance4()) + "/" + str(j1.getGamePuissance4() - j1.getGamePuissance4())))) * " " + "|  " + "Devinettes :  " + G + str(j2.getGamePuissance4()) + "/" + R + str(j2.getGamePuissance4() - j2.getGamePuissance4()) + " " + O + str(round((j2.getGamePuissance4()/j2.getGamePuissance4()) * 100)) + "%" + W)

        print()
        print("--------------------------------------------------------------------")

    if(nb_humans == 1):
        i = 0
        while i < len(listJoueurs) and j1 == None:
            if(listJoueurs[i].getName() == j1_name): j1 = listJoueurs[i]
            i += 1

        if(j1 == None): j1 = joueur(j1_name, 0, 0, 0, 0, 0, 0, 0, 0)

        print("--------------------------------------------------------------------")
        print("                             Profils :                              ")
        print("             Joueur 1 :                             Bot 2 :            ")
        print(35 * " " + "|  " + 35 * " ")
        print(j1_name + (35 - len(j1_name)) * " " + "|  "  + j2_name + (35 - len(j1_name)) * " ")
        print(35 * " " + "|  " + 35 * " ")
        print("Scores :" + 27 * " " + "|  " + "Difficulté : " + str(difficulty[1]) + (22 - len(str(difficulty[1]))) * " ")
        print(35 * " " + "|  " + 35 * " ")
        print("Devinettes :  " + G + str(j1.getScoreDevinette()) + W + "/" + R + str(j1.getGameDevinette() - j1.getScoreDevinette()) + W + (21 - (len(str(j1.getScoreDevinette()) + "/" + str(j1.getGameDevinette() - j1.getScoreDevinette())))) * " " + "|  " + 35 * " ")
        print("Allumettes :  " + G + str(j1.getScoreAllumettes()) + W + "/" + R + str(j1.getGameAllumettes() - j1.getScoreAllumettes()) + W + (21 - len(G + str(j1.getScoreAllumettes()) + "/" + str(j1.getGameAllumettes() - j1.getScoreAllumettes()))) * " " + "|  " + 35 * " ")
        print("Morpion :     " + G + str(j1.getScoreMorpion()) + W + "/" + R + str(j1.getScoreMorpion() - j1.getScoreMorpion()) + W + (21 - len(str(j1.getScoreMorpion()) + "/" + str(j1.getScoreMorpion() - j1.getScoreMorpion()))) * " " + "|  " + 35 * " ")
        print("Puissance 4 : " + G + str(j1.getScorePuissance4()) + W + "/" + R + str(j1.getGamePuissance4() - j1.getScorePuissance4()) + W + (21 - len(str(j1.getScorePuissance4()) + "/" + str(j1.getGamePuissance4() - j1.getScorePuissance4()))) * " " + "|  " + 35 * " ")
        print(35 * " " + "|  " + 35 * " ")
        print("--------------------------------------------------------------------")

    if(nb_humans == 0):
        print("--------------------------------------------------------------------")
        print("                             Profils :                              ")
        print("             Bot 1 :                             Bot 2 :            ")
        print(35 * " " + "|  " + 35 * " ")
        print(j1_name + (35 - len(j1_name)) * " " + "|  "  + j2_name + (35 - len(j1_name)) * " ")
        print(35 * " " + "|  " + 35 * " ")
        print("Difficulté : " + str(difficulty[0]) + (22 - len(str(difficulty[0]))) * " " + "|  " +"Difficulté : " + str(difficulty[1]) + (22 - len(str(difficulty[1]))) * " ")
        print(35 * " " + "|  " + 35 * " ")
        print("--------------------------------------------------------------------")


    os.system("pause")


def __afficher_menu_1():
    """Affiche le menu numéro 1

    Arguments :
        Aucuns

    Retour : affichage

    Private : Cette fonction n'est utile que pour ce script
    """

    os.system("cls")
    print("--------------------------")
    print("        Bienvenue !       ")
    print("                          ")
    print("  1 - Jouer               ")
    print("  2 - Scores              ")
    print("  3 - Règles              ")
    print("  4 - Profils des joueurs ")
    print("  5 - Modifier Joueurs    ")
    print("                          ")
    print("  6 - Quitter             ")
    print("                          ")
    print("--------------------------")

def __afficher_menu_2():
    """Affiche le menu numéro 2

    Arguments :
        Aucuns

    Retour : affichage

    Private : Cette fonction n'est utile que pour ce script
    """
    os.system("cls")
    print("---------------------")
    print("       Jouer :       ")
    print("                     ")
    print("  1 - Devinette      ")
    print("  2 - Allumettes     ")
    print("  3 - Morpion        ")
    print("  4 - Puissance 4    ")
    print("                     ")
    print("  5 - Retour         ")
    print("                     ")
    print("---------------------")


def __afficher_menu_3():
    """Affiche le menu numéro 3

    Arguments :
        Aucuns

    Retour : affichage

    Private : Cette fonction n'est utile que pour ce script
    """

    os.system("cls")
    print("---------------------")
    print("       Scores :      ")
    print("                     ")
    print("  1 - Devinette      ")
    print("  2 - Allumettes     ")
    print("  3 - Morpion        ")
    print("  4 - Puissance 4    ")
    print("                     ")
    print("  5 - Retour         ")
    print("                     ")
    print("---------------------")

def __afficher_menu_4():
    """Affiche le menu numéro 4

    Arguments :
        Aucuns

    Retour : affichage

    Private : Cette fonction n'est utile que pour ce script
    """

    os.system("cls")
    print("---------------------")
    print("       Règles :      ")
    print("                     ")
    print("  1 - Devinette      ")
    print("  2 - Allumettes     ")
    print("  3 - Morpion        ")
    print("  4 - Puissance 4    ")
    print("                     ")
    print("  5 - Retour         ")
    print("                     ")
    print("---------------------")

def __afficher_scores(listJoueur : list[joueur], nom : str):
    """Affiche les scores d'un jeu pour tout les joueurs, classé dans l'ordre croissant

    Arguments :
        Liste des joueurs : list[joueur]
        Nom du jeu : str

    Retour : affichage

    Private : Cette fonction n'est utile que pour ce script
    """
    os.system("cls")
    print("---------------------")
    print("Scores : " + nom)
    print("                     ")

    scores = {}

    for j in listJoueur:
        if(nom == "devinette"): scores[j.getName()] = j.getScoreDevinette()
        if(nom == "allumettes"): scores[j.getName()] = j.getScoreAllumettes()
        if(nom == "morpion"): scores[j.getName()] = j.getScoreMorpion()
        if(nom == "puissance4"): scores[j.getName()] = j.getScorePuissance4()

    #pyright: reportUnknownLambdaType=false
    #pyright: reportUnknownVariableType=false
    scores = sorted(scores.items(), key=lambda t:t[1])

    #pyright: reportUnknownArgumentType=false
    for k in range(len(scores)-1, -1, -1):
        if(scores[k][1] != 0):print(scores[k][0] + " : " + str(scores[k][1]))
    print("                     ")
    print("---------------------")
    os.system("pause")

def __afficher_regles(nom : str):
    """Affiche les règles d'un jeu

    Arguments :
        Nom du jeu : str

    Retour : affichage

    Private : Cette fonction n'est utile que pour ce script
    """

    B  = '\033[94m' # blue
    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)
    O  = '\033[93m' # yellow
    P  = '\033[95m' # purple
    N  = '\033[90m' # noir

    os.system("cls")
    print("---------------------")
    print(O + "Règles : " + nom + W)
    print("---------------------")
    if(nom == "devinette"):
        print("Les joueurs commencent par choisir l'intervalle dans lequel la partie se jouera")
        print("")
        print(N + "(Le joueur qui démarre est défini aléatoirement)" + W)
        print("")
        print("Le " + B + "joueur 1" + W + " choisit " + P + "le nombre a faire deviner" + W + ";")
        print("Le " + R + "joueur 2" + W + " essaye ensuite de le" + P + " deviner" + W + " le plus" + P + " rapidement" + W + " possible")
        print("")
        print("Le " + R + "joueur 2" + W + " choisit le nombre a faire deviner;")
        print("Le " + B + "joueur 1" + W + " essaye ensuite de le" + P + " deviner" + W + " le plus" + P + " rapidement" + W + " possible")
        print("")
        print(P + "Le joueur qui a deviné le plus rapidement gagne la partie !" + W)
    if(nom == "allumettes"):
        print("La partie démarre avec 20 allumettes")
        print("")
        print(N + "(Le joueur qui démarre est défini aléatoirement)" + W)
        print("")
        print("Le " + B + "joueur 1" + W + " choisit de retirer " + P + "entre 1 et 3 allumettes" + W)
        print("")
        print("Le " + R + "joueur 2" + W + " choisit à son tour de retirer " + P + "entre 1 et 3 allumettes" + W)
        print()
        print("Et ainsi de suite " + P + "jusqu'a ne plus y avoir d'allumettes" + W)
        print()
        print(P + "Le joueur qui tire la dernière allumette perd la partie" + W)
    if(nom == "morpion"):
        print("La partie se déroule dans un tableau de 3 x 3")
        print("")
        print(N + "(Le joueur qui démarre est défini aléatoirement)" + W)
        print("")
        print("Le " + B + "joueur 1" + W + " choisit de mettre son " + P + "symbole de couleur" + W + " dans la case qu'il désire")
        print("")
        print("Le " + R + "joueur 2" + W + " choisit de à son tour de mettre son " + P + "symbole de couleur" + W + " dans la case qu'il désire")
        print()
        print("Et ainsi de suite " + P + "jusqu’à obtenir une rangée de 3 symbole de même couleur dans toutes les directions possible" + W)
        print()
        print(P + "Le joueur qui possède les 3 jetons alignés gagne la partie" + W)
    if(nom == "puissance4"):
        print("La partie se déroule dans un tableau de 6 x 7")
        print("")
        print(N + "(Le joueur qui démarre est défini aléatoirement)" + W)
        print("")
        print("Le " + B + "joueur 1" + W + " met un de ses " + P + "jetons de couleur" + W + " dans l’une des colonnes de son choix. Le " + P + "jeton" + W + " tombe alors en bas de la colonne.")
        print("")
        print("Le " + R + "joueur 2" + W + " insère à son tour son " + P + "jeton de couleur" + W + ", dans la colonne de son choix.")
        print()
        print("Et ainsi de suite " + P + "jusqu’à obtenir une rangée de 4 jetons de même couleur dans toutes les directions possible" + W)
        print()
        print(P + "Le joueur qui possède les 4 jetons alignés gagne la partie" + W)
    print("---------------------")
    os.system("pause")

def __ajouterScore(winner : str, jeu : str, listJoueur : list[joueur]):
    """Ajoute un point a un joueur souhaité, designé par son nom, dans le jeu souhaité

    Arguments :
        Vainqueur : str
        Nom du jeu : str
        Liste de joueur : list[joueur]

    Retour : Modification du fichier texte en fonction de la list de joueur

    Private : Cette fonction n'est utile que pour ce script
    """
    playerFound : bool

    playerFound = False

    for j in listJoueur:
        if(j.getName() == winner):
            if(jeu == "devinette"):j.setScoreDevinette(j.getScoreDevinette() + 1)
            elif(jeu == "allumettes"):j.setScoreAllumettes(j.getScoreAllumettes() + 1)
            elif(jeu == "morpion"):j.setScoreMorpion(j.getScoreMorpion() + 1)
            elif(jeu == "puissance4"):j.setScorePuissance4(j.getScorePuissance4() + 1)
            else: print("Jeu inconnu")
            playerFound = True

    if(not playerFound):
        if(jeu == "devinette"): listJoueurs.append(joueur(winner, 1, 1, 0, 0, 0, 0, 0, 0))
        elif(jeu == "allumettes"): listJoueurs.append(joueur(winner, 0, 0, 1, 1, 0, 0, 0, 0))
        elif(jeu == "morpion"): listJoueurs.append(joueur(winner, 0, 0, 0, 0, 1, 1, 0, 0))
        elif(jeu == "puissance4"): listJoueur.append(joueur(winner, 0, 0, 0, 0, 0, 0, 1, 1))
        else: print("Jeu erreur")

    __writePlayersData(listJoueurs)

def __writePlayersData(listJoueur : list[joueur]):
    """Ecris les données des joueurs dans le fichier ./Scores/playersData.txt

    Arguments :
        Liste de joueur : lis[joueur]

    Retour : Modification du fichier texte en fonction de la list de joueur

    Private : Cette fonction n'est utile que pour ce script
    """
    _i : int

    lines : list[str]
    lines = []

    f = open("./Scores/playersData.txt","w")
    for _i in range(0, len(listJoueur)):
        if(_i == 0): lines.append(listJoueur[_i].getName() + " " + str(listJoueur[_i].getScoreDevinette()) + "|" + str(listJoueurs[_i].getGameDevinette()) + " " + str(listJoueur[_i].getScoreAllumettes()) + "|" + str(listJoueurs[_i].getGameAllumettes()) + " " + str(listJoueur[_i].getScoreMorpion()) + "|" + str(listJoueurs[_i].getGameMorpion()) + " " + str(listJoueurs[_i].getScorePuissance4()) + "|" + str(listJoueur[_i].getGamePuissance4()))
        else: lines.append(listJoueur[_i].getName() + " " + str(listJoueur[_i].getScoreDevinette()) + "|" + str(listJoueurs[_i].getGameDevinette()) + " " + str(listJoueur[_i].getScoreAllumettes()) + "|" + str(listJoueurs[_i].getGameAllumettes()) + " " + str(listJoueur[_i].getScoreMorpion()) + "|" + str(listJoueurs[_i].getGameMorpion()) + " " + str(listJoueurs[_i].getScorePuissance4()) + "|" + str(listJoueur[_i].getGamePuissance4()))

    f.writelines(lines)
    f.close()

def __ajouterGame(j1_name : str, j2_name : str, game : str, nb_humans : int, listJoueur : list[joueur]):
    for j in listJoueur :
        if(j.getName() == j1_name):
            if(nb_humans>0):
                if(game=="devinette"):j.setGameDevinnette(j.getGameDevinette() + 1)
                if(game=="allumettes"):j.setGameAllumettes(j.getGameAllumettes() + 1)
                if(game=="morpion"):j.setGameMorpion(j.getGameMorpion() + 1)
                if(game=="puissance4"):j.setGamePuissance4(j.getGamePuissance4() + 1)
        elif(j.getName() == j2_name):
            if(nb_humans==2):
                if(game=="devinette"):j.setGameDevinnette(j.getGameDevinette() + 1)
                if(game=="allumettes"):j.setGameAllumettes(j.getGameAllumettes() + 1)
                if(game=="morpion"):j.setGameMorpion(j.getGameMorpion() + 1)
                if(game=="puissance4"):j.setGamePuissance4(j.getGamePuissance4() + 1)

if __name__ == "__main__":

    listJoueurs : list[joueur]

    j1_name : str
    j2_name : str
    data : list[str]
    nb_humans : int
    difficulty : list[int]
    WantToQuit : bool

    B  = '\033[94m' # blue
    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)

    #demande les infos sur les joueurs
    data = getPlayerData()

    nb_humans = int(data[0])
    difficulty = []
    difficulty.append(int(data[1]))
    difficulty.append(int(data[3]))
    j1_name = data[2]
    j2_name = data[4]


    listJoueurs = __getJoueurs("./Scores/playersData.txt")

    WantToQuit = False

    while not WantToQuit :

        __afficher_menu_1()

        choice = str(input("Choisissez le jeu : "))

        match choice:

            case "1":

                WantToGoBack = False
                while not WantToGoBack :

                    __afficher_menu_2()

                    choice = str(input("Choisissez le jeu : "))

                    match choice:

                        case "1":
                            winner = Devinette.LaunchGame_devinettes(j1_name,j2_name, nb_humans, difficulty)
                            if(not winner == ""):
                                __ajouterScore(winner, "devinette", listJoueurs)
                                __ajouterGame(j1_name, j2_name,"devinette", nb_humans, listJoueurs)

                        case "2":
                            winner = Allumettes.LaunchGame_allumettes(j1_name, j2_name, nb_humans, difficulty)
                            if(not winner == ""):
                                __ajouterScore(winner, "allumettes", listJoueurs)
                                __ajouterGame(j1_name, j2_name,"allumettes", nb_humans, listJoueurs)

                        case "3":
                            winner = Morpion.LaunchGame_morpion(j1_name, j2_name,nb_humans,difficulty)
                            if(not winner == ""):
                                __ajouterScore(winner, "morpion", listJoueurs)
                                __ajouterGame(j1_name, j2_name,"morpion", nb_humans, listJoueurs)

                        case "4":
                            winner = P4.LaunchGame_puissance4(j1_name, j2_name, nb_humans, difficulty)
                            if(not winner == ""):
                                __ajouterScore(winner, "puissance4", listJoueurs)
                                __ajouterGame(j1_name, j2_name,"puissance4", nb_humans, listJoueurs)

                        case "5":
                            WantToGoBack = True

                        case other:
                            print("Réponse inconnue")
                            os.system("pause")

            case "2":
                WantToGoBack = False
                while not WantToGoBack :

                    __afficher_menu_3()

                    choice = str(input("Choisissez le jeu : "))

                    match choice:

                        case "1":
                            __afficher_scores(listJoueurs, "devinette")

                        case "2":
                            __afficher_scores(listJoueurs, "allumettes")

                        case "3":
                            __afficher_scores(listJoueurs, "morpion")

                        case "4":
                            __afficher_scores(listJoueurs, "puissance4")

                        case "5":
                            WantToGoBack = True

                        case other:
                            print("Réponse inconnue")
                            os.system("pause")

            case "3":
                WantToGoBack = False
                while not WantToGoBack :

                    __afficher_menu_4()

                    choice = str(input("Choisissez le jeu : "))

                    match choice:

                        case "1":
                            __afficher_regles("devinette")

                        case "2":
                            __afficher_regles("allumettes")

                        case "3":
                            __afficher_regles("morpion")

                        case "4":
                            __afficher_regles("puissance4")

                        case "5":
                            WantToGoBack = True

                        case other:
                            print("Réponse inconnue")
                            os.system("pause")

            case "4":
                __afficher_profils(j1_name, j2_name, nb_humans, listJoueurs, difficulty)

            case "5":
                data = getPlayerData()

                nb_humans = int(data[0])
                difficulty = []
                difficulty.append(int(data[1]))
                difficulty.append(int(data[3]))
                j1_name = data[2]
                j2_name = data[4]

            case "6":
                WantToQuit = True

            case other:
                print("Réponse inconnue")
                os.system("pause")
