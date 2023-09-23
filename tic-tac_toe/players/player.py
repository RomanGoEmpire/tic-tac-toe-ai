from board import Board

class Player:

    def __init__(self, name: str, marker: int):
        self.name = name
        self.marker = marker

    def play_move(self, board: Board) -> int:
        return 0
