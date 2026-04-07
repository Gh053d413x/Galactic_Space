# Galactic Space Reborn
# Copyright (c) Ghosted Alex 2026
# Made under the MIT license: https://opensource.org/license/mit

VER = "dev_build.3"

import os
import pygame

from config import *
from assets import *

import player

FPS = pygame.time.Clock()


class Game:
    title = "Galactic Space"
    running = True
    players = []


scr = pygame.display.set_mode((Screen.Size.w, Screen.Size.h))

pygame.display.set_caption(Game.title)

# ... (imports and Game class stay the same)

# FIX: Removed the ', 0' so it uses the default texture correctly
player0 = player.Player(Screen.Size.w / 2 - 20, Screen.Size.h / 2 - 20)
Game.players.append(player0)

while Game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game.running = False

    if not Game.running:
        break

    keys = pygame.key.get_pressed()
    scr.fill((0, 0, 0))

    # BETTER: Loop through your list.
    # This makes adding more players/entities effortless later!
    for p in Game.players:
        p.handle_input(keys)
        p.draw(scr)

    pygame.display.flip()
    FPS.tick(30)

pygame.quit()
