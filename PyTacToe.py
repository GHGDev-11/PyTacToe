import sys

class Game:
    def __init__(self):
        self.board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
        self.players = {1: 'X', 2: 'O'}
        self.moves = []
        self.player = None

        self.start()

    def restart(self):
        print("Would you like to play again?\nIf so, type y")
        res = input("> ")
        if res == "y" or res == "Y":
            Game()
        else:
            sys.exit()
    
    def drawBoard(self):
        print(f"{self.board[1]}|{self.board[2]}|{self.board[3]}\n-+-+-\n{self.board[4]}|{self.board[5]}|{self.board[6]}\n-+-+-\n{self.board[7]}|{self.board[8]}|{self.board[9]}")
    
    def start(self):
        for i in range(10):
            if i % 2 == 0:
                self.player = self.players[1]
            else:
                self.player = self.players[2]
        
            print(f"It's your turn, {self.player}!")

            move = input("> ")
            if move not in self.moves:
                self.board[int(move)] = self.player

                self.drawBoard()
                print()
                
                self.moves += move

                if self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1] != ' ' or self.board[4] == self.board[5] and self.board[4] == self.board[6] and self.board[4] != ' ' or self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7] != ' ' or self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[1] != ' ' or self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2] != ' ' or self.board[3] == self.board[6] and self.board[3] == self.board[9] and self.board[3] != ' ' or self.board[1] == self.board[5] and self.board[1] == self.board[9] and self.board[1] != ' ' or self.board[7] == self.board[5] and self.board[7] == self.board[3] and self.board[7] != ' ':
                    print(f"Player {self.player} won!")
                    self.restart()
                
                if len(self.moves) == 9:
                    print("Game over. No one won.")
                    self.restart()
            else:
                print("That spot is already taken!")

Game()