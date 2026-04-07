import pygame

from config import *

class RawTextures:
    """Base Class for Unscaled Textures, Only use for scaling!"""
    player0_unscaled = pygame.image.load(f"{WIN_PATH}/textures/player/player0.png")

    bullet_normal = pygame.image.load(f"{WIN_PATH}/textures/bullet/bullet0.png")


class Textures:
    """Base Class for Textures"""

    class Player:
        """Sprites Class for Textures"""
        player0 = pygame.transform.scale_by(RawTextures.player0_unscaled, SPRITE_SCALING)

    class Bullet:
        """Bullet Class for Textures"""
        normal = pygame.transform.scale_by(RawTextures.bullet_normal, SPRITE_SCALING)

if __name__ == "__main__":
    print("This is a module, please execute it via main.py")