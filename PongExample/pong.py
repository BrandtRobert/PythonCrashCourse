import pygame
from pygame.locals import *
from pygame.time import Clock
import random

pygame.init()
clock = Clock()


screen = pygame.display.set_mode((800, 600))


class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.surf = pygame.Surface((10, 100))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = 1
        self.rect.y = 0

    def move(self, x, y):
        self.rect.move_ip(x, y)
        if self.rect.x >= 800:
            self.rect.x = 800
        if self.rect.x < 0:
            self.rect.x -= 0
        if self.rect.y >= 600:
            self.rect.y = 600
        if self.rect.y == 0:
            self.rect.y = 0


class Computer(pygame.sprite.Sprite):

    def __init__(self):
        self.surf = pygame.Surface((10, 100))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = 789
        self.rect.y = 0

    def update(self, ball_y_position):
        direction = 1
        if self.rect.y > ball_y_position:
            direction = -1
        self.rect.move_ip((0, 10 * direction))


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        self.surf = pygame.Surface((15, 15))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = 400
        self.rect.y = 300
        self.direction = [-10, -5]

    def update(self):
        self.rect.move_ip(tuple(self.direction))
        if self.rect.y < 0 or self.rect.y > 600:
            self.direction[1] = - self.direction[1]

    def reverse(self):
        self.direction[0] = -(self.direction[0] - random.randint(0, 5))
        self.direction[1] = -(self.direction[1] - random.randint(0, 5))


player = Player()
computer = Computer()
ball = Ball()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    # move the player
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_UP]:
        player.move(0, -15)
    if pressed_keys[K_DOWN]:
        player.move(0, 15)

    ball.update()
    computer.update(ball.rect.y)
    if pygame.sprite.collide_rect(player, ball):
        ball.reverse()
    if pygame.sprite.collide_rect(computer, ball):
        ball.reverse()

    if ball.rect.x < -100:
        print('You lose')
        running = False
    if ball.rect.x > 900:
        print('You win')
        running = False

    screen.fill((0, 0, 0))
    screen.blit(player.surf, player.rect)
    screen.blit(computer.surf, computer.rect)
    screen.blit(ball.surf, ball.rect)

    pygame.display.flip()
    clock.tick(100)

pygame.quit()
