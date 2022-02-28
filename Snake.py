from typing import List, Tuple
from random import randint
import pygame as pg
import sys, time
from Directions import *
from copy import copy

class Snake:
    def __init__(self,
                 board_size: Tuple[int, int],
                 pos: List[Tuple[int, int]] = None,
                 color: Tuple[int, int, int] = (0, 223, 0),
                 dir: Tuple[int, int] = RIGHT):

        self.board_size = board_size

        if not pos:
            pos = [(1, 1)]
        self.pos = pos
        self.length = len(pos)

        self.dir = dir

        self.startPos = copy(pos)
        self.startLength = len(pos)
        self.startDir = copy(dir)

        self.color = color
        
        self.dead = False

    def move(self):
        if self.dead:
            return

        new = self.__get_new_head()
        self.pos.insert(0, new)

    def head_in_snake(self):
        return self.get_head() in self.pos[1:]

    def in_snake(self, node):
        return node in self.pos

    def __get_new_head(self):
        return (self.pos[0][0] + self.dir[0],
                self.pos[0][1] + self.dir[1])

    def get_head(self):
        return self.pos[0]

    def get_pos(self):
        return self.pos

    def get_color(self):
        return self.color

    def get_length(self):
        return self.length

    def set_dir(self, dir):
        self.dir = dir

    def is_dead(self):
        return self.dead

    def death(self, died):
        self.dead = died

    def increase(self):
        self.length += 1

    def decrease(self):
        if len(self.pos) > self.length:
            self.pos.pop()

    def reset(self):
        self.pos = copy(self.startPos)
        self.length = copy(self.startLength)
        self.dir = copy(self.startDir)
        self.dead = False
