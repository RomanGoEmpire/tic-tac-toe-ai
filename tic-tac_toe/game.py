from board import Board
from random_player import RandomPlayer

class Game:

    def __init__(self):
        self.board = Board()
        self.players = [RandomPlayer("Player 1", 1), RandomPlayer("Player 2", 2)]
        self.winner = None

    def start_game(self):
        current = 0
        for i in range(9):
            free_moves = self.board.get_free_places()
            x, y = self.players[current].play_move(free_moves)
            self.board.place(x, y, self.players[current].marker)
            print(self.board)
            if self.board.get_winner():
                print(self.players[current].name)
                self.winner = self.players[current]
                break
            current = 1 if current == 0 else 0
        if self.winner is None:
            print("No winner")

