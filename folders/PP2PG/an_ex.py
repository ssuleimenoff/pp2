import pygame, sys
from pygame.locals import *
import math
import random
import time
from pygame import mixer

# initial game configs
screen_width = 800
screen_height = 600
fps = 60
car_speed = 1

# enemy car configs
side_list = ['left', 'middle', 'right']

class Background(pygame.sprite.Sprite):
    def __init__(self):
        self.size = (screen_width, screen_height)
        self.bg_num = 1
        self.image = pygame.transform.scale(pygame.image.load(f'./assets/bg{self.bg_num}.png'), self.size)

    def draw(self):