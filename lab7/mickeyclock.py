import pygame 
import datetime

pygame.init()
#размеры
S_Width = 700
S_Height = 700
Centre = (S_Width // 2, S_Height // 2)  # Центр экрана
#colour
screen = pygame.display.set_mode((S_Width, S_Height))
white = (255, 250, 255)
fps = 60

clock = pygame.time.Clock()
cartinkamc = pygame.image.load('/Users/artem/Downloads/mickey-clock.jpg')
cartinkamc_width = 500
cartinkamc_height = 500
cartinkamc_xpos = (S_Width - cartinkamc_width) // 2  #по горизонталм установка центра
cartinkamc_ypos = (S_Height - cartinkamc_height) // 2  #по вертикали

#инициализация стрелок
barrow = pygame.image.load('/Users/artem/Downloads/big-arrow.png')
barrow_width = 25  #уменьшаем ширину стрелки
barrow_ratio = 0.13
barrow_height = barrow_width / barrow_ratio
barrow = pygame.transform.scale(barrow, (barrow_width, int(barrow_height)))

sarrow = pygame.image.load('/Users/artem/Downloads/small-arrow.png')
sarrow_width = 40  #меньшаем ширину стрелки
sarrow_ratio = 0.22
sarrow_height = sarrow_width / sarrow_ratio
sarrow = pygame.transform.scale(sarrow, (sarrow_width, int(sarrow_height)))

start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False 

    #угол поворота стрелок
    angle_1 = datetime.datetime.now().second * -6
    angle_2 = datetime.datetime.now().minute * -6

    screen.fill(white)
    screen.blit(cartinkamc, (cartinkamc_xpos, cartinkamc_ypos))

    #подгон центра стрелок
    barrowre = barrow.get_rect(center=Centre)
    sarrowre = sarrow.get_rect(center=Centre)

    #стрелки на экране
    start_barrow = pygame.transform.rotate(barrow, angle_1)#поворачивает изображение на заданный угол
    ssb = start_barrow.get_rect()
    ssb.center = barrowre.center
    screen.blit(start_barrow, ssb)

    start_sarrow = pygame.transform.rotate(sarrow, angle_2)
    sarrow_start_rect = start_sarrow.get_rect()
    sarrow_start_rect.center = sarrowre.center
    screen.blit(start_sarrow, sarrow_start_rect)

    pygame.display.flip()
    clock.tick(fps)