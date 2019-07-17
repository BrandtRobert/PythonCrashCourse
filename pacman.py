import time
import random
import pygame
from pygame.locals import *
import time
from player import Player
from enemy import Enemy

pygame.init()
clock=pygame.time.Clock()
FPS=30


 #board
#  0 1 2 3 4 5 6 7 
#0 + + + + + + + +
#1 + x           +
#2 +   + +   +   +
#3 +   +     +   +
#4 +       + +   +
#5 +   +     +   +
#6 +   + +   +   +
#7 + o         o +
#8 + + + + + + + +
board = [[1,1,1,1,1,1,1,1],
         [1,0,0,0,0,0,0,1],
         [1,0,1,1,0,1,0,1],
         [1,0,1,0,0,1,0,1],
         [1,0,0,0,1,1,0,1],
         [1,0,1,0,0,1,0,1],
         [1,0,1,1,0,1,0,1],
         [1,0,0,0,0,0,0,1],
         [1,1,1,1,1,1,1,1]]


class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super(Player, self).__init__()
        #replace the player surface with an image
        self.surf = pygame.Surface((50,50))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center=(pos[0]*100+50, pos[1]*100+50))
        self.direction = (1,0)
        self.pos = pos
        self.speed = 10
        self.getDest()
        self.getMoves()
    def getDest(self):
        if board[self.pos[1]+self.direction[1]][self.pos[0]+self.direction[0]]==0:
            self.dest=(self.pos[0]+self.direction[0],self.pos[1]+self.direction[1])
        else:
            self.dest=self.pos

    def getMoves(self):
        self.moves = [((self.dest[0]-self.pos[0])*10,(self.dest[1]-self.pos[1])*10)]*10
        self.pos=self.dest

    def update(self):
        if len(self.moves)==0:
            self.getDest()
            self.getMoves()
        self.rect.move_ip(self.moves.pop(0))

    def hitWall(self):
        self.direction=(0,0)

 
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Enemy, self).__init__()
        #replace enemy surface with an Image
        self.surf = pygame.Surface((90,90))
        self.surf.fill((255,0,0))
        self.pos=pos
        self.speed=10
        posPix = (pos[0]*100+50,pos[1]*100+50)
        self.rect = self.surf.get_rect(center=posPix)
        self.getDest()
        self.getMoves()

    def getDest(self):
        possible = [(1,0),(-1,0),(0,1),(0,-1)]
        openSpaces = []
        for p in possible:
            if board[self.pos[1]+p[1]][self.pos[0]+p[0]]==0:
                openSpaces.append(p)
        selection = openSpaces[random.randint(0,len(openSpaces))-1]
        self.dest=(self.pos[0]+selection[0],self.pos[1]+selection[1])

    def getMoves(self):
        self.moves = [((self.dest[0]-self.pos[0])*10,(self.dest[1]-self.pos[1])*10)]*10
        self.pos=self.dest
	
    def update(self):
        if len(self.moves)==0:
            self.getDest()
            self.getMoves()
        self.rect.move_ip(self.moves.pop(0))
    def hitWall(self):
        pass

class Wall(pygame.sprite.Sprite):
    def __init__(self,pos):
        super(Wall, self).__init__()
        self.surf = pygame.Surface((100,100))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect(center=pos)

class Food(pygame.sprite.Sprite):
    def __init__(self,pos):
        super(Food, self).__init__()
        self.surf = pygame.Surface((80,80))
        self.surf.fill((255,255,0))
        self.rect = self.surf.get_rect(center=(pos[0]*100+50,pos[1]*100+50))
    def move(self):
        found=False
        while not found:
            x = random.randint(0,7)
            y = random.randint(0,8)
            if board[y][x]==0:
                self.pos=(x,y)
                self.rect.center = (self.pos[0]*100+50,self.pos[1]*100+50)
                found=True
class Game:
    def __init__(self):
        #are the enemies vulnerable?
        self.vul = False
        self.vulTime=0
        self.walls=pygame.sprite.Group()
        for i in range(0,8):
            for j in range(0,9):
                if board[j][i]==1:
                    self.walls.add(Wall((i*100+50,j*100+50)))
        self.restart()
        self.gameover=False
        
    def restart(self):
        '''
            This function defines all of the player and enemy positions
            Try creatingin your own enemies, or changing the posistion of the walls
            Positions are defined using 8x9 grid
        '''
        self.enemy_count=2
        self.player = Player((1,1))
        enemy1 = Enemy((1,7))
        enemy2 = Enemy((6,7))
        self.food = Food((6,5))
        self.food_group = pygame.sprite.Group()
        self.food_group.add(self.food)
        self.enemies = pygame.sprite.Group()
        self.enemies.add(enemy1)
        self.enemies.add(enemy2)
        self.all_movable = pygame.sprite.Group()
        self.all_movable.add(self.player)
        self.all_movable.add(enemy1)
        self.all_movable.add(enemy2)
        self.all_movable.add(self.food)
        for wall in self.walls:
            screen.blit(wall.surf,wall.rect)
    
    def redraw(self,screen):
        screen.fill((0,0,255))
        for wall in self.walls:
            screen.blit(wall.surf,wall.rect)

        for entity in self.all_movable:
            screen.blit(entity.surf, entity.rect)
        pygame.display.flip()

    def end(self):
        print("gameover")
        default_font=pygame.font.get_default_font()
        font = pygame.font.Font(default_font,32)
        text= font.render("GAME OVER",True,(255,0,0),(0,0,0))
        textRect = text.get_rect(center=(400,400))
        text2 = font.render("Press any key to continue",True,(255,0,0),(0,0,0)) 
        text2Rect = text2.get_rect(center=(400,400))

        screen.blit(text,textRect)
        screen.blit(text2,text2Rect)
        pygame.display.flip()
        locked=True
        while locked:
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    locked=False
                if event.type==QUIT:
                    locked=False    
        self.restart()
        #time.sleep(10)
    
    def update(self):
        if self.gameover:
            return
        for entity in self.all_movable:
            entity.update()
            if pygame.sprite.spritecollideany(entity, self.walls):
                entity.hitWall()
    
    def handleKey(self,key):
       if event.key==K_LEFT:
           self.player.direction=(-1,0)
       if event.key==K_RIGHT:
           self.player.direction=(1,0)
       if event.key==K_DOWN:
           self.player.direction=(0,1)
       if event.key==K_UP:
           self.player.direction=(0,-1)
       self.gameover=False


screen = pygame.display.set_mode((800,900))
game = Game()
game.redraw(screen)
running=True
while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
        if event.type==KEYDOWN:
           game.handleKey(event.key)
    game.update()
    for enemy in game.enemies:
        if pygame.sprite.collide_circle(game.player, enemy):
            if not game.vul:
                game.player.kill()
                game.end()
            else:
                enemy.kill()
                game.enemy_count=game.enemy_count-1
                #check if its 0 and do something
    if time.time()-game.vulTime>10:
        game.vul=False
        game.player.surf.fill((255,255,255))

    if pygame.sprite.spritecollideany(game.player, game.food_group):
        game.player.surf.fill((0,0,0))
        game.vul=True
        game.food.move()
        game.vulTime=time.time()

    game.redraw(screen)

    clock.tick(30)

    
