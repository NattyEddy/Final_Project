import os
import pygame


class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image_location = os.path.join("assets", "bullet.png") # yes I used the bullet asset lol
        self.image = pygame.image.load(image_location).convert_alpha()

        self.rect = pygame.Rect(0, 0, 2, 2)

    def tp(self, x, y):
        # move to whatever x and y is, will be used to tp to the mouse x and y position
        self.rect.x = x
        self.rect.y = y
        