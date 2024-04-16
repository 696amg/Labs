import pygame

pygame.init()

background = (250, 255, 255)
red = (255, 0, 1)

width = 610
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("red ball")
clock = pygame.time.Clock()
fps = 60

radis = 25
speed_pix = 20
crug = pygame.Rect(0, 0, 50, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_w] and crug.top > 0:
        crug.top -= speed_pix
    if pressed[pygame.K_s] and crug.bottom < height:
        crug.bottom += speed_pix
    if pressed[pygame.K_a] and crug.left > 0:
        crug.left -= speed_pix
    if pressed[pygame.K_d] and crug.right < width:
        crug.right += speed_pix
    #присваиваем движения к кнопкам

    screen.fill(background)
    pygame.draw.circle(screen, red, crug.center, radis)
    pygame.display.update()
    clock.tick(fps)