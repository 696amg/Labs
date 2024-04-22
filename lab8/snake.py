import pygame
import time
import random

snake_speed = 15
window_x = 720
window_y = 480
#цвета
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()
#игровое окно
pygame.display.set_caption('Змейка')
game_window = pygame.display.set_mode((window_x, window_y))

#  фпс
fps = pygame.time.Clock()
# определение положения змеи по умолчанию
snake_position = [100, 50]
#определение первых блоков тела
snake_body = [
    [100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# фрукты
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True
# установка направления змеи по умолчанию к
direction = 'RIGHT'
change_to = direction
# начальные очки
score = 0

fruit_time = 5

#создание функции показа очков
def show_score(choice, color, font, size) :
    #создание объекта шрифта score_font
    score_font = pygame.font.SysFont(font, size)
    
    score_surface = score_font.render('Score : ' + str(score), True, color)

    #создаем объект для текста
    score_rect = score_surface.get_rect()

    #отображение текста
    game_window.blit(score_surface, score_rect)


def game_over() :
    #создание объекта шрифта
    my_font = pygame.font.SysFont('times new roman', 50)

    #создание текстовой поверхности нв которой текст
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)

    
    #создать прямоугольный объект для текста
    game_over_rect = game_over_surface.get_rect()

    #установка положения текста
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    #blit -- нарисует текст на экране
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    #через 2 секунды мы выйдем из программы
    time.sleep(2)
    pygame.quit()
    quit()

while True :

    #обработка ключевых событий
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                change_to = 'UP'
            if event.key == pygame.K_DOWN :
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT :
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT :
                change_to = 'RIGHT'

    #сли две клавиши нажаты одновременно
    if change_to == 'UP' and direction != 'DOWN' :
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP' :
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT' :
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT' :
        direction = 'RIGHT'

    #перемещение
    if direction == 'UP' :
        snake_position[1] -= 15
    if direction == 'DOWN' :
        snake_position[1] += 15
    if direction == 'LEFT' :
        snake_position[0] -= 15
    if direction == 'RIGHT' :
        snake_position[0] += 15

    #сам рост змеи при получении фруктов
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1] :
        score += 10
        fruit_spawn = False
    else :
        snake_body.pop()

    if not fruit_spawn :
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                         random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body :
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    #Game Over
    if snake_position[0] < 0 or snake_position[0] > window_x - 10 :
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10 :
        game_over()


    for block in snake_body[1 :] :
        if snake_position[0] == block[0] and snake_position[1] == block[1] :
            game_over()

    #показ очков
    show_score(1, white, 'again', 20)

    #перезапуск
    pygame.display.update()
    #фпс
    fps.tick(snake_speed)