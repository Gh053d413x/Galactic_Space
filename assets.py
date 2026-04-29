"Module for Assets"

import pygame

import config

# -------------------------------------

class RawTextures:
    """Base Class for Unscaled Textures, Only use for scaling!"""
    # Player
    player0_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/player/player0.png")

    # Enemy
    enemy0_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/enemy/enemy0.png")

    # Bullet
    bullet_blank_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/bullet/bullet-1.png")

    # Powerup
    heart_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/powerUp/powerUp0.png")
    energy_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/powerUp/powerUp2.png")

    # UI


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
        blank = pygame.transform.scale_by(RawTextures.bullet_blank_unscaled, config.SPRITE_SCALING)
    

    class PowerUp:
        """PowerUp Class for Textures"""
        heart = pygame.transform.scale_by(RawTextures.heart_unscaled, config.SPRITE_SCALING)
        energy = pygame.transform.scale_by(RawTextures.energy_unscaled, config.SPRITE_SCALING)


    class UI:
        """UI Class for Textures"""
        panel_01 = pygame.image.load(f"{config.WIN_PATH}/textures/ui/panel/panel_01.png")

# -------------------------------------

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")
    