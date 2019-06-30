import pygame
from pygame.locals import *

# Define our player object and call super to give it all the properties and methods of pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'player'


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.transform.scale(pygame.image.load('./Icons/jet.png'), (40, 40)).convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.move_size = 10


    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.move_size)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.move_size)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.move_size, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.move_size, 0)
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600