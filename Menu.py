import sys
import pygame as pg
from Snake import *
from Food import *
from PlayerGame import *
from Game import *
from AIGame import *
from MenuManager import *

class Menu:
    def __init__(self,
                 board_size: Tuple[int, int],
                 window: pg.display,
                 title: str):
        self.res = pg.display.get_surface().get_size()
        self.board_size = board_size
        self.window = window
        self.title = title

        # initializing snake and food object
        self.snake = Snake(board_size)
        self.food = Food(board_size, board_size[0])

        self.txts = ["Player", "Pathfinding"]

        # initializing game menu drawer
        self.drawer = MenuManager(self.txts, window)
        self.game = None

    # start menu loop
    def open_menu(self):
        while True:
            self.__key_listener()
            self.draw_menu()

    # draw menu buttons and title
    def draw_menu(self):
        self.window.fill((10, 10, 10))

        self.drawer.draw_title(self.title)
        self.drawer.draw_buttons()
        pg.display.update()

    # handling close button and button clicks
    def __key_listener(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                self.__start_game(self.drawer.get_button_id())

    # starting game depending on button clicked
    def __start_game(self, ch):
        if ch == 0:
            manager = PlayerGame()
        elif ch == 1:
            manager = AIGame(self.board_size, self.snake, self.food)
        else:
            return
        self.game = Game(self.board_size, self.snake, self.food, manager, self.window)
        self.game.start_game()
        self.snake.reset()
