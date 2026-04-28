"Module for Assets"

import pygame

import config

# -------------------------------------

class RawTextures:
    """Base Class for Unscaled Textures, Only use for scaling!"""
    player0_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/player/player0.png")

    enemy0_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/enemy/enemy0.png")

    bullet_blank = pygame.image.load(f"{config.WIN_PATH}/textures/bullet/bullet-1.png")


class Textures:
    """Base Class for Textures"""

    class Player:
        """Player Class for Textures"""
        player0 = pygame.transform.scale_by(RawTextures.player0_unscaled, config.SPRITE_SCALING)


    class Enemy:
        """Enemy Class for textures"""
        enemy0 = pygame.transform.scale_by(RawTextures.enemy0_unscaled, config.SPRITE_SCALING)


    class Bullet:
        """Bullet Class for Textures"""
        blank = pygame.transform.scale_by(RawTextures.bullet_blank, config.SPRITE_SCALING)

# -------------------------------------

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")
    