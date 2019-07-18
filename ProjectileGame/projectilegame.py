import pygame
from pygame.locals import *
import math
pygame.init()

clock = pygame.time.Clock()


class Projectile(pygame.sprite.Sprite):

    GRAVITY_CONST = 9

    def __init__(self, initial_velocity, initial_position, launch_direction):
        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 255, 255))
        self.initial_velocity = initial_velocity
        self.init_x, self.init_y = initial_position
        self.launch_x, self.launch_y = launch_direction
        self.time = 0

    def get_pos(self):
        self.time = self.time + 0.1
        return self.x_pos(), self.y_pos()

    def x_pos(self):
        return (self.time * self.initial_velocity) + self.init_x

    def y_pos(self):
        x_tan_theta = self.x_pos() * self.tan_theta()
        other_part = (self.GRAVITY_CONST * self.x_pos() ** 2) / (2 * (self.initial_velocity ** 2) * (self.cos_theta()**2))
        # print(x_tan_theta, other_part)
        return 600 - (x_tan_theta - other_part)

    def tan_theta(self):
        x_1, y_1 = self.init_x, self.init_y
        x_2, y_2 = self.launch_x, self.launch_y
        return math.fabs(y_2 - y_1) / math.fabs(x_2 - x_1)

    def cos_theta(self):
        x_1, y_1 = self.init_x, self.init_y
        x_2, y_2 = self.launch_x, self.launch_y
        dot_ab = (x_1 * x_2) + (y_1 * y_2)
        return dot_ab / (math.fabs(y_2 - y_1) * math.fabs(x_2 - x_1))


class Gun(pygame.sprite.Sprite):

    def __init__(self, initial_position):
        self.image = pygame.Surface((150, 25))
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = initial_position[0]
        self.rect.y = initial_position[1]
        self.rotation_image = self.image.copy()

    def update(self, pos):
        self.rotation_image = self.rotate((self.rect.x, self.rect.y), pos)

    def rotate(self, current_pos, new_pos):
        rotation_angle = self.get_angle(current_pos, new_pos)
        image_copy = self.image.copy()
        return pygame.transform.rotate(image_copy, rotation_angle % 360)

    def get_angle(self, current_pos, new_pos):
        x_1, y_1 = current_pos
        x_2, y_2 = new_pos
        if x_1 == x_2:
            rotation_angle = 90
        elif y_1 == y_2:
            rotation_angle = 0
        else:
            rotation_angle = math.degrees(math.atan((math.fabs(y_2 - y_1) / math.fabs(x_2 - x_1))))
        return rotation_angle


screen = pygame.display.set_mode((1000, 600))

initial_pos = (20, 550)
gun = Gun(initial_pos)
pygame.init()
running = True
projectile = None
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            gun.update(pos)
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            velocity = math.sqrt((pos[0] - initial_pos[0]) ** 2 + (pos[1] - initial_pos[1]) ** 2) / 10
            print(velocity)
            projectile = Projectile(velocity, initial_pos, pos)
    rect = gun.rotation_image.get_rect()
    rect.center = (100, 525)
    screen.fill((0, 0, 0))
    # screen.blit(gun.rotation_image, rect)
    if projectile:
        # print('drawing projectile at pos', projectile.get_pos())
        screen.blit(projectile.image, projectile.get_pos())
    pygame.display.flip()
    clock.tick(30)
