import pygame
from pygame.locals import *
from pygame.time import Clock
import random

pygame.init()
clock = Clock()

'''
    1. Set the font we will be using for our game
        - check the notebook
        - the lines should look like
        default_font = pygame.font.get_default_font()
        font = pygame.font.Font(default_font, 18)
'''
# <name_this: default_font> = pygame.font.get_default_font()
# font = pygame.font.Font(<put default_font here>, 18)

''' DON'T CHANGE THE CODE BELOW HERE '''

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pong')

class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.surf = pygame.Surface((10, 100))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = 1
        self.rect.y = 0

    def move(self, x, y):
        if y < 0 and self.rect.y < 5:
            return
        if y > 0 and self.rect.y > 495:
            return
        self.rect.move_ip(x, y)


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
        if self.rect.y + 10 * direction < 0 or self.rect.y + 10 * direction > 500:
            return
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
        if self.rect.y < 2 or self.rect.y > 580:
            self.direction[1] = - self.direction[1]

    def reverse(self):
        self.direction[0] = -self.direction[0]
        self.direction[1] = -(self.direction[1] - random.randint(0, 5))


player = Player()
computer = Computer()
ball = Ball()

'''DON'T CHANGE THE CODE ABOVE HERE'''

''' 6. Create a player_points variable to track your points'''
player_points = 0

computer_points = 0
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
        computer_points = computer_points + 1
        ball = Ball()
    if ball.rect.x > 900:
        ''' 
            7. Copy the example from the above if statement in order to track player_points
                and reset the ball using ball = Ball()
        '''
        # 1. increment player points using player_points = player_points + 1
        # 2. create a new ball using ball = Ball()

    ''' 
        2. Set the score_str = to the text you want to print
            - I recommend: "Your score {} | Computer's Score {}".format(player_points, computer_points)
    '''
    score_str = "<My text>"

    ''' 3. Set the score_text using font.render(score_str, True, (255, 255, 255), None)'''
    # score_text = font.render("<Put score_str here>", True, (255, 255, 255), None)

    # This adjusts the positioning of the text and puts it at the bottom of the screen
    ''' 4. Uncomment these lines to position the text'''
    # text_rect = score_text.get_rect()
    # text_rect.center = (400, 580)

    screen.fill((0, 0, 0))
    screen.blit(player.surf, player.rect)
    screen.blit(computer.surf, computer.rect)
    screen.blit(ball.surf, ball.rect)

    ''' 
        5. Draw the text to the screen
            - use screen.blit(score_text, text_rect) to draw it
    '''
    # screen.blit(<enter score_text here>, text_rect)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
