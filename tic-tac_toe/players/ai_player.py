import numpy as np
from keras.saving import load_model

from player import Player


class AI(Player):

    def __init__(self, name: str, marker: int, file: str):
        super().__init__(name, marker)
        self.model = load_model(file)

    def play_move(self, board: np.array) -> int:
        return self.model.predict(np.concatenate((board.board, np.array([self.marker]))))
