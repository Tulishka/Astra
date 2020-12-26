import pygame

from const import *


class Player:
    def_upr = [
        {
            'вверх': pygame.K_w,
            'вниз': pygame.K_s,
            'вправо': pygame.K_d,
            'влево': pygame.K_a,
            'буст': pygame.K_SPACE,
        },
        {
            'вверх': pygame.K_UP,
            'вниз': pygame.K_DOWN,
            'вправо': pygame.K_RIGHT,
            'влево': pygame.K_LEFT,
            'буст': pygame.K_KP0,
        }]

    def __init__(self, player_number):

        self.number = player_number

        self.pics = [
            pygame.transform.scale2x(
                pygame.transform.scale2x(pygame.image.load("img/" + str((player_number-1)%2+1) + "-" + str(i + 1) + ".png")))
            for i in range(3)]

        self.fly_slow = [self.pics[0], self.pics[1]]
        self.fly_fast = [self.pics[1], self.pics[2]]

        self.width = self.pics[0].get_width()
        self.height = self.pics[0].get_height()

        self.fly_ani = self.fly_slow

        self.upr = Player.def_upr[(player_number - 1)%len(Player.def_upr)]

        self.x = game_width // 2 - self.width // 2
        self.y = высотаЭкрана - self.height * 2

        self.sx = ширинаЭкрана / 3
        self.sy = self.sx

        self.time = 0
        self.fps = 40

        self.spd = 1

        self.left = (player_number - 1) * game_width
        self.min_x = 0
        self.max_x = game_width - self.width

        self.min_y = 0
        self.max_y = высотаЭкрана - self.height

    def draw(self, dis):
        dis.blit(self.fly_ani[int(self.time * self.fps) % len(self.fly_ani)], (self.left + self.x, self.y))

    def update(self, keys, dt):

        if keys[self.upr['вверх']]:
            self.y = self.y - self.sy * dt

        if keys[self.upr['вниз']]:
            self.y = self.y + self.sy * dt

        if keys[self.upr['влево']]:
            self.x = self.x - self.sx * dt

        if keys[self.upr['вправо']]:
            self.x = self.x + self.sx * dt

        if self.x < self.min_x:
            self.x = self.min_x

        if self.x > self.max_x:
            self.x = self.max_x

        if self.y < self.min_y:
            self.y = 0

        if self.y > self.max_y:
            self.y = self.max_y

        self.time += dt

    def set_spd(self, val):
        self.fly_ani = self.fly_fast if val > 1 else self.fly_slow
        self.spd = val
