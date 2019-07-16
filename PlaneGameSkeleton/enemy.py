import pygame
import random
from pygame.locals import *
from pathlib import Path


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        if Path('./Icons/small-plane.png').is_file():
            self.image = pygame.transform.scale(pygame.image.load('./Icons/small-plane.png'), (50, 50)).convert()
            self.image.set_colorkey((0, 0, 0), RLEACCEL)
        else:
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(
            center=(820, random.randint(0, 600))
        )
        # self.speed = random.randint(5, 20)

    def update(self, lateral, horizontal):
        # self.rect.move_ip(-self.speed, 0)
        self.rect.move_ip(lateral, horizontal)
        if self.rect.right < 0:
            self.kill()
