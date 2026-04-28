# Galactic Space Reborn
# Copyright (c) Ghosted Alex 2026
# Made under the MIT license: https://opensource.org/license/mit

VER = "dev_build.4"

import os
import random
import pygame

import assets
import config
import entity
import bullet

FPS = pygame.time.Clock()

pygame.init()

monocraft = pygame.font.Font(f"{config.WIN_PATH}/fonts/Monocraft.ttf", 30)

scr = pygame.display.set_mode((config.Screen.Size.w, config.Screen.Size.h))

pygame.display.set_caption(config.Game.title)

# ... (imports and Game class stay the same)

# FIX: Removed the ', 0' so it uses the default texture correctly
player = entity.Player(config.Screen.Size.w / 2 - 20, config.Screen.Size.h / 2 - 20)
config.Game.players.append(player)

bullet_normal = bullet.Normal(player.x+28, player.y)

a1 = entity.Enemy(random.randint(16, 906), -5, assets.Textures.Enemy.enemy0, 0)

print(config.Game.players)

enemies = []
bullets = []

while config.Game.running:
    FPS.tick(60)

    # for i in range(len(entity.armada)):
    #     timer = entity.armada[i].move(timer)

    # Change this part at the top
    if config.blink_timer < 60:
        config.blink_timer += 1

    fps_display = monocraft.render(f"FPS: {FPS.get_fps()}", False, (255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.Game.running = False
        
        # Check for the initial key press here
        if event.type == pygame.KEYDOWN:
            if config.debug:
                if event.key == pygame.K_KP_PLUS:
                    if player.energy < 100:
                        player.energy += 10
                if event.key == pygame.K_KP_MINUS:
                    if player.health < 100:
                        player.health += 10
            if event.key == pygame.K_SPACE or event.key == pygame.K_z:
                # Create the bullet at the player's current position
                if player.energy > 0:
                    new_bullet = bullet.Normal(player.rect.centerx, player.rect.top)
                    bullets.append(new_bullet)
                    player.energy -= 5
                else:
                    config.blink_timer = 0
                        
            if event.key == pygame.K_F12:
                config.debug = not config.debug

    if not config.Game.running:
        break

    # Replace that whole 'for i in range(2)' block with this:
    if config.blink_timer < 60:
        # This checks if the timer is in the first or second half of a 30-frame cycle
        if (config.blink_timer // 15) % 2 == 0:
            config.BACKGROUND_ENERGY_COLOR = (166, 51, 51) # Red
        else:
            config.BACKGROUND_ENERGY_COLOR = (15, 15, 15)  # Dark
    else:
        config.BACKGROUND_ENERGY_COLOR = (15, 15, 15) # Default Dark
    
    keys = pygame.key.get_pressed()

    # RENDERING
    # Inside your "RENDERING" section in main.py
    scr.fill((0, 0, 0))

    # Update and Draw Bullets
    for b in bullets[:]: # [:] creates a copy so we can safely remove items
        b.update()
        b.draw(scr)
        
        # Optimization: Delete bullet if it leaves the screen
        if b.rect.bottom < 0:
            bullets.remove(b)

    player.handle_input(keys)
    player.draw(scr)

    config.delay -= 1
    if config.delay <= 0:
        config.delay = 60
        # Create a new enemy and ADD it to the list instead of overwriting
        new_enemy = entity.Enemy(random.randint(48, 874), -75, assets.Textures.Enemy.enemy0, 0)
        enemies.append(new_enemy)

    # --- ONE LOOP TO RULE THEM ALL ---
    for e in enemies[:]:
        e.move()    
        e.update()

        if e.y > config.Screen.Size.h:
            enemies.remove(e)
            continue

        # Check Bullet Collision
        for b in bullets[:]:
            if e.rect.colliderect(b.rect):
                if e in enemies: enemies.remove(e)
                if b in bullets: bullets.remove(b)
                break # Enemy is dead, stop checking bullets for it

        # Check Player Collision
        if e.rect.colliderect(player.rect):
            if config.difficulty == 0:
                player.health -= 10
            else:
                player.health -= 15
            if e in enemies: enemies.remove(e)

        e.draw(scr) # Draw it here

    pygame.draw.rect(scr, config.PANEL_COLOR, (0, config.Screen.Size.h-45, config.Screen.Size.w, config.Screen.Size.h))

    # pygame.draw.rect(surface, (51, 255, 51), self.rect, 1)
    pygame.draw.rect(scr, config.BACKGROUND_HEALTH_COLOR, (15, 656, 400, 25))

    pygame.draw.rect(scr, config.HEALTH_COLOR_DRAIN, (15, 656, player.health_drain*4, 25))

    if player.health > 50:
        pygame.draw.rect(scr, config.HEALTH_COLOR_HIGH, (15, 656, player.health*4, 25))
    if 50 >= player.health > 25:
        pygame.draw.rect(scr, config.HEALTH_COLOR_MED, (15, 656, player.health*4, 25))
    if player.health <= 25:
        pygame.draw.rect(scr, config.HEALTH_COLOR_LOW, (15, 656, player.health*4, 25))
    if player.health <= 0:
        print("Game Over!")
        config.Game.running = False
    
    if player.health_drain > player.health:
        player.health_drain -= .1
    elif player.health_drain < player.health:
        player.health_drain = player.health

    # 1. Background Bar (The gray slot)
    # Starts at 507, width 400 (507 + 400 = 907)
    pygame.draw.rect(scr, config.BACKGROUND_ENERGY_COLOR, (507, 656, 400, 25))

    # 2. The Draining Logic
    # We calculate the width first
    energy_width = player.energy * 4

    # To make it "reverse," we push the X-coordinate forward by the missing amount
    # 507 + (400 - energy_width)
    reverse_x = 507 + (400 - energy_width)

    # 3. Draw the Energy Bar (Yellow)
    if player.energy > 0:
        pygame.draw.rect(scr, config.ENERGY_COLOR, (reverse_x, 656, energy_width, 25))

    if player.health > 100:
        player.health = 100
    if player.energy > 100:
        player.energy = 100

    pygame.display.flip()

pygame.quit()
