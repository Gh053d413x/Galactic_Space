"Config Module"

import os
import subprocess
import math
import pygame

WIN_PATH = os.getcwd()
SPRITE_SCALING = 6

delay = 60

difficulty = 0

debug = False

BACKGROUND_HEALTH_COLOR = (15, 15, 15)
BACKGROUND_ENERGY_COLOR = (15, 15, 15)

HEALTH_COLOR_HIGH = (50, 168, 82) # High Health Color (Green)
HEALTH_COLOR_MED = (166, 164, 51) # Medium Health Color (Yellow)
HEALTH_COLOR_LOW = (166, 51, 51) # Low Health Color (Red)
HEALTH_COLOR_DRAIN = (135, 242, 255) # Drain Color (Cyan)

ENERGY_COLOR = (219, 212, 53)

blink_timer = 60
health_blink_timer = 60

game_over = False

class Screen:
    "Base Class for Screen"
    class Size:
        "Size of Screen"
        w = 922
        "width: 922"
        h = 691
        "height: 691"

class Game:
    title = "Galactic Space Reborn"
    running = True
    players = []

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")
    