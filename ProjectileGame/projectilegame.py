import pygame
from pygame.locals import *

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
