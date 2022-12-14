import os
import random
import time

def __AskVerification(state : int, proposition : int):
    """Procédure qui demande au deuxième joueur les hypothèses sur le nombre entré par le premier

    Arguments :
        State : int (résultat de la vérification : 1 si le nombre est trop grand, 2 s'il est trop petit et 3 s'il est bon)
        Proposition : int

    Retour : affichage

    Private : Cette fonction n'est utile que pour ce script
    """
    W  = '\033[0m'  # white (normal)
    R  = '\033[91m' # red
    O  = '\033[93m' # yellow
    P  = '\033[95m' # purple
    B  = '\033[94m' # blue

    choix : str
    insulte : list[str]
    insulte = ["Ne triche pas petit filou", "Essaye plutot de ne pas mentir","Apprend à compter !"," Réfléchies avant d'agir","Des problèmes de mémoires ?","Bien tenté ... mais non."]
    choix = ""

    while choix != str(state):

        os.system("cls")
        print("Le nombre est il : ")
        print()
        print("1 - plus " + P + "grand " + W + "que " + B + str(proposition) + W)
        print("2 - plus " + O + "petit " + W + "que " + B + str(proposition) + W)
        print("3 - " + B + str(proposition) + W + " est la bonne réponse")
        print()

        choix = input("Choix : ")

        if(choix not in ["3", "2", "1"]):print( R + "réponse impossible" + W)
        else:
            if(choix != str(state)):
                print(R + insulte[random.randint(0, len(insulte) - 1)] + W)

                os.system("pause")

    os.system("cls")

