import pygame as pg
from Settings import *
from Player import Player
from Render import Render
from Map import *


class Main:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        # self.screen = pg.display.set_mode((1200, 1000))
        self.clock = pg.time.Clock()
        self.player = Player(pg.display.get_surface().get_size())
        self.render = Render(self.screen)
        self.run = True

    def events(self):
        for event in pg.event.get():
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.run = False

        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.player.speed_directions[LEFT] = self.player.speed
        if keys[pg.K_d]:
            self.player.speed_directions[RIGHT] = self.player.speed
        if keys[pg.K_w]:
            if self.player.can_jump:
                self.player.speed_directions[UP] = self.player.jump_speed

    def main_loop(self):
        while self.run:
            self.clock.tick(FPS)
            pg.display.set_caption(str(self.clock.get_fps()))
            self.events()
            self.player.move()

            self.rendering()

    def rendering(self):
        self.screen.fill(BLACK)
        self.render.map(self.player.camera_pos)
        self.render.player(self.player.camera_pos, self.player)
        pg.display.update()


main = Main()
main.main_loop()
pg.quit()
