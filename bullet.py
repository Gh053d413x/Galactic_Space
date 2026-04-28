"Module for Bullet"

import subprocess
import pygame
import config

class Normal:
    def __init__(self, x, y):
        # Center the thin bullet on the spawn point
        self.rect = pygame.Rect(x - 1, y, 3, 20)
        self.speed = 25

    def update(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        # Draw a simple white vertical line/rect
        pygame.draw.rect(surface, (255, 255, 255), self.rect)

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")