# Galactic Space Reborn
# Copyright (c) Ghosted Alex 2026
# Made under the MIT license: https://opensource.org/license/mit

VER = "dev_build.3"

import os
import pygame

from config import *
from assets import *
import config
import entity
import bullet

FPS = pygame.time.Clock()

pygame.init()

monocraft = pygame.font.Font(f"{WIN_PATH}/fonts/Monocraft.ttf", 30)

scr = pygame.display.set_mode((Screen.Size.w, Screen.Size.h))

pygame.display.set_caption(Game.title)

# ... (imports and Game class stay the same)

# FIX: Removed the ', 0' so it uses the default texture correctly
player0 = entity.Player(Screen.Size.w / 2 - 20, Screen.Size.h / 2 - 20)
Game.players.append(player0)

dart = bullet.Normal(player0.x+28, player0.y, player0)

print(Game.players)

while Game.running:
    FPS.tick(60)

    timer += 1

    for i in range(len(entity.armada)):
        timer = entity.armada[i].move(timer)

    fps_display = monocraft.render(f"FPS: {FPS.get_fps()}", False, (255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F12:
                if config.debug == False:
                    config.debug = True
                else:
                    config.debug = False


    if not Game.running:
        break

    keys = pygame.key.get_pressed()

    # RENDERING
    scr.fill((0, 0, 0))

    if config.debug:
        scr.blit(fps_display, (10, 10))

    # BETTER: Loop through list.
    # This makes adding more players/entities effortless later!
    for p in Game.players:
        p.handle_input(keys)
        p.draw(scr)

    #draw all enemies in list:
    for i in range (len(entity.armada)):
        entity.armada[i].draw(scr)

    a1 = entity.Enemy(400, 400, Textures.Enemy.enemy0)
    a1.draw(scr)

    pygame.display.flip()

pygame.quit()
