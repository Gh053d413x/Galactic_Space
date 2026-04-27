"Config Module"

import os
import subprocess

WIN_PATH = os.getcwd()
SPRITE_SCALING = 6

timer = 1

difficulty = 0

debug = True

class Screen:
    class Size:
        w = 922
        h = 691


class Game:
    title = "Galactic Space"
    running = True
    players = []

if __name__ == "__main__":
    print("Execution of module detected! Running Main.py")
    subprocess.run(f"{WIN_PATH}/main.py", shell=True)