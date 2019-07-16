import pygame
import random
from pygame.locals import *
from pathlib import Path


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        if Path('./Icons/cloud.png').is_file():
            self.image = pygame.transform.scale(pygame.image.load('./Icons/cloud.png'), (100,100)).convert()
            self.image.set_colorkey((255, 255, 255), RLEACCEL)
        else:
            self.image = pygame.Surface((100, 100))
            self.image.fill((125, 255, 128))
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600))
        )

    def update(self, lateral, horizontal):
        self.rect.move_ip(lateral, horizontal)
        if self.rect.right < 0:
            self.kill()

