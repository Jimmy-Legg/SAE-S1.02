class joueur:

    name : str
    win_devinette : int
    win_allumettes : int
    win_morpion : int
    win_puissance4 : int

    def __init__(self, name : str, win_devinette : int, game_devinette : int, win_allumettes : int, game_allumettes : int, win_morpion : int, game_morpion : int, win_puissance4 : int, game_puissance4 : int):

        self.name = name
        self.win_devinette = win_devinette
        self.game_devinette = game_devinette
        self.win_allumettes = win_allumettes
        self.game_allumettes = game_allumettes
        self.win_morpion = win_morpion
        self.game_morpion = game_morpion
        self.win_puissance4 = win_puissance4
        self.game_puissance4 = game_puissance4

    def getName(self)->str:
        return self.name

    def setName(self, name : str):
        self.name = name

    def getScoreDevinette(self)->int:
        return self.win_devinette

    def getScoreAllumettes(self)->int:
        return self.win_allumettes

    def getScoreMorpion(self)->int:
        return self.win_morpion

    def getScorePuissance4(self)->int:
        return self.win_puissance4

    def getGameDevinette(self)->int:
        return self.game_devinette

    def getGameAllumettes(self)->int:
        return self.game_allumettes

    def getGameMorpion(self)->int:
        return self.game_morpion

    def getGamePuissance4(self)->int:
        return self.game_puissance4

    def setScoreDevinette(self, win_devinette : int):
        self.win_devinette = win_devinette

    def setScoreAllumettes(self, win_allumettes : int):
        self.win_allumettes = win_allumettes

    def setScoreMorpion(self, win_morpion : int):
        self.win_morpion = win_morpion

    def setScorePuissance4(self, win_puissance4 : int):
        self.win_puissance4 = win_puissance4

    def setGameDevinnette(self, game_devinette : int):
        self.game_devinette = game_devinette

    def setGameAllumettes(self, game_allumettes : int):
        self.game_allumettes = game_allumettes

    def setGameMorpion(self, game_morpion : int):
        self.game_morpion = game_morpion

    def setGamePuissance4(self, game_puissance4 : int):
        self.game_puissance4 = game_puissance4

    def showScoreDevinette(self):
        print(self.getName(), " : " , self.win_devinette)

    def showScoreAllumettes(self):
        print(self.getName(), " : " , self.win_allumettes)

    def showScoreMorpion(self):
        print(self.getName(), " : " , self.win_morpion)

    def showScorepuissance4(self):
        print(self.getName(), " : " , self.win_puissance4)

