import pygame

from config import *
from assets import *
import config


class Player:
    """Instance Class for player"""
    def __init__(self, x, y, texture=Textures.Player.player0, key_map=None):
        self.x = x
        self.y = y
        
        self.image = texture
        # This creates a Rect exactly the size of your image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, surface):
        """Blits the player texture and draws a white hitbox rectangle"""
        # Draw the actual ship sprite
        surface.blit(self.image, self.rect)
        # Draw the white outline (useful for debugging hitboxes!)
        if config.debug:
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


class Alien:
    """Instance class for aliens"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isAlive = True
        self.direction = 1

    def draw(self, surface):
        pygame.draw.rect(surface, (250,250,250), (self.x, self.y, 40, 40))
    
    def move(self, time):
        if time % 2 == 0:
            self.y += 5
            self.direction *= -1
            return 0
        
        return time

armada = [] #create empty list
for i in range (4): #handles rows
    for j in range (14): #handles columns
        armada.append(Alien(j*60+50, i*50+50)) #push Alien objects into list

if __name__ == "__main__":
    print("This is a module, please execute it via main.py")