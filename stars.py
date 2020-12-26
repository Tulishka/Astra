import pygame
import random

from const import *


class Zvezda:

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s


class GeneratorZvezd:

    def __init__(self, s, p, d, sz, col, bound=(0, ширинаЭкрана)):
        self.s = s
        self.p = p
        self.d = d
        self.zvezdi = []
        self.dl = 0
        self.sz = sz
        self.col = col
        self.bound=bound

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
            z = Zvezda(random.randint(self.bound[0]+5, self.bound[1] - 5), y, self.s + random.randrange(self.s * 0.6) - self.s * 0.3)
            self.zvezdi.append(z)
        self.dl = 0


