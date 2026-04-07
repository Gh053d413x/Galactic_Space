import os
import pygame

WIN_PATH = os.getcwd()
SPRITE_SCALING = 6

timer = 1

difficulty = 0

debug = False

class Screen:
    class Size:
        w = 922
        h = 691


class Game:
    title = "Galactic Space"
    running = True
    players = []

if __name__ == "__main__":
    print("This is a module, please execute it via main.py")