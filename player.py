import math
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
    
class MasterComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        if len(game.availableMoves()) == 9:
            square = random.choice(game.availableMoves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        maxPlayer = self.letter
        otherPlayer = 'O' if player == 'X' else 'X'

        if state.currentWinner == otherPlayer:
            return {'position': None, 'score': 1 * (state.numEmptySquares() + 1) if otherPlayer == maxPlayer else -1 * (
                        state.numEmptySquares() + 1)}
        elif not state.emptySquares():
            return {'position': None, 'score': 0}
        
        if player == maxPlayer:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possibleMove in state.availableMoves():
            state.makeMove(possibleMove, player)
            simScore = self.minimax(state, otherPlayer)

            state.board[possibleMove] = ' '
            state.currentWinner = None
            simScore['position'] = possibleMove
            if player == maxPlayer:
                if simScore['score'] > best['score']:
                    best = simScore
            else:
                if simScore['score'] < best['score']:
                    best = simScore
        return best