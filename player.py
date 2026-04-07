import pygame

from config import *
from assets import *


class Player:
    def __init__(self, x, y, texture=Textures.Player.player0, key_map=None):
        self.image = texture
        # This creates a Rect exactly the size of your image
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        """Blits the player texture and draws a white hitbox rectangle"""
        # Draw the actual ship sprite
        surface.blit(self.image, self.rect)
        # Draw the white outline (useful for debugging hitboxes!)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 1)

    # In player.py -> handle_input
    def handle_input(self, key):
        # 1. Get Input
        up = key[pygame.K_UP] or key[pygame.K_w]
        down = key[pygame.K_s] or key[pygame.K_DOWN]
        left = key[pygame.K_a] or key[pygame.K_LEFT]
        right = key[pygame.K_d] or key[pygame.K_RIGHT]

        # 2. Apply Movement
        self.rect.x += (right - left) * 15
        self.rect.y += (down - up) * 15

        # 3. The Boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Screen.Size.w:
            self.rect.right = Screen.Size.w
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Screen.Size.h:
            self.rect.bottom = Screen.Size.h