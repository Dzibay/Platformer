from Settings import *
from Map import *


class Player:
    def __init__(self, display_size):
        self.display_width, self.display_height = display_size
        self.pos = [500, 550]
        self.camera_pos = [0, 0]
        self.speed_directions = [0, 0, 0, 0]

        self.is_jumping = 0
        self.can_jump = True
        self.jump_height = 200
        self.speed = 10
        self.jump_speed = 15

    def move(self):
        if self.speed_directions[LEFT] > 0:
            for i in range(self.speed):
                if (self.pos[0] - 1) // tile not in level_map[self.pos[1] // 50] and \
                        (self.pos[0] - 1) // tile not in level_map[self.pos[1] // 50 + 1]:
                    self.pos[0] -= 1
                    if self.camera_pos[0] > 0 and self.pos[0] < self.camera_pos[0] + self.display_width // 2:
                        self.camera_pos[0] -= 1
            self.speed_directions[LEFT] -= 5

        if self.speed_directions[RIGHT] > 0:
            for i in range(self.speed):
                if self.pos[0] // tile + 1 not in level_map[self.pos[1] // 50] and \
                        self.pos[0] // tile + 1 not in level_map[self.pos[1] // 50 + 1]:
                    self.pos[0] += 1
                    if self.camera_pos[0] + self.display_width < len(level_map[0]) * tile and \
                            self.pos[0] > self.camera_pos[0] + self.display_width // 2:
                        self.camera_pos[0] += 1
            self.speed_directions[RIGHT] -= 5

        if self.speed_directions[UP] > 0:
            self.can_jump = False
            if self.is_jumping >= self.jump_height:
                self.speed_directions[UP] -= 5
            for i in range(self.speed_directions[UP]):
                if ((self.pos[0] + 1) // tile not in level_map[(self.pos[1] - 1) // 50]) and \
                        ((self.pos[0] - 1) // tile + 1 not in level_map[(self.pos[1] - 1) // 50]):
                    self.pos[1] -= 1
                    if self.camera_pos[1] > 0 and self.pos[1] < self.camera_pos[1] + self.display_height // 2:
                        self.camera_pos[1] -= 1
                else:
                    self.speed_directions[UP] = 0
            self.is_jumping += self.speed_directions[UP]
        else:
            for i in range(self.jump_speed):
                if ((self.pos[0] + 1) // tile not in level_map[(self.pos[1] + 1) // 50 + 1]) and \
                        ((self.pos[0] - 1) // tile + 1 not in level_map[(self.pos[1] + 1) // 50 + 1]):
                    self.can_jump = False
                    self.pos[1] += 1
                    if self.camera_pos[1] + self.display_height < len(level_map) * tile and \
                            self.pos[1] > self.camera_pos[1] + self.display_height // 2:
                        self.camera_pos[1] += 1
                else:
                    self.can_jump = True
                    self.is_jumping = 0



