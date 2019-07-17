# import the pygame module
import pygame
import random
from pygame.locals import *
from pygame.time import Clock

''' DONT WRITE ANY CODE BELOW HERE '''

# initialize pygame
pygame.init()
clock = Clock()
# create the screen object
# here we pass it a size of 800x600
screen_height = 800
screen_width = 600
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Plane Game")


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


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        if Path('./Icons/jet.png').is_file():
            self.image = pygame.transform.scale(pygame.image.load('./Icons/jet.png'), (40, 40)).convert()
            self.image.set_colorkey((255, 255, 255), RLEACCEL)
        else:
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        # self.move_size = 10

    def update(self, lateral, vertical):
        self.rect.move_ip(lateral, vertical)
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600


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
    text_rect = text.get_rect()
    text_rect.center = (screen_height / 2, screen_width / 2)
    return background, text

player = Player()
ADDENEMY, ADDCLOUD = init_events()
enemies, clouds, all_sprites = init_groups()
background, game_over_text = init_background()

''' DONT WRITE ANY CODE ABOVE HERE '''

# Initialize our game
running = True
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
            '''
                7. Add code to start over when they press space and the game is over
            '''
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
        '''
            4. Add code to create new enemies
        '''
        ''' 6. Add code to create new clouds '''
    screen.blit(background, (0, 0))
    if game_over:
        screen.blit(background, (0, 0))
        screen.blit(game_over_text, game_over_text.get_rect())
        pygame.display.flip()
    else:
        '''2. Get the keys the player presses using pygame.key.get_pressed()'''
        # if pressed_keys[K_RIGHT]:
        #     player.update(10, 0)

        ''' 4. Update the enemies so they move across the screen '''
        ''' 6. Update the clouds so they move across the screen '''
        '''
            5. Using pygame.sprite.spritecollidany(thing, collision)
                - kill the player
                - kill all the sprites
                - set game_over to true
        '''
        '''1. Draw the player to the screen using screen.blit(player.image, player.rect)'''
        '''3. Now use a for loop to draw everything in all_sprites to the screen'''
    # Update the display
    pygame.display.flip()
    clock.tick(30)  # you can change the speed by making this number higher


