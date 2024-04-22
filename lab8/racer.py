import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
#цвета
black  = (0, 0, 0)
red   = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

WIDTH = 400
HEIGHT = 600
SPEED = 5
 
coin = ["lab8/coin1.png", "lab8/coin2.png", "lab8/coin3.png", "lab8/coin4.png"]
sheet_ofcoin = 0
#установка белого скрина(экрана)
DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
DISPLAYSURF.fill(white)
pygame.display.set_caption("гонщик супер")
 
 
#добавление противника через функицю
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("lab8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,WIDTH-40), 0)    
 
    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
 
#также добавление игровых монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load(coin[sheet_ofcoin]), (pygame.image.load(coin[sheet_ofcoin]).get_width()//2, pygame.image.load(coin[sheet_ofcoin]).get_height()//2))
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, WIDTH-40), 0)

    def move(self):
            self.rect.move_ip(0, 5)
            if self.rect.top > 600:
                self.rect.center = (random.randint(30, 370), -300)

    def update_image(self):
            global sheet_ofcoin
            sheet_ofcoin = (sheet_ofcoin + 1) % len(coin)  # Обновляем индекс изображения монетки с учетом цикличности
            self.image = pygame.transform.scale(pygame.image.load(coin[sheet_ofcoin]), (pygame.image.load(coin[sheet_ofcoin]).get_width()//7, pygame.image.load(coin[sheet_ofcoin]).get_height()//7))



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("lab8/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()  
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
#настройка spites       
ig = Player()
ee = Enemy()
coi = Coin()
#группы
enemies = pygame.sprite.Group()
enemies.add(ee)
all_sprites = pygame.sprite.Group()
all_sprites.add(ig)
all_sprites.add(ee)
Coin.add(coi)
coin_ap = pygame.USEREVENT + 1
pygame.time.set_timer(coin_ap, 100)

#добавление игрока
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#цикл
while True:     
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 2
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.fill(white)

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    #
    if pygame.sprite.spritecollideany(ig, enemies):
          DISPLAYSURF.fill(red)
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)



    
    
