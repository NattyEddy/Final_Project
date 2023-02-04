import sys
import os
import pygame
from items import *
from cursor import *

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# Global constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768
FRAME_RATE = 60 # turn down to 60 or 72 if you need to (for performance or to slow the game down)

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

START_TIME = pygame.time.get_ticks()

# background setup
SCREEN_RECT = screen.get_rect()
background = pygame.image.load(os.path.join("assets", "bamboo_wall.png")).convert_alpha()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# cursor thing
cursor = Cursor()

# list to store all the sprites thrown
items = []

# initial items that allow the program to make more of it
# consider this as reference
apple = Item("apple.png", -500, -500)                                 # not in the window ever
melon = Item("melon_slice.png", -500, -500)                           # not in the window ever
glistering_melon = Item("glistering_melon_slice.png", -500, -500)     # not in the window ever
rocket = Item("firework_rocket.png", -500, -500)                      # not in the window ever

# create sprite groups
apple_sprites = pygame.sprite.Group()
melon_sprites = pygame.sprite.Group()
glistering_melon_sprites = pygame.sprite.Group()
rocket_sprites = pygame.sprite.Group()
cursors = pygame.sprite.Group()

sprite_groups = [apple_sprites, melon_sprites, glistering_melon_sprites, rocket_sprites, cursors]

# function to spawn an item
def spawn_item(item, sprite, group, x_low, x_high, launch_low, launch_high):
    item = Item(sprite, r.randint(x_low, x_high), 800)
    item.launch(launch_low, launch_high)
    group.add(item)
    items.append(item)

# other variables related to relative points in time and game status
point_in_time = 0
game_time = 0
play_time = 0
stop_game = True

while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()

    # Keyboard events
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]:
        play_time = pygame.time.get_ticks()
        point_in_time = 0
        for group in sprite_groups:
            group.empty()
        items.clear()
        stop_game = False
        print("Game has started!")

    # Mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
    # (x, y) coordinate

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        cursor = Cursor()
        cursor.tp(mouse_pos[0] - (cursor.rect.width/2), mouse_pos[1] - (cursor.rect.height/2)) # Teleport centre of body to cursor
        cursors.add(cursor)
    else:
        cursor.tp(-1, -1)
        cursors.empty()
        
    if mouse_buttons[2]:  # If right mouse pressed
        pass  # Replace this line
    """
    UPDATE section - manipulate everything on the screen
    """
    # time variables
    UPTIME = pygame.time.get_ticks()
    
    if stop_game == False:
        # starts game_time and point_in_time to be in sync with the spacebar being pressed
        game_time = UPTIME - play_time
        
        # STAGES - the game launches fruits and rockets in different quantities and intervals based on the stage in the game
        # each if statement outlines what will happen between x and y time, every z milliseconds
        
        # STAGE ONE - starts at 2 seconds and ends at x ms, every 3 seconds
        # launches one of either an apple or melon
        if game_time > 2000 and game_time <= 15000 and game_time - point_in_time > 3000:
            rng_sprites = r.randint(0, 1)
            if rng_sprites == 0:
                spawn_item(apple, "apple.png", apple_sprites, 80, 1100, 10, 12)
                point_in_time = game_time
            else:
                spawn_item(melon, "melon_slice.png", melon_sprites, 80, 1100, 10, 12)
                point_in_time = game_time

        # STAGE ONE A - starts at 15 seconds and ends at 18 seconds, once
        # launches one rocket
        if game_time > 15000 and game_time <= 18000 and game_time - point_in_time > 3000:
            spawn_item(rocket, "firework_rocket.png", rocket_sprites, 400, SCREEN_WIDTH - 400, 0, 0) # the zeroes don't matter here, adding for clarification in code
            point_in_time = game_time
    
        # STAGE TWO - starts at 18 seconds and ends at 30 seconds, every two seconds
        # launches 1-2 items
        if game_time > 18000 and game_time <= 30000 and game_time - point_in_time > 2000:
            for quantity in range(r.randint(1, 2)):
                rng_sprites = r.randint(0, 3)
                if rng_sprites == 1:
                    spawn_item(apple, "apple.png", apple_sprites, 80, 1100, 10, 12)
                    point_in_time = game_time
                elif rng_sprites == 2:
                    spawn_item(melon, "melon_slice.png", melon_sprites, 80, 1100, 10, 12)
                    point_in_time = game_time
                elif rng_sprites == 3:
                    spawn_item(glistering_melon, "glistering_melon_slice.png", glistering_melon_sprites, 80, 1100, 10, 12)
                    point_in_time = game_time
                else:
                    spawn_item(rocket, "firework_rocket.png", rocket_sprites, 80, 1100, 0, 0)
                    point_in_time = game_time

        # STAGE THREE - starts at 30 seconds, every second
        # launches 1-3 items
        if game_time > 30000 and game_time - point_in_time > 1000:
            for quantity in range(r.randint(1, 3)):
                rng_sprites = r.randint(0, 3)
                if rng_sprites == 1:
                    spawn_item(apple, "apple.png", apple_sprites, 80, 1100, 9, 12)
                    point_in_time = game_time
                elif rng_sprites == 2:
                    spawn_item(melon, "melon_slice.png", melon_sprites, 80, 1100, 9, 12)
                    point_in_time = game_time
                elif rng_sprites == 3:
                    spawn_item(glistering_melon, "glistering_melon_slice.png", glistering_melon_sprites, 80, 1100, 9, 12)
                    point_in_time = game_time
                else:
                    spawn_item(rocket, "firework_rocket.png", rocket_sprites, 80, 1100, 0, 0)
                    point_in_time = game_time

    # update, kill, and remove for every item; also stops game
    for item in items:
        item.update()
        if pygame.sprite.collide_rect(cursor, item):
            if item.sprite == "firework_rocket.png":
                for group in sprite_groups:
                    group.empty()
                items.clear()
                stop_game = True
                print("Hit a rocket, GAME OVER!")
            else:
                item.kill()
                items.remove(item)
        elif item.sprite == "firework_rocket.png" and item.rect.y < -200: # unessential to gameplay
            item.kill()
            items.remove(item)
        elif item.rect.y >= 2000:
            stop_game = True
            items.remove(item)
            print("Failed to slice fruit, GAME OVER!")

    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour
    screen.blit(background, SCREEN_RECT)

    for group in sprite_groups:
        group.draw(screen)

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second

