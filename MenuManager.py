import pygame as pg
from typing import List, Tuple

class MenuManager:
    def __init__(self,
                 txts: List[str],
                 window: pg.display,
                 color: Tuple[int, int, int] = (0, 230, 0),
                 inactive_color: Tuple[int, int, int] = (0, 200, 0),
                 btn_size: Tuple[int, int] = (200, 40),
                 btn_margin: Tuple[int, int] = 20):
        self.res = pg.display.get_surface().get_size()
        self.mid = (self.res[0] // 2, self.res[1] // 2)

        self.size = btn_size
        self.margin = btn_margin

        self.window = window
        self.font = pg.font.SysFont("Comic Sans MS", 30)
        self.titleFont = pg.font.SysFont("Comic Sans MS", 70)

        self.color = color
        self.inactive_color = inactive_color
        self.txts = txts

        self.__get_start_pos()
        self.__calculate_pos()

    # draw game menu title
    def draw_title(self, text):
        txt = self.titleFont.render(str(text), True, (255, 255, 255))
        txt_size = self.titleFont.size(str(text))

        self.window.blit(txt, (self.mid[0] - txt_size[0] // 2,
                               self.startPos[1] // 2 - txt_size[1] // 2))

    # draw all buttons
    def draw_buttons(self):
        for i in range(len(self.txts)):
            self.draw_button(self.positions[i], self.txts[i])

    # draw given button
    def draw_button(self, pos, text):
        txt = self.font.render(str(text), True, (0, 0, 0))
        txt_size = self.font.size(str(text))
        mouse = pg.mouse.get_pos()

        if (pos[0] <= mouse[0] <= pos[0] + self.size[0] and
            pos[1] <= mouse[1] <= pos[1] + self.size[1]):
            pg.draw.rect(
                self.window,
                self.color,
                [pos, self.size]
            )
        else:
            pg.draw.rect(
                self.window,
                self.inactive_color,
                [pos, self.size]
            )
        self.window.blit(
            txt,
            (
                self.mid[0] - txt_size[0] // 2,
                pos[1] + self.size[1] // 2 - txt_size[1] // 2
            )
        )

    # get button id depending on mouse pos
    def get_button_id(self):
        n = 0
        mouse = pg.mouse.get_pos()
        for pos in self.positions:
            if (pos[0] <= mouse[0] <= pos[0] + self.size[0] and
                pos[1] <= mouse[1] <= pos[1] + self.size[1]):
                return n
            n += 1

    def set_txts(self, txts):
        self.txts = txts

    def set_color(self, color, inactive_color):
        self.color = color
        self.inactive_color = inactive_color

    def set_size(self, size):
        self.size = size
        self.__get_start_pos()
        self.__calculate_pos()

    def get_pos(self, n):
        return (self.startPos )

    def __calculate_pos(self):
        pos = []
        for i in range(len(self.txts)):
            pos.append((
                self.startPos[0], 
                self.startPos[1] + (self.size[1] + self.margin) * i
            ))
        self.positions = pos

    def __get_start_pos(self):
        n = len(self.txts)
        self.startPos = (
            self.mid[0] - self.size[0] // 2,
            self.mid[1] - (self.size[1] * n + self.margin * (n - 1)) // 2
        )
