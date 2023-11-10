import pygame as pg
from Map import *
from Settings import *


class Render:
    def __init__(self, screen):
        self.screen = screen

    def player(self, camera_pos, player):
        try:
            pg.draw.rect(self.screen, WHITE, (player.pos[0] - camera_pos[0],
                                              player.pos[1] - camera_pos[1], tile, tile))
        except:
            pass

    def map(self, camera_pos):
        for y in level_map:
            for x in level_map[y]:
                pg.draw.rect(self.screen, BLUE, (x * tile - camera_pos[0], y * tile - camera_pos[1], tile, tile))
