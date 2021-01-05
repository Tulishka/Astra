import pygame
from const import *

from playerGame import PlayerGame

# =======================================

pygame.init()

экран = pygame.display.set_mode(size=размерЭкрана,
                                     flags=pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption('Astra')

часы = pygame.time.Clock()
шрифт = pygame.font.SysFont("arial", 14)

playersGames = [PlayerGame(p + 1, экран) for p in range(players_num)]

while 1:
    deltaTime = часы.get_time() * 0.001

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            exit()
        for g in playersGames:
            g.event(event)

    keys = pygame.key.get_pressed()
    экран.fill(цветФона)
    # =======================================

    for g in playersGames:
        g.update(deltaTime,keys)
        if (g.player_no<players_num):
            pygame.draw.line(экран,(255,255,255),(game_width*g.player_no,0),(game_width*g.player_no,высотаЭкрана),2)

    # =======================================
    pygame.display.flip()
    часы.tick(60)
