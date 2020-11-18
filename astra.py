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
spd = 1
spd_target = 1
trans_time = 2
spd_acl = 0

players = [Player(1), Player(2)]

while 1:
    deltaTime = часы.get_time() * 0.001

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            spd_target = 1 if spd_target > 1 else 8
            for x in players:
                x.set_spd(spd_target)
            spd_acl = 0

    keys = pygame.key.get_pressed()
    экран.fill(цветФона)
    # =======================================

    if spd != spd_target:
        if spd_acl == 0:
            spd_acl = (spd_target - spd) / trans_time
        else:
            spd = spd + spd_acl * deltaTime
            if (spd_acl < 0 and spd < spd_target) or (spd_acl > 0 and spd > spd_target):
                spd = spd_target

    stars_update(spd * deltaTime, экран)

    for player in players:
        player.update(keys, deltaTime)
        player.draw(экран)

    # =======================================
    pygame.display.flip()
    часы.tick(60)
