import os
import pygame
import random as r

GRAVITY = 0.4

class Item(pygame.sprite.Sprite):
    def __init__(self, sprite, x, y):
        super().__init__()

        self.sprite = sprite # won't be redundant in update() and launch(), unless it is ig
        image_location = os.path.join("assets", self.sprite)
        self.image = pygame.image.load(image_location).convert_alpha()
        
        # get the size of the original image first
        self.original_size = self.image.get_size()
        # create an image three times larger
        self.image = pygame.transform.scale(self.image, (int(self.original_size[0]*10), int(self.original_size[1]*10)))
        
        # and then make the rectangle
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y_speed = 0

    def update(self):
        # gravity only applies if it is not a firework
        if self.sprite != "firework_rocket.png":
            self.y_speed += GRAVITY
        self.rect.y += self.y_speed

    def launch(self, low, high):
        # if it's not a firework, then it'll be thrown up by a random range determined in main.py, otherwise launch the rocket by 6
        if self.sprite != "firework_rocket.png":
            self.y_speed -= r.randrange(2*low, 2*high)
        else:
            self.y_speed -= 12