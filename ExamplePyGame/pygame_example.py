# import the pygame module
import pygame
from enemy import Enemy
from player import Player
from cloud import Cloud
from pygame.locals import *

# initialize pygame
pygame.init()

# create the screen object
# here we pass it a size of 800x600
screen_height = 800
screen_width = 600
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Plane Game")


def start_over():
    global player
    global game_over
    game_over = False
    player = Player()
    all_sprites.add(player)


def init_events():
    ADDENEMY = pygame.USEREVENT + 1
    ADDCLOUD = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDENEMY, 500)
    pygame.time.set_timer(ADDCLOUD, 2500)
    return ADDENEMY, ADDCLOUD


def init_groups():
    enemies = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    return enemies, clouds, all_sprites


def init_background():
    background = pygame.Surface(screen.get_size())
    background.fill((128, 128, 255))

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("GAME OVER (press space to play again)", True, (255, 255, 255), (128, 128, 255))
    textRect = text.get_rect()
    textRect.center = (screen_height / 2, screen_width / 2)
    return background, text

# Initialize our game
running = True
player = Player()
ADDENEMY, ADDCLOUD = init_events()
enemies, clouds, all_sprites = init_groups()
background, game_over_text = init_background()
game_over = False

# Our main loop!
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_SPACE and game_over:
                start_over()
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
        if not game_over:
            if event.type == ADDENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == ADDCLOUD:
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)

    screen.blit(background, (0, 0))
    if game_over:
        screen.blit(background, (0, 0))
        textRect = game_over_text.get_rect()
        textRect.center = (screen_height / 2, screen_width / 2)
        screen.blit(game_over_text, textRect)
        pygame.display.update()
    else:
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        clouds.update()

        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            for sprite in all_sprites:
                sprite.kill()
                game_over = True
        # Draw the player to the screen
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
    # Update the display
    pygame.display.flip()



