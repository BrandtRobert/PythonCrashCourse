import pygame
from pygame.locals import *
import math
import random

pygame.init()

clock = pygame.time.Clock()

screen_width = 800
screen_height = 600


class Player(pygame.sprite.Sprite):

    def __init__(self):
        # self.image = pygame.Surface((50, 50))
        # self.image.fill((255, 255, 255))
        super().__init__()
        self.image = pygame.image.load('./plain-triangle.png')
        self.image = pygame.transform.scale(self.image, (25, 40))
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.rect.y = screen_height // 2
        self.rotated_image = self.image.copy()
        self.rotation = 0
        self.movement_speed = 5

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            new_x = self.movement_speed * math.sin(math.radians(self.rotation))
            new_y = self.movement_speed * math.cos(math.radians(self.rotation))
            if self.rect.x - new_x < 0 or self.rect.x - new_x > screen_width:
                return
            if self.rect.y - new_y < 0 or self.rect.y - new_y > screen_height:
                return
            self.rect.move_ip(-new_x, -new_y)
        if pressed_keys[K_RIGHT]:
            self.rotation = (self.rotation - 5) % 360
            self.rotated_image = pygame.transform.rotate(self.image.copy(), self.rotation)
        if pressed_keys[K_LEFT]:
            self.rotation = (self.rotation + 5) % 360
            self.rotated_image = pygame.transform.rotate(self.image.copy(), self.rotation)

    def get_center(self):
        return self.rect.x + 0.5 * 25, self.rect.y + 0.5 * 40


class Bullet(pygame.sprite.Sprite):

    def __init__(self, initial_pos, angle):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = initial_pos[0]
        self.rect.y = initial_pos[1]
        self.angle = angle
        self.movement_speed = 8

    def update(self):
        new_x = self.movement_speed * math.sin(math.radians(self.angle))
        new_y = self.movement_speed * math.cos(math.radians(self.angle))
        self.rect.move_ip(-new_x, -new_y)
        if self.rect.x > 800 or self.rect.y < 0:
            self.kill()


class Asteroid(pygame.sprite.Sprite):

    def __init__(self, position, health = 4):
        super().__init__()
        self.health = health
        self.image = pygame.image.load('./asteroid.png')
        size = self.health_to_dimensions()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        direction_x = (screen_width // 2 - position[0])
        direction_y = (screen_height // 2 - position[1])
        magnitude = math.sqrt((direction_x ** 2) + (direction_y ** 2))
        self.direction = (direction_x / magnitude, direction_y / magnitude)
        self.movement_speed = 4

    def health_to_dimensions(self):
        if self.health == 1:
            return 20, 20
        if self.health == 2:
            return 30, 30
        if self.health == 3:
            return 40, 40
        if self.health == 4:
            return 50, 50
        if self.health == 5:
            return 60, 60

    def update(self):
        self.rect.move_ip(self.direction[0] * self.movement_speed,
                          self.direction[1] * self.movement_speed)

    def hit_by_bullet(self):
        self.health = self.health - 1
        if self.health == 0:
            self.kill()
            return
        size = self.health_to_dimensions()
        self.image = pygame.transform.scale(self.image, size)

def game_loop():
    ADD_ASTEROID = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_ASTEROID, 2000)

    player = Player()
    bullets = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    screen = pygame.display.set_mode((800, 600))
    running = True
    # make a limit on asteroids

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pos = player.get_center()
                    angle = player.rotation
                    bullet = Bullet(pos, angle)
                    bullets.add(bullet)
            elif event.type == ADD_ASTEROID:
                x_direction = random.randint(0, 2)
                y_direction = random.randint(0, 2)

                if x_direction == 1:
                    rand_x = random.randint(screen_width, screen_width + 100)
                elif x_direction == 2:
                    rand_x = random.randint(-100, 0)
                else:
                    rand_x = screen_width // random.randint(1, 5)
                if y_direction == 1:
                    rand_y = random.randint(screen_height, screen_height + 100)
                elif y_direction == 2:
                    rand_y = random.randint(-100, 0)
                else:
                    rand_y = screen_height // random.randint(1, 5)
                asteroid = Asteroid((rand_x, rand_y), health=random.randint(1,5))
                asteroids.add(asteroid)

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        # if pressed_keys[K_SPACE]:
        #     pos = player.get_center()
        #     angle = player.rotation
        #     bullet = Bullet(pos, angle)
        #     bullets.add(bullet)
        for _, asteroid_list in pygame.sprite.groupcollide(bullets, asteroids, True, False).items():
            for asteroid in asteroid_list:
                asteroid.hit_by_bullet()

        if pygame.sprite.spritecollideany(player,  asteroids):
            running = False
        screen.fill((255, 255, 255))
        for bullet in bullets:
            bullet.update()
            screen.blit(bullet.image, bullet.rect)
        for asteroid in asteroids:
            asteroid.update()
            screen.blit(asteroid.image, asteroid.rect)
        screen.blit(player.rotated_image, player.rect)
        pygame.display.flip()
        clock.tick(60)

# def replay_screen():
#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 return True



game_done = False
while not game_done:
    game_loop()
    # game_done = replay_screen()