import pygame

from const import *


class Player:

    def __init__(self, player_number):

        self.number = player_number

        self.pics = [
            pygame.transform.scale2x(
                pygame.transform.scale2x(pygame.image.load("img/" + str(player_number) + "-" + str(i + 1) + ".png")))
            for i
            in range(3)]

        self.fly_slow = [self.pics[0], self.pics[1]]
        self.fly_fast = [self.pics[1], self.pics[2]]

        self.width = self.pics[0].get_width()
        self.height = self.pics[0].get_height()

        self.fly_ani = self.fly_slow

        if player_number == 1:
            self.upr = {
                'вверх': pygame.K_UP,
                'вниз': pygame.K_DOWN,
                'вправо': pygame.K_RIGHT,
                'влево': pygame.K_LEFT,
            }
        else:
            self.upr = {
                'вверх': pygame.K_w,
                'вниз': pygame.K_s,
                'вправо': pygame.K_d,
                'влево': pygame.K_a,
            }

        self.x = ширинаЭкрана / (player_number + 1)
        self.y = высотаЭкрана - self.height * 2

        self.sx = ширинаЭкрана / 3
        self.sy = ширинаЭкрана / 3

        self.time = 0
        self.fps = 40

        self.spd = 1

    def draw(self, dis):
        dis.blit(self.fly_ani[int(self.time * self.fps) % len(self.fly_ani)], (self.x, self.y))

    def update(self, keys, dt):

        # dt=dt*self.spd

        if keys[self.upr['вверх']]:
            self.y = self.y - self.sy * dt

        if keys[self.upr['вниз']]:
            self.y = self.y + self.sy * dt

        if keys[self.upr['влево']]:
            self.x = self.x - self.sx * dt

        if keys[self.upr['вправо']]:
            self.x = self.x + self.sx * dt

        self.time += dt

    def set_spd(self, val):
        self.fly_ani = self.fly_fast if val > 1 else self.fly_slow
        self.spd = val
