import random

class Player:
    def __init__(self, letter):
        #defines letter
        self.letter = letter

    def getMove(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        square = random.choice(game.availableMoves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter, texts):
        super().__init__(letter)
        self.texts = texts

    def getMove(self, game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter + self.texts['turn'])
            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print(self.texts['wrong'])
        return val