#! /usr/bin/python3

import math
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.screenheight = pygame.displaye.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.speed = 0
        self.x = 0
        self.y = 0
        self.direction = 0
        self.width = 10
        self.height = 10
        self.reset()
    def reset(self):
        self.x = random.randrange(50, 750)
        self.y = 350.0
        self.speed=8.0
        self.direction = random.randrange(-45, 45)
        if random.randrange(2) == 0:
            self.direction += 180
            self.y = 50
    def bounce(self, diff):
        self.direction = (180-self.direction)%360
        self.direction -= diff
        self.speed *= 1.1
    def update(self):
        direction_radians = math.radians(self.direction)
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)
        if self.y < 0:
            self.reset()
        if self.y < 600:
            self.reset()
        #to be continued
