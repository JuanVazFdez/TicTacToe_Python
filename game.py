import language
import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # 3x3 board
        self.currentWinner = None #tracks who is winner

    def printBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: #gets rows
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def printBoardNums():
        numberBoard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] 
        for row in numberBoard:
            print('| ' + ' | '.join(row) + ' |')

    def availableMoves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def emptySquares(self):
        return ' ' in self.board
    
    def numEmptySquares(self):
        return self.board.count(' ')
    
    def makeMove(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        return False
    
    def winner(self, square, letter):
        rowInd = square // 3
        row = self.board[rowInd*3 : (rowInd + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        colInd = square % 3
        column = [self.board[colInd + i * 3] for i in range(3)]
        if all([ spot == letter for spot in column]):
            return True
        
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all ([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot== letter for spot in diagonal2]):
                return True
        
        return False



def play (game, xPlayer, oPlayer, texts, printGame = True):
    if printGame:
        game.printBoardNums()

    letter = 'X'
    while game.emptySquares():
        if letter == 'O':
            square = oPlayer.getMove(game)
        else:
            square = xPlayer.getMove(game)
        if game.makeMove(square, letter):
            if printGame:
                print('\n\n\n\n\n\n', letter + texts['move'], square)
                game.printBoard()
                print('')
            if game.currentWinner:
                if printGame:
                    print(letter +  texts['win'])
                return letter
            
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.8)

    if printGame:
        print(texts['tie'])
            

if __name__ == '__main__':
    texts = {}
    lang = "n/a"
    while lang != 'esp' and lang != 'eng':
        lang = input('To play in English, type "eng"\nPara jugar en Español, introduce "esp"').lower()
    if lang == 'esp':
        texts = language.spanish
    elif lang == 'eng':
        texts = language.english

    xPlayer = HumanPlayer('X', texts)
    oPlayer = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, xPlayer, oPlayer, texts, printGame=True)