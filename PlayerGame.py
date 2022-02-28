import pygame as pg

from Directions import *

class PlayerGame:
    def __init__(self):
        self.moves = [RIGHT]
        self.input = []
    
    def get_move(self):
        self.__get_input()

        move = self.moves[0]

        if len(self.moves) > 1:
            self.moves.pop(0)
        
        return move

    def set_input(self, input):
        self.input = input

    def __get_input(self):
        for event in self.input:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP or event.key == pg.K_w:
                    if self.moves[-1] != DOWN:
                        self.__add_move(UP)
                elif event.key == pg.K_LEFT or event.key == pg.K_a:
                    if self.moves[-1] != RIGHT:
                        self.__add_move(LEFT)
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    if self.moves[-1] != LEFT:
                        self.__add_move(RIGHT)
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    if self.moves[-1] != UP:
                        self.__add_move(DOWN)
        self.input = []

    def __add_move(self, dir):
        self.moves.append(dir)
        
        if len(self.moves) > 2:
            self.moves.pop(0)
