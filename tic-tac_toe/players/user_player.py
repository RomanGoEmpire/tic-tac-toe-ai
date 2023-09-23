from player import Player
from board import Board


class User(Player):

    def __init__(self, name: str, marker: int):
        super().__init__(name, marker)

    def play_move(self, board: Board) -> int:
        return int(input("Enter a move"))
