import pygame as pg
import time
from typing import List, Tuple

class Draw:
    def __init__(self,
                 board_size: Tuple[int, int],
                 window: pg.display):

        self.res = pg.display.get_surface().get_size()
        self.board_size = board_size

        self.mid = (self.res[0] // 2, self.res[1] // 2)

        tile_height = self.res[1] // self.board_size[1]
        tile_width = self.res[0] // self.board_size[0]
        
        if tile_height < tile_width:
            self.tile_size = (tile_height, tile_height)
        else:
            self.tile_size = (tile_width, tile_width)

        self.offset: Tuple[int, int] = (
            (self.res[0] - (self.tile_size[0] * self.board_size[0])) // 2,
            (self.res[1] - (self.tile_size[1] * self.board_size[1])) // 2
        )

        self.window = window
    
    # draw given object
    def draw(self, obj):
        for pos in obj.get_pos():
            if not pos:
                continue

            pg.draw.rect(
                self.window,
                obj.get_color(),
                [
                    self.__get_screen_pos(pos),
                    (self.tile_size[0] - 6, self.tile_size[0] - 6)
                ]
            )

    # draw border around the board
    def draw_border(self, color):
        # left border
        pg.draw.rect(
            self.window,
            color,
            [
                (self.offset[0] + self.tile_size[0] // 2,
                 self.offset[1] + self.tile_size[1] // 2),
                (self.tile_size[0] // 2, 
                self.tile_size[1] * (self.board_size[1] - 1))
            ]
        )
        # right border
        pg.draw.rect(
            self.window,
            color,
            [
                (self.offset[0] + self.tile_size[0] * (self.board_size[0] - 1),
                 self.offset[1] + self.tile_size[1] // 2),
                (self.tile_size[0] // 2, 
                self.tile_size[1] * (self.board_size[1] - 1))
            ]
        )
        # top border
        pg.draw.rect(
            self.window,
            color,
            [
                (self.offset[0] + self.tile_size[0] // 2,
                 self.offset[1] + self.tile_size[1] // 2),
                (self.tile_size[0] * (self.board_size[0] - 1), 
                self.tile_size[1] // 2)
            ]
        )
        # bottom border
        pg.draw.rect(
            self.window,
            color,
            [
                (self.offset[0] + self.tile_size[0] // 2,
                 self.offset[1] + self.tile_size[1] * (self.board_size[1] - 1)),
                (self.tile_size[0] * (self.board_size[0] - 1), 
                self.tile_size[1] // 2)
            ]
        )

    # draw start timer (3 seconds)
    def start_timer(self, snake, food):
        for n in [3, 2, 1]:
            self.window.fill((10, 10, 10))
            [self.draw(s) for s in snake]
            [self.draw(f) for f in food]
            self.draw_border(snake[0].get_color())
            self.__draw_number(n)
            pg.display.update()
            time.sleep(1)

    # draw game over screen and snake length
    def game_over(self, snake, stats):
        font = pg.font.SysFont("Comic Sans MS", 100)
        go = font.render("Game Over", True, (255, 255, 255))
        go_size = font.size("Game Over")

        score_font = pg.font.SysFont("Comic Sans MS", 25)
        score_txt = "Score: " + str(snake.get_length())
        score = score_font.render(score_txt, True, (255, 255, 255))
        score_size = score_font.size(score_txt)

        high_txt = "Highscore: " + str(stats["highscore"])
        high = score_font.render(high_txt, True, (255, 255, 255))
        high_size = score_font.size(high_txt)

        played_txt = "Games Played: " + str(stats["games"])
        played = score_font.render(played_txt, True, (255, 255, 255))
        played_size = score_font.size(played_txt)

        self.window.blit(go, (self.mid[0] - (go_size[0] // 2),
                              self.mid[1] - (go_size[1] // 2)))
        self.window.blit(score, 
                         (self.mid[0] - (score_size[0] // 2),
                          self.mid[1] - (score_size[1] // 2) + go_size[1] // 2))

        self.window.blit(high,
                         (self.mid[0] - (high_size[0] // 2),
                          self.res[1] - 2 * high_size[1] - self.tile_size[1]))

        self.window.blit(played,
                         (self.mid[0] - (played_size[0] // 2),
                          self.res[1] - played_size[1] - self.tile_size[1]))

    # draw number on the middle of the screen
    def __draw_number(self, n):
        font = pg.font.SysFont("Comic Sans MS", 100)
        txt = font.render(str(n), True, (255, 255, 255))
        txt_size = font.size(str(n))
        self.window.blit(txt, (self.mid[0] - (txt_size[0] // 2),
                               self.mid[1] - (txt_size[1] // 2)))

    # returns screen pos from board pos
    def __get_screen_pos(self, pos):
        return (self.tile_size[0] * pos[0] + self.offset[0] + 3,
                self.tile_size[1] * pos[1] + self.offset[1] + 3)
