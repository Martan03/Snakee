from typing import List, Tuple
from random import randint

class Food:
    def __init__(self,
                 board_size: Tuple[int, int],
                 size: Tuple[int, int],
                 color: Tuple[int, int, int] = (255, 0, 0)):

        self.board_size = board_size
        self.size = size
        self.color = color
        self.pos = None

    def generate(self, pos):
        self.pos = pos[randint(1, len(pos) - 1)]

    def get_pos(self):
        return [self.pos]

    def get_color(self):
        return self.color
