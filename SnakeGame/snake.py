"""
 Simple snake example.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame
import random
from pygame.locals import *

# Call this function so the Pygame library can initialize itself
pygame.init()
# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set the width and height of each snake segment
segment_width = 15
segment_height = 15
# Margin between each segment
segment_margin = 3

default_font = pygame.font.get_default_font()
font = pygame.font.Font(default_font, 24)


class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """

    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Apple(pygame.sprite.Sprite):

    def __init__(self, x=None, y=None):
        super().__init__
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x if x else random.randint(50, screen_width - segment_width)
        self.rect.y = y if y else random.randint(50, screen_height - segment_height)

# Create an 800x600 sized screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# Set the title of the window
pygame.display.set_caption('Snake Example')


def game_loop():
    # Set initial speed
    x_change = segment_width + segment_margin
    y_change = 0

    segments_list = pygame.sprite.Group()

    # Create an initial snake
    snake_segments = []
    head_segment = Segment(250 - (segment_width + segment_margin), 30)
    for i in range(1, 15):
        x = 250 - (segment_width + segment_margin) * i
        y = 30
        segment = Segment(x, y)
        snake_segments.append(segment)
        segments_list.add(segment)
    apple = Apple(300, 100)
    clock = pygame.time.Clock()
    apples_eaten = 0
    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # Set the speed based on the key pressed
            # We want the speed to be enough that we move a full
            # segment, plus the margin.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = (segment_width + segment_margin) * -1
                    y_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = (segment_width + segment_margin)
                    y_change = 0
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = (segment_height + segment_margin) * -1
                if event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = (segment_height + segment_margin)

        # Get rid of last segment of the snake
        # .pop() command removes last item in list
        old_segment = snake_segments.pop()
        segments_list.remove(old_segment)

        # Figure out where new segment will be
        old_head = head_segment

        x = old_head.rect.x + x_change
        y = old_head.rect.y + y_change
        head_segment = Segment(x, y)
        # Insert new segment into the list
        snake_segments.insert(0, old_head)
        segments_list.add(old_head)

        if pygame.sprite.spritecollideany(head_segment, segments_list):
            done = True

        if pygame.sprite.collide_rect(head_segment, apple):
            apples_eaten = apples_eaten + 1
            x = snake_segments[-1].rect.x - (segment_width + segment_margin)
            y = snake_segments[-1].rect.y
            new_tail_segment = Segment(x, y)
            snake_segments.append(new_tail_segment)
            segments_list.add(new_tail_segment)
            apple = Apple()

        screen.fill(BLACK)
        # display the number of apples eaten
        text_str = "You've eaten {} apples".format(apples_eaten)
        text = font.render(text_str, True, (255, 255, 255), None)
        text_rect = text.get_rect()
        text_rect.center = (400, 570)
        segments_list.draw(screen)
        screen.blit(head_segment.image, head_segment.rect)
        screen.blit(apple.image, apple.rect)
        screen.blit(text, text_rect)

        # Flip screen
        pygame.display.flip()

        # Pause
        clock.tick(15)


def display_replay_screen():
    play_again_text = font.render("Hit Space to play again", True, (255, 255, 255), None)
    text_rect = play_again_text.get_rect()
    text_rect.center = (400, 300)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return False
        screen.fill((0, 0, 0))
        screen.blit(play_again_text, text_rect)
        pygame.display.flip()


game_over = False
while not game_over:
    game_loop()
    game_over = display_replay_screen()

pygame.quit()
