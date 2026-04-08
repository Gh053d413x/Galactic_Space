import pygame
import subprocess

from config import *

class Normal:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
        self.live = False

    def move(self, x, y):
        if self.live:
            self.y -= 5
        if self.y < 0:
            self.live = False
            self.x = self.player.x
            self.y = self.player.y
    
    def draw(self, surface):
        pygame.draw.rect(surface, (250,250,250), (self.x, self.y, 3, 20))

if __name__ == "__main__":
    print("Execution of module detected! Running Main.py")
    subprocess.run(f"{WIN_PATH}/main.py", shell=True)