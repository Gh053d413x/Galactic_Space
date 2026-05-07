"Module for Assets"

import pygame

import config

pygame.mixer.init()

# -------------------------------------
try:
    class RawTextures:
        """Base Class for Unscaled Textures, Only use for scaling!"""
        # Player
        player0_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/player/player0.png")

        # Enemy
        enemy0_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/enemy/enemy0.png")

        # Bullet
        bullet_blank_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/bullet/bullet-1.png")

        # Powerup
        wrench_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/powerUp/powerUp0.png")
        power_wrench_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/powerUp/powerUp1.png")
        ammo_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/powerUp/powerUp2.png")

        # UI
        game_over_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/ui/txt/game_over.png")


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
            wrench = pygame.transform.scale_by(RawTextures.wrench_unscaled, config.SPRITE_SCALING)
            power_wrench = pygame.transform.scale_by(RawTextures.power_wrench_unscaled, config.SPRITE_SCALING)
            ammo = pygame.transform.scale_by(RawTextures.ammo_unscaled, config.SPRITE_SCALING)
            

        class UI:
            """UI Class for Textures"""
            panel_01 = pygame.image.load(f"{config.WIN_PATH}/textures/ui/panel/panel_01.png")
            game_over = pygame.transform.scale_by(RawTextures.game_over_unscaled, config.SPRITE_SCALING)


    class Sounds:
        """Base Class for Sounds"""

        entity_damage = pygame.mixer.Sound(f"{config.WIN_PATH}/sounds/entity_damage.wav")
        player_death = pygame.mixer.Sound(f"{config.WIN_PATH}/sounds/player_death.wav")
        player_shoot = pygame.mixer.Sound(f"{config.WIN_PATH}/sounds/player_shoot.wav")


    class Music:
        """Base Class for Music"""

        invincibility = f"{config.WIN_PATH}/music/invincibility.wav"

    def load_music(song, songhint: str = ""):
        pygame.mixer.music.load(filename=song, namehint=songhint)

except Exception as e:
    config.error = 1010
    config.error_text = f"An error occured while loading one or more assets!\nError: {e}"
    # This automatically gets the current file's absolute path
    config.error_origin = config.pathlib.Path(__file__).resolve()


# -------------------------------------

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")
    