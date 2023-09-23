from board import Board
from player import Player


class Game:

    def __init__(self, players: list[Player]):
        self.board = Board()
        self.players = players
        self.winner = None

    def start_game(self):
        current = 0
        for i in range(9):
            index = -1
            print(self.board)
            while not self.board.can_place(index):
                index = self.players[current].play_move(self.board)
            self.board.place(index, self.players[current].marker)
            if self.board.get_winner():
                print(self.players[current].name)
                self.winner = self.players[current]
                break
            current = 1 if current == 0 else 0
        if self.winner is None:
            print("No winner")
