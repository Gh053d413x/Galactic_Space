"Module for Entities"

import pygame

import assets
from config import *
from assets import *
import config


class Player:
    """Instance Class for player"""
    def __init__(self, x: int, y: int, texture: pygame.surface.Surface = Textures.Player.player0):
        self.x = x
        self.y = y
        self.speed = 8
        
        self.image = texture
        # This creates a Rect exactly the size of your image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, surface):
        """Blits the player texture\n
        Draws a white hitbox rectangle (if debug mode is on)"""
        # Draw the actual ship sprite
        surface.blit(self.image, self.rect)
        # Draw the white outline (useful for debugging hitboxes!)
        if config.debug:
            pygame.draw.rect(surface, (51, 255, 51), self.rect, 1)

    # In player.py -> handle_input
    def handle_input(self, key):
        # 1. Get Input
        up = key[pygame.K_UP] or key[pygame.K_w] or key[pygame.K_i] or key[pygame.K_o]
        down = key[pygame.K_s] or key[pygame.K_DOWN] or key[pygame.K_k]
        left = key[pygame.K_a] or key[pygame.K_LEFT] or key[pygame.K_j]
        right = key[pygame.K_d] or key[pygame.K_RIGHT] or key[pygame.K_l]

        # 2. Apply Movement
        if up:
            self.rect.y -= self.speed
        if down:
            self.rect.y += self.speed
        if left:
            self.rect.x -= self.speed
        if right:
            self.rect.x += self.speed

        # self.rect.x += (right - left) * 15
        # self.rect.y += (down - up) * 15

        # 3. The Boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Screen.Size.w:
            self.rect.right = Screen.Size.w
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Screen.Size.h:
            self.rect.bottom = Screen.Size.h


class Enemy:
    """Instance class for enemies"""
    def __init__(self, x: int, y: int, image: pygame.surface.Surface, enemy_type: int):
        self.x = x
        self.y = y
        self.image = image
        self.enemy_type = enemy_type

        self.isAlive = True
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, surface):
        """Blits the enemy texture\n
        Draws a white hitbox rectangle (if debug mode is on)"""
        if self.enemy_type == 0:
            img = pygame.transform.flip(self.image, False, True)
            surface.blit(img, (self.x, self.y))
        # Draw the white outline (useful for debugging hitboxes!)
        if config.debug:
            pygame.draw.rect(surface, (255, 51, 51), self.rect, 1)
    
    def move(self, time):
        if time % 2 == 0:
            self.y += 5
            return 0
        
        return time

    def update(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

# armada = [] #create empty list
# for i in range (4): #handles rows
#     for j in range (14): #handles columns
#         armada.append(Enemy(j*60+50, i*50+50, assets.Textures.Enemy.enemy0, 0)) #push Enemy objects into list

if __name__ == "__main__":
    print("Execution of module detected! Running Main.py")
    subprocess.run(f"{WIN_PATH}/main.py", shell=True)