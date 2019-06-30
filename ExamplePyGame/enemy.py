import pygame
import random
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.transform.scale(pygame.image.load('./Icons/small-plane.png'), (50,50)).convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        # self.surf = pygame.Surface((20, 10))
        # self.surf.fill((255, 255, 255))
        self.rect = self.image.get_rect(
            center=(820, random.randint(0, 600))
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
