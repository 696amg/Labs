import pygame 
pygame.init()
#выбор системного шрифта размером 40, с помощью этого шрифта создается ERASER и BRUSH
font = pygame.font.SysFont(None, 40)

#цвета
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
LIGHTBLUE = (0,255,255)


W, H = 1000, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("PAIN 2.0")
done = False
clock = pygame.time.Clock()
FPS = 60

#создание экрана на котором изображены сами инструменты, и цвет его
toolSC = pygame.Surface((W, 80))
toolSC.fill("gray")
#кнопки на toolSC
redR = pygame.Rect(0, 0, 40, 40)
blueR = pygame.Rect(0,40,40,40)
greenR = pygame.Rect(40,0,40,40)
yellowR = pygame.Rect(40,40,40,40)
lgblueR = pygame.Rect(80,0,40,40)
blackR = pygame.Rect(80,40,40,40)
pygame.draw.rect(toolSC, RED, redR)
pygame.draw.rect(toolSC, BLUE, blueR)
pygame.draw.rect(toolSC, GREEN, greenR)
pygame.draw.rect(toolSC, YELLOW, yellowR)
pygame.draw.rect(toolSC, LIGHTBLUE, lgblueR)
pygame.draw.rect(toolSC, BLACK, blackR)
R = [redR, blueR, greenR, yellowR, lgblueR, blackR]
C = [RED, BLUE, GREEN, YELLOW, LIGHTBLUE, BLACK]
#создание того самого текста Eraser, егт цвет 
#потом с помощью get_rect выходит прямоугольник, и затем его позиция 
erase_text = font.render("ERASER", True, BLACK)
erase_text_rect = erase_text.get_rect(topleft = (120, 30))
toolSC.blit(erase_text, erase_text_rect)
#размер браш, координаты 
brush10 = pygame.Rect(276, 32, 20, 20)
pygame.draw.circle(toolSC, BLACK, brush10.center, 10)
brush15 = pygame.Rect(316, 25, 30, 30)
pygame.draw.circle(toolSC, BLACK, brush15.center, 15)
brush20 = pygame.Rect(366, 18, 40, 40)
pygame.draw.circle(toolSC, BLACK, brush20.center, 20)
B = [brush10, brush15, brush20]
S = [10,15,20]
#прямоугольник
#круг
rectangle = pygame.Rect(436, 20, 40, 40)
pygame.draw.rect(toolSC, BLACK, rectangle, 5)

circle = pygame.Rect(496, 20, 40, 40)
pygame.draw.circle(toolSC, BLACK, circle.center, 20, 5)
#создание BRUSH
brush_text = font.render("BRUSH", True, BLACK)
brush_text_rect = brush_text.get_rect(topleft = (556, 30))
toolSC.blit(brush_text, brush_text_rect)
#ромб
rhombus = pygame.Rect(666, 20, 40, 40)
pygame.draw.polygon(toolSC, BLACK, [(686, 20), (666, 40), (686, 60), (706, 40)], 5)
#треугольник и его размеры и координаты
triangle = pygame.Rect(726, 20, 40, 40)
pygame.draw.polygon(toolSC, BLACK, [(746, 20), (726, 60), (766, 60)], 5)
#прямой треуг
triangle90 = pygame.Rect(786, 20, 40, 40)
pygame.draw.polygon(toolSC, BLACK, [(786, 20), (786, 60), (826, 60)], 5)
#начальные значения, режим работы и тому подобное 
colorOfBrush = BLUE
status = "brush"
size = 10
drawStarted = False
startPos = (0,0)
top = left = right = bottom = (0,0)

#холст
screen.fill(WHITE)

#самый главный цикл
while not done:
    touch = pygame.mouse.get_pressed()
    posMouse = pygame.mouse.get_pos()
    if posMouse[1] < 80:
        pygame.mouse.set_cursor(pygame.cursors.arrow)
    else:
        pygame.mouse.set_cursor(pygame.cursors.diamond)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        #изменение цветов
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            for i in range(len(R)):
                if R[i].collidepoint(posMouse):
                    colorOfBrush = C[i]
            #для eraser
            if erase_text_rect.collidepoint(posMouse):
                colorOfBrush = WHITE
                size = 20
                status = "brush"
            #разщмеры
            for i in range(len(B)):
                if B[i].collidepoint(posMouse):
                    size = S[i]
            
            if rectangle.collidepoint(posMouse):
                status = "rectangle"
            if circle.collidepoint(posMouse):
                status = "circle"
            if brush_text_rect.collidepoint(posMouse):
                status = "brush"
            if rhombus.collidepoint(posMouse):
                status = "rhombus"
            if triangle.collidepoint(posMouse):
                status = "triangle"
            if triangle90.collidepoint(posMouse):
                status = "triangle90"

        #присваивание мыши для различных режимов рисования 
        #если стутус равен кисти то при движении мыши рисуется круг, труег и тд
        if status == "brush":
            if event.type == pygame.MOUSEMOTION:
                if touch[0]:
                    pygame.draw.circle(screen, colorOfBrush, (posMouse), size)
                    
        if status == "rectangle":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == pygame.MOUSEMOTION:
                if drawStarted:
                    pos = event.pos

                    width = abs(pos[0] - startPos[0])
                    height = abs(pos[1] - startPos[1])
                    pygame.draw.rect(screen, colorOfBrush, (min(pos[0],startPos[0]), 
                                min(pos[1],startPos[1]), width, height))
                    
            if event.type == pygame.MOUSEBUTTONUP:
                drawStarted = False
        # 2
        if status == "circle":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == pygame.MOUSEMOTION:
                if drawStarted:
                    pos = event.pos

                    radius = abs(pos[0] - startPos[0])
                    pygame.draw.circle(screen, colorOfBrush, startPos, radius)

            if event.type == pygame.MOUSEBUTTONUP:
                drawStarted = False
        # 3
        if status == "rhombus":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == pygame.MOUSEMOTION:
                if drawStarted:
                    pos = event.pos

                    top = (startPos[0] + abs(startPos[0] - pos[0]) / 2, startPos[1])
                    bottom = (startPos[0] + abs(startPos[0] - pos[0]) / 2, pos[1])
                    right = (pos[0], startPos[1] + abs(startPos[1] - pos[1]) / 2)
                    left = (startPos[0], startPos[1] + abs(startPos[1] - pos[1]) / 2)

            if event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.polygon(screen, colorOfBrush, [top, right, bottom, left])
                drawStarted = False
        # 4
        if status == "triangle":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == pygame.MOUSEMOTION:
                if drawStarted:
                    pos = event.pos

                    top = (startPos[0] + abs(startPos[0] - pos[0])/2, startPos[1])
                    left = (startPos[0], pos[1])
                    right = (pos[0], pos[1])
                    

            if event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.polygon(screen, colorOfBrush, [top, left, right])
                drawStarted = False
        # 5
        if status == "triangle90":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == pygame.MOUSEMOTION:
                if drawStarted:
                    pos = event.pos

                    top = startPos
                    left = (startPos[0], pos[1])
                    right = (pos[0],pos[1])
            
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.polygon(screen, colorOfBrush, [top, left, right])
                drawStarted = False

    screen.blit(toolSC, (0,0))             
    pygame.display.update()
    clock.tick(FPS)

