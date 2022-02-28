import pygame as pg
from Game import *
from Snake import *
from Food import *
from AIGame import *
from PlayerGame import *
from Menu import *
import sys

def main():
    # initializing window variables
    res = (1280, 720)
    board_size = (32, 18)
    title = ("Snakee")

    # initializing pygame & creating window
    pg.init()
    pg.display.set_caption(title)
    window = pg.display.set_mode(res)

    # creating game menu
    menu = Menu(board_size, window, title)
    menu.open_menu()

if __name__ == '__main__':
    main()
