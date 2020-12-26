import pygame

from const import *
from igrok import Player
from stars import GeneratorZvezd


class PlayerGame:

    def __init__(self, player_no, display):
        self.display = display
        self.player_no = player_no
        self.bound = ((player_no-1) * game_width, player_no * game_width)
        self.stars_gen = [
            GeneratorZvezd(базоваяСкорость // 4, 1, 3 * players_num, 1, (100, 100, 50), self.bound),
            GeneratorZvezd(базоваяСкорость // 2, 1, 20 * players_num, 2, (200, 200, 100), self.bound),
            GeneratorZvezd(базоваяСкорость     , 1, 40 * players_num, 3, (240, 240, 200), self.bound)
        ]
        self.player=Player(player_no)
        self.spd = 1
        self.spd_target = 1
        self.trans_time = 2
        self.spd_acl = 0

    def event(self, event):
        if event.type == pygame.KEYDOWN and event.key == self.player.upr['буст']:
            self.spd_target = 1 if self.spd_target > 1 else 8
            self.player.set_spd(self.spd_target)
            self.spd_acl = 0


    def update(self, deltaTime, keys):

        if self.spd != self.spd_target:
            if self.spd_acl == 0:
                self.spd_acl = (self.spd_target - self.spd) / self.trans_time
            else:
                self.spd = self.spd + self.spd_acl * deltaTime
                if (self.spd_acl < 0 and self.spd < self.spd_target) or (self.spd_acl > 0 and self.spd > self.spd_target):
                    self.spd = self.spd_target

        for g in self.stars_gen:
            g.update(self.spd * deltaTime)
            g.draw(self.display)

        self.player.update(keys, deltaTime)
        self.player.draw(self.display)

