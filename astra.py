import pygame

from const import *
from igrok import Player
from stars import stars_update

# =======================================
pygame.init()

экран = pygame.display.set_mode(размерЭкрана)
pygame.display.set_caption('Astra ')

часы = pygame.time.Clock()
шрифт = pygame.font.SysFont("arial", 14)

# =======================================


while 1:
    deltaTime = часы.get_time() * 0.001

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            exit()

    keys = pygame.key.get_pressed()
    экран.fill(цветФона)
    # =======================================



    stars_update(deltaTime, экран)



    # =======================================
    pygame.display.flip()
    часы.tick(60)
