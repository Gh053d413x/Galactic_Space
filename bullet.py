"Module for Bullet"

import subprocess
import pygame
import config
import assets

class Normal:
    def __init__(self, x, y, image=assets.Textures.Bullet.blank):     
        self.image = image
        # Use the image's rect to handle positioning and collisions
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 25

    def update(self):
        # Move the rect, which is the "source of truth" for position
        self.rect.y -= self.speed

    def draw(self, surface):
        # Draw the actual image at the rect's current position
        surface.blit(self.image, self.rect)

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")