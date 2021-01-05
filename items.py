import pygame
import random

from const import *


class Item:

    def __init__(self, x, y, sx, sy,images):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.images = images


class ItemGenerator:

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



