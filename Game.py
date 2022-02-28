from typing import List, Tuple
import pygame as pg
import json, os
from Snake import *
from Food import *
from Draw import *
from PlayerGame import *

class Game:
    def __init__(self,
                 board_size: Tuple[int, int],
                 snake: Snake,
                 food: Food,
                 game_manager,
                 window: pg.display):

        self.res = pg.display.get_surface().get_size()
        self.board_size = board_size
        self.snake = snake
        self.food = food
        self.game_manager = game_manager
        self.window = window

        # initializing game drawer
        self.drawer = Draw(board_size, window)

        self.tiles = self.__get_tiles()
        self.statsDir = "stats.json"

    # starting game loop
    def start_game(self):
        self.__load_stats()
        self.playerQuit = False
        clock = pg.time.Clock()

        self.food.generate(self.__different_tiles(self.snake.get_pos()))

        # countdown to start the game
        self.drawer.start_timer([self.snake], [self.food])

        # loop until snake dies
        while not self.snake.is_dead():
            self.__key_listener()
            
            clock.tick(self.stats["speed"])
            
            self.snake.set_dir(self.game_manager.get_move())
            self.snake.move()

            # eat check
            if self.snake.get_head() in self.food.get_pos():
                self.food.generate(self.__different_tiles(self.snake.get_pos()))
                self.snake.increase()
            else:
                self.snake.decrease()

            if not self.snake.is_dead():
                self.snake.death(self.__death())
            self.draw()

    def __key_listener(self):
        input = pg.event.get()
        self.game_manager.set_input(input)
        for event in input:
            if event.type == pg.QUIT:
                self.__save_stats()
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playerQuit = True
                    self.snake.death(True)
                if event.key == pg.K_KP_PLUS:
                    self.__increase_ticks()
                if event.key == pg.K_KP_MINUS:
                    self.__decrease_ticks()

    def __increase_ticks(self):
        self.stats["speed"] += 2

    def __decrease_ticks(self):
        if self.stats["speed"] >= 3:
            self.stats["speed"] -= 2

    # calling functions from game drawer
    def draw(self):
        if self.snake.is_dead():
            self.__save_stats()
            if self.playerQuit:
                return
            self.drawer.game_over(self.snake, self.stats)
            pg.display.update()
            time.sleep(3)
            return

        self.window.fill((10, 10, 10))
        self.drawer.draw_border(self.snake.get_color())
        self.drawer.draw(self.snake)
        self.drawer.draw(self.food)
        pg.display.update()

    def __load_stats(self):
        if not os.path.exists(self.statsDir):
            with open(self.statsDir, "w+") as file:
                self.stats = {
                    "highscore": 0,
                    "games": 0,
                    "speed": 15,
                }
                json.dump(self.stats, file)
        else:
            with open("stats.json", "r") as file:
                self.stats = json.load(file)

    def __save_stats(self):
        if type(self.game_manager) is PlayerGame:
            self.stats["games"] += 1
            if self.snake.get_length() > self.stats["highscore"]:
                self.stats["highscore"] = self.snake.length

        with open("stats.json", "w") as outfile:
            json.dump(self.stats, outfile)

    # death check
    def __death(self):
        return (self.__node_in_boundaries(self.snake.get_head()) or
                self.snake.head_in_snake())

    # snake in boundary check
    def __node_in_boundaries(self, node):
        return not (0 < node[0] < self.board_size[0] - 1 and
                    0 < node[1] < self.board_size[1] - 1)

    def __get_tiles(self):
        tiles = []
        for i in range(1, self.board_size[1] - 1):
            for j in range(1, self.board_size[0] - 1):
                tiles.append((j, i))
        return tiles

    def __different_tiles(self, arr):
        return [i for i in self.tiles if i not in arr]
