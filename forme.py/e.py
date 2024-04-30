      import pygame
from pygame.locals import *
import random, sys
import time

pygame.init()

screen = pygame.display.set_mode((310, 300))
black = pygame.Color(0,0,0)
white = pygame.Color(255, 255,255)
grey = pygame.Color(125, 125, 125)
red = pygame.Color(250, 0, 0)

speed = 5; playerspeed = 5 
pygame.display.set_caption("гонщик")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        prese_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if prese_keys[K_LEFT]:
                self.rect.move_ip(-speed, 0)
        if self.rect.right < 400:
            if prese_keys[K_RIGHT]:
                self.rect.move_ip(speed, 0)


class Coinz(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(coin[coin_sheet_index]), (pg.image.load(coin[coin_sheet_index]).get_width()//2, pg.image.load(coin[coin_sheet_index]).get_height()//2))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)

    def move(self):
        self.rect.move_ip(0, 5)
        
        if self.rect.top > 600:
           
            self.rect.center = (random.randint(30, 370), -300)

    def update_image(self):
        global coin_sheet_index
        coin_sheet_index = (coin_sheet_index + 1) % len(coin)  # Обновляем индекс изображения монетки с учетом цикличности
        self.image = pg.transform.scale(pg.image.load(coin[coin_sheet_index]), (pg.image.load(coin[coin_sheet_index]).get_width()//7, pg.image.load(coin[coin_sheet_index]).get_height()//7))

        