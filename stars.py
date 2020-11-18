import pygame
import random

from const import *


class Zvezda:

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s


class GeneratorZvezd:

    def __init__(self, s, p, d, sz, col):
        self.s = s
        self.p = p
        self.d = d
        self.zvezdi = []
        self.dl = 0
        self.sz = sz
        self.col = col

        y = 0
        while y < высотаЭкрана:
            self.spawn(y)
            y = y + self.d

    def update(self, dt):

        mz = []
        for z in self.zvezdi:
            z.y = z.y + z.s * dt
            if z.y > высотаЭкрана:
                mz.append(z)

        for z in mz:
            self.zvezdi.remove(z)

        self.dl = self.dl + self.s * dt

        if self.dl >= self.d:
            self.spawn(-5)

    def draw(self, dis):
        for z in self.zvezdi:
            pygame.draw.circle(dis, self.col, (int(z.x), int(z.y)), self.sz)

    def spawn(self, y):
        for i in range(self.p):
            z = Zvezda(random.randint(5, ширинаЭкрана - 5), y, self.s + random.randrange(self.s * 0.6) - self.s * 0.3)
            self.zvezdi.append(z)
        self.dl = 0


gen = [
    GeneratorZvezd(базоваяСкорость // 4,    1, 3, 1, (100, 100, 50)),
    GeneratorZvezd(базоваяСкорость // 2,    1, 20, 2, (200, 200, 100)),
    GeneratorZvezd(базоваяСкорость,         1, 40, 3, (240, 240, 200))
]


def stars_update(dt, экран):
    for g in gen:
        g.update(dt)
        g.draw(экран)