def __LaunchTurnBot(nombre_a_trouver : int, couleur : str, couleur1 : str, j_name : str, p_name : str, mini:int, maxi:int, difficulty : int, playAgainstHuman : bool)->float:
    """Fonction qui lance un tour d'un bot

    Arguments :
        Nombre a trouver : int
        Couleur du joueur a qui est le tour : str
        Couleur de son adversaire : str
        Nom du joueur a qui est le tour : str
        Nom de son adversaire : str
        Borne minimum : int
        Borne maximum : int
        Difficulté du bot : int (compris entre 1 et 3)
        Joue contre un humain : bool


    Retour : temps pris : float

    Private : Cette fonction n'est utile que pour ce script
    """
    choix : str
    temps : float
    tempsTotal : float
    nombre : int
    choixPrecedents : list[str]
    mini2 : int
    maxi2: int

    choixPrecedents = []

    tempsTotal = 0

    W  = '\033[0m'  # white (normal)
    G  = '\033[92m' # green
    O  = '\033[93m' # yellow

    os.system("cls")

    temps = time.time()

    print(couleur + j_name + W + " est en train de choisir une hypothèse ...")

    if(difficulty == 1): time.sleep(random.random() * 4 + 2)
    elif(difficulty == 2): time.sleep(random.random() * 3.5 + 1.5)
    else: time.sleep(random.random() * 2 + 1)

    mini2 = mini
    maxi2 = maxi
    nombre = random.randint(mini, maxi)
    choix = str(nombre)
    choixPrecedents.append(choix)

    if(not int(choix) == nombre_a_trouver):

        tempsTotal += time.time() - temps
        if playAgainstHuman:
            if(int(choix) > nombre_a_trouver): __AskVerification(2, int(choix))
            elif(int(choix) < nombre_a_trouver): __AskVerification(1, int(choix))
        else:
            os.system("cls")
            print(couleur + j_name + W + " propose la valeur : " + O + choix)
            print(couleur1 + p_name + W + " est en train de vérifier la valeur ...")
            time.sleep(2)
        temps = time.time()

    while nombre != nombre_a_trouver:

        if(nombre > nombre_a_trouver):

            os.system("cls")
            print(couleur1 + p_name + W + " dit que c'est un nombre plus petit que " + O + str(nombre) + W + " : ")
            print(couleur + j_name + W + " est en train de choisir une hypothèse ...")

            if(difficulty == 1):
                choix = str(random.randint(mini, nombre - 1))
                while choix in choixPrecedents:
                    choix = str(random.randint(mini, nombre - 1))
                time.sleep(random.random() * 4 + 2)
            elif(difficulty == 2):
                maxi2 = nombre - 1
                choix = str(random.randint(mini2, maxi2))
                time.sleep(random.random() * 3.5 + 1.5)
            else:
                maxi2 = nombre - 1
                choix = str((mini2 + maxi2) // 2)
                time.sleep(random.random() * 2 + 1)

        elif(nombre < nombre_a_trouver):

            os.system("cls")
            print(couleur1 + p_name + W + " dit que c'est un nombre plus grand que " + O + str(nombre) + W + " : ")
            print(couleur + j_name + W + " est en train de choisir une hypothèse ...")

            if(difficulty == 1):
                choix = str(random.randint(nombre + 1, maxi))
                while choix in choixPrecedents:
                    choix = str(random.randint(nombre + 1, maxi))
                time.sleep(random.random() * 4 + 2)
            elif(difficulty == 2):
                mini2 = nombre + 1
                choix = str(random.randint(mini2, maxi2))
                time.sleep(random.random() * 3.5 + 2)
            else:
                mini2 = nombre + 1
                choix = str((mini2 + maxi2) // 2)
                time.sleep(random.random() * 2 + 1)


        nombre = int(choix)
        choixPrecedents.append(choix)
        tempsTotal += time.time() - temps

        if playAgainstHuman:
            if(int(choix) > nombre_a_trouver): __AskVerification(2, int(choix))
            elif(int(choix) < nombre_a_trouver): __AskVerification(1, int(choix))
        else:
            os.system("cls")
            print(couleur + j_name + W + " propose la valeur : " + O + choix)
            print(couleur1 + p_name + W + " est en train de vérifier la valeur ...")
            time.sleep(2)

        temps = time.time()

    tempsTotal += time.time() - temps
    if(playAgainstHuman):__AskVerification(3, int(choix))
    else:
        os.system("cls")
        print(couleur + j_name + W + " propose la valeur : " + O + choix)
        print(couleur1 + p_name + W + " est en train de vérifier la valeur ...")
        time.sleep(2)
        os.system("cls")
    print("-----------------------------------")
    print(couleur + j_name + W + " à trouvé le nombre " + G + str(nombre_a_trouver) + W + " en " + str(tempsTotal) + " secondes")
    print("-----------------------------------")
    os.system("pause")

    return tempsTotal

def __LaunchTurn(nombre_a_trouver : int, couleur : str, couleur1 : str, j_name : str, p_name : str, mini:int, maxi:int, nb_humans : int)->float:
    """Fonction qui lance le tour d'un joueur

    Arguments :
        Nombre a trouver : int
        Couleur du joueur a qui est le tour : str
        Couleur de son adversaire : str
        Nom du joueur a qui est le tour : str
        Nom de son adversaire : str
        Borne minimum : int
        Borne maximum : int
        Nombre de joueur humains : int (compris entre 0 et 2)


    Retour : temps pris : float

    Private : Cette fonction n'est utile que pour ce script
    """
    choix : str
    temps : float
    tempsTotal : float
    nombre : int

    tempsTotal = 0

    W  = '\033[0m'  # white (normal)
    R  = '\033[91m' # r
    N  = '\033[90m' # noir
    O  = '\033[93m' # yellow
    P  = '\033[95m' # purple
    G  = '\033[92m' # green

    os.system("cls")
    print("-----------------------------------")
    print(couleur + j_name + W + " à vous de jouer !" + N + " (Appuyez pour lancer le chronomètre)" + W)
    print("-----------------------------------")
    print("Nombre entre " + O + str(mini) + W + " et " + P + str(maxi) + W + " : ")
    os.system("pause")
    os.system("cls")

    temps = time.time()

    print("-----------------------------------")
    print(couleur + j_name + W + " à vous de jouer !")
    print("-----------------------------------")

    choix = ""
    nombre = 0
    choiceIsOk = False
    while not choiceIsOk :

        print("Nombre entre " + O + str(mini) + W + " et " + P + str(maxi) + W + " : ")
        choix = input("Faites une première hypothèse : ")
        if(not str(choix).isdigit() or int(choix) < int(mini) or int(choix) > int(maxi)):
            os.system("cls")
            print("-----------------------------------")
            print(couleur + j_name + W + " à vous de jouer ! " + R + "Valeur impossible" + W)
            print("-----------------------------------")
        else:
            nombre = int(choix)
            choiceIsOk = True

    if(not int(choix) == nombre_a_trouver):

        tempsTotal += time.time() - temps
        if(nb_humans == 2):
            if(int(choix) > nombre_a_trouver): __AskVerification(2, int(choix))
            elif(int(choix) < nombre_a_trouver): __AskVerification(1, int(choix))
        temps = time.time()

        os.system("cls")
        print("-----------------------------------")
        print(couleur + j_name + W + " à vous de jouer !")
        print("-----------------------------------")

    while nombre != nombre_a_trouver:

        if(nombre > nombre_a_trouver):

            print("Nombre entre " + O + str(mini) + W + " et " + P + str(maxi) + W + " : ")

            choix = input(couleur1 + p_name + W + " dit que c'est un nombre plus " + O + "petit " + W + "que " + G + str(nombre) + W + " : ")

        elif(nombre < nombre_a_trouver):

            print("Nombre entre " + O + str(mini) + W + " et " + P + str(maxi) + W + " : ")

            choix = input(couleur1 + p_name + W + " dit que c'est un nombre plus " + P + "grand " + W + "que " + G + str(nombre) + W + " : ")

        if(not choix.isdigit() or int(choix) < int(mini) or int(choix) > int(maxi)):

            os.system("cls")
            print("-----------------------------------")
            print(couleur + j_name + W + " à vous de jouer ! " + R + "Valeur impossible" + W)
            print("-----------------------------------")

        else :

            nombre = int(choix)

            tempsTotal += time.time() - temps
            if(nb_humans == 2):
                if(int(choix) > nombre_a_trouver): __AskVerification(2, int(choix))
                elif(int(choix) < nombre_a_trouver): __AskVerification(1, int(choix))
            temps = time.time()

            if(not int(choix) == nombre_a_trouver):
                os.system("cls")
                print("-----------------------------------")
                print(couleur + j_name + W + " à vous de jouer !")
                print("-----------------------------------")


    tempsTotal += time.time() - temps
    if(nb_humans == 2):__AskVerification(3, int(choix))
    else: os.system("cls")
    print("-----------------------------------")
    print(G + "Trouvé ! " + W + "Le nombre était bien : " + G + str(nombre_a_trouver) + W)
    print("-----------------------------------")
    os.system("pause")

    return tempsTotal

def __askNombreATrouver(couleur : str, j_name : str, mini : int, maxi : int)->int:
    """Fonction qui demande le nombre que l'adversaire du joueur devra trouver

    Arguments :
        Couleur : str
        Nom du joueur : str
        Borne minimum : int
        Borne maximum : int

    Retour : Nombre a trouver : int

    Private : Cette fonction n'est utile que pour ce script
    """
    choix : str

    W  = '\033[0m'  # white (normal)
    R  = '\033[91m' # red
    O  = '\033[93m' # yellow
    P  = '\033[95m' # purple

    os.system("cls")
    print("Tour de " + couleur + j_name + W + " :")

    choix = str(input("Choisissez un nombre entre " + O + str(mini) + W + " et " + P + str(maxi) + W + " : "))
    while (not choix.isdigit() or int(choix) < int(mini) or int(choix) > int(maxi)):
        os.system("cls")
        print("Tour de " + couleur + j_name + W + " : " + R + "Valeur impossible" + W)
        choix = str(input("Choisissez un nombre entre " + O + str(mini) + W + " et " + P + str(maxi) + W + " : "))

    return int(choix)

def __askBotNombreATrouver(couleur : str, j_name : str, mini : int, maxi : int)->int:
    """Fonction qui demande le nombre que l'adversaire du bot devra trouver

    Arguments :
        couleur : str
        Nom du joueur : str
        Borne minimum : int
        Borne maximum : int

    Retour : Nombre a trouver : int

    Private : Cette fonction n'est utile que pour ce script
    """
    W  = '\033[0m'  # white (normal)

    os.system("cls")
    print(couleur + j_name + W + " est en train de choisir son nombre ...")
    time.sleep(2)

    return random.randint(mini, maxi)

def __checkWin(temps1:float,temps2:float, j1_name : str, j2_name : str, nb_humans : int)->str:
    """Fonction qui affiche le temps des deux joueurs et deduit le joueur qui a gagné en les comparant

    Arguments :
        Temps joueur 1 : float
        Temps joueur 2 : float
        Nom joueur 1 : str
        Nom joueur 2 : str
        Nombre de joueurs humains : int (compris entre 0 et 2)

    Retour : Vainqueur : str (Si le joueur est un bot, retourne "" pour ne pas ajouter de scores)

    Private : Cette fonction n'est utile que pour ce script
    """


    os.system("cls")

    B  = '\033[94m' # blue
    W  = '\033[0m'  # white (normal)
    R  = '\033[91m' # r

    if temps1 < temps2 :
        print("---------------------------")
        print("")
        print("le gangnant est : " + B + j1_name + W)
        print("")
        print("---------------------------")
        print("")
        print(B + str(j1_name) + W + " a terminé en : " + str(temps1)[0:5])
        print(R + str(j2_name) + W + " a terminé en : " + str(temps2)[0:5])
        print("")
        print("---------------------------")
        os.system("pause")
        if(nb_humans > 0): winner = j1_name
        else: winner = ""

    elif temps1 > temps2 :
        print("---------------------------")
        print("")
        print("le gangnant est : " + R + j2_name + W)
        print("")
        print("---------------------------")
        print("")
        print(B + str(j1_name) + W + " a terminé en : " + str(temps1)[0:5])
        print(R + str(j2_name) + W + " a terminé en : " + str(temps2)[0:5])
        print("")
        print("---------------------------")
        os.system("pause")
        if(nb_humans == 2): winner = j2_name
        else: winner = ""

    else:
        print("---------------------------")
        print("")
        print("égalité")
        print("")
        print("---------------------------")
        print("")
        print(B + str(j1_name) + W + " a terminé en : " + str(temps1)[0:5])
        print(R + str(j2_name) + W + " a terminé en : " + str(temps2)[0:5])
        print("")
        print("---------------------------")
        os.system("pause")
        winner = ""

    return winner

def __askForMaxi(mini : int):
    """Fonction qui demande le nombre maximum que les joueurs vont pouvoir entrer, forcément supérieur a la Borne minimum

    Arguments :
        Borne minimum : int

    Retour : Borne max : int

    Private : Cette fonction n'est utile que pour ce script
    """

    maxi : str
    maxi_ok : bool

    W  = '\033[0m'  # white (normal)
    P  = '\033[95m' # purple
    R  = '\033[91m' # red
    O  = '\033[93m' # yellow

    os.system("cls")
    maxi = input('Définissez le nombre ' + P + 'maximum' + W + ' que pourront entrez les joueurs : ')

    maxi_ok = False

    while(not maxi_ok):

        if(not maxi.isdigit()):
            print(R + "Valeur impossible !" + W)
            os.system("pause")
            os.system("cls")
            maxi = input('Définissez le nombre ' + P + 'maximum' + W + ' que pourront entrez les joueurs : ')
        elif(int(maxi) <= mini):
            print(R + "Le" + P + " Maximum" + R +" doit être plus élevé que le " + O +"minimum" + R + " !" + W)
            os.system("pause")
            os.system("cls")
            maxi = input('Définissez le nombre ' + P + 'maximum' + W + ' que pourront entrez les joueurs : ')
        else:
            maxi_ok = True

    return int(maxi)


def __askForMini():
    """Fonction qui demande le nombre minimum que les joueurs vont pouvoir entrer

    Arguments :
        Aucun

    Retour : Borne max : int

    Private : Cette fonction n'est utile que pour ce script
    """
    mini : str

    W  = '\033[0m'  # white (normal)
    O  = '\033[93m' # yellow
    R  = '\033[91m' # red

    os.system("cls")

    mini = str(input('Définissez le nombre ' + O + 'minimum' + W + ' que pourront entrez les joueurs : '))

    while(not mini.isdigit()):
        print(R + "Valeur impossible" + W)
        os.system("pause")
        os.system("cls")
        print("")
        mini = str(input('Définissez le nombre ' + O + 'minimum' + W + ' que pourront entrez les joueurs : '))


    return int(mini)

def LaunchGame_devinettes(j1_name : str, j2_name : str, nb_humans : int, difficulty : list[int])->str:
    """Fonction qui lance la partie de devinettes

    Arguments :
        Nom du joueur 1 : str
        Nom du joueur 2 : str
        Nombre de joueur humains : int (compris entre 0 et 2)
        Difficulté : list[int] (en position 0 la difficulté du joueur 1 et en position 1 celle du joueur 2)

    Retour : Vainqueur : str

    Private : Cette fonction n'est utile que pour ce script
    """

    nombre_a_trouver : int
    temps1 : float
    temps2 : float
    mini : int
    maxi : int

    B  = '\033[94m' # blue
    R  = '\033[91m' # r

    mini = __askForMini()

    maxi = __askForMaxi(mini)

    if(nb_humans == 2):
        nombre_a_trouver = __askNombreATrouver(B, j1_name, mini, maxi)

        temps2 = __LaunchTurn(nombre_a_trouver, R, B, j2_name, j1_name, mini, maxi, nb_humans)

        nombre_a_trouver = __askNombreATrouver(R, j2_name, mini, maxi)

        temps1 = __LaunchTurn(nombre_a_trouver, B, R, j1_name, j2_name, mini, maxi, nb_humans)

    elif(nb_humans == 1):
        nombre_a_trouver = __askNombreATrouver(B, j1_name, mini, maxi)

        temps2 = __LaunchTurnBot(nombre_a_trouver, R, B, j2_name, j1_name, mini, maxi, difficulty[0], True)

        nombre_a_trouver = __askBotNombreATrouver(R, j2_name, mini, maxi)

        temps1 = __LaunchTurn(nombre_a_trouver, B, R, j1_name, j2_name, mini, maxi, nb_humans)
    else:
        nombre_a_trouver = __askBotNombreATrouver(B, j1_name, mini, maxi)

        temps2 = __LaunchTurnBot(nombre_a_trouver, R, B, j2_name, j1_name, mini, maxi, difficulty[0], False)

        nombre_a_trouver = __askBotNombreATrouver(R, j2_name, mini, maxi)


        temps1 = __LaunchTurnBot(nombre_a_trouver, B, R, j1_name, j2_name, mini, maxi, difficulty[1], False)

    #check et retour du vainqueur
    return __checkWin(temps1, temps2, j1_name, j2_name, nb_humans)
