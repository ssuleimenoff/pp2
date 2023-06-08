import pygame,sys
from pygame.locals import *
import math
import random
import time
from pygame import mixer
# game initialliting
screen_width = 800
screen_height = 600
fps = 60
car_speed = 1
# enemy cars configs
side_list = ['left', 'middle', 'right']

class Backgorund(pygame.sprite.Sprite):
    def __init__(self):
        self.size = (screen_width, screen_height)
        self.bg_num = 1
        self.image = pygame.transform.scale(pygame.image.load(f"./assets/bg{self.bg_num}.png"), self.size)
        surf.blit(self.image, (0, 0))
        if self.bg_num < 2:
            self.bg_num += 1
        else:
            self.bg_num = 1


class EnemyCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = [75, 50]
        self.side = side_list[random.randint(0, 2)]
        self.image = pygame.transfrom.scale(pygame.image.load(f"./assets/{random.randint(1, 4)}_car_{self.side}.png"), self.size)
        self.rect = self.image.get_rect()
        match self.side:
            case 'left':
                self.rect.center = (370, 390)
            case 'middle':
                self.rect.center = (420, 390)
            case 'right':
                self.rect.center = (470, 390)

