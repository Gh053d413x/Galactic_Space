# Galactic Space Reborn
# Copyright (c) Ghosted Alex 2026
# Made under the MIT license: https://opensource.org/license/mit

VER = "dev_build.3"

import os
import time
import pygame
import json
import tkinter.messagebox

WIN_PATH = os.getcwd()

FPS = pygame.Clock()

class screen:
    class size:
        w = 922
        h = 691

class game:
    running = True

class __unscaled__:
    """Base Class for Unscaled Textures, Only use for scaling!"""
    player0_unscaled = pygame.image.load(f"{WIN_PATH}/textures/player/player0.png")
    
class textures:
    """Base Class for Textures"""
    class player:
        """Sprites Class for Textures"""
        player0 = pygame.transform.scale_by(__unscaled__.player0_unscaled, 6)

scr = pygame.display.set_mode((screen.size.w, screen.size.h), pygame.RESIZABLE)

# Start Instance Classes--------------------------------------------------

class Player:
    def __init__(self, x, y, player, flags = []):
        self.x = x
        self.y = y
        self.w = 48
        self.h = 54
        self.flags = flags
        self.player = player
    
    def draw(self, surface):
        if self.player == 0:
            surface.blit(textures.player.player0, (self.x, self.y))
    
    def handle_input(self, key):
        if key[pygame.K_w] or key[pygame.K_UP]:
            self.y += -15
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.x += 15
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            self.y += 15
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.x += -15
        
        if key[pygame.K_w] and key[pygame.K_UP]:
            self.y += -30
        if key[pygame.K_d] and key[pygame.K_RIGHT]:
            self.x += 30
        if key[pygame.K_s] and key[pygame.K_DOWN]:
            self.y += 30
        if key[pygame.K_a] and key[pygame.K_LEFT]:
            self.x += -30

# End Instance Classes----------------------------------------------------

player0 = Player(461, 345, 0)

while game.running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
            pygame.quit()
            quit()

    scr.fill((0,0,0))

    player0.draw(scr)

    player0.handle_input(keys)

    pygame.draw.rect(scr, (255,255,255), (player0.x, player0.y, player0.w, player0.h), 1)

    pygame.display.flip()
    
    FPS.tick(30)