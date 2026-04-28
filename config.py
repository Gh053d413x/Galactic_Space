"Config Module"

import os
import subprocess
import math

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
HEALTH_COLOR_DRAIN = (140, 67, 176) # Drain Color (Magenta)

ENERGY_COLOR = (219, 212, 53)

PANEL_COLOR = (69, 69, 69)
PANEL_REFLECTION_COLOR = (127, 127, 127)

blink_timer = 60

class Screen:
    class Size:
        w = 922
        h = 691

class Game:
    title = "Galactic Space Reborn"
    running = True
    players = []

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")
    