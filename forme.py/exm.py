#lab4 math1 
#import math
'''deg = int(input("Input degree: "))#there use the one of the math methods
print("Output radian:", math.radians(deg))'''
#lab4 math2
'''height = int(input()) #there is i just used the basic formula
astorona = int(input())
bstorona = int(input())
trapeziod = (astorona + bstorona)/2 * height 
print(trapeziod)'''
#lab4 math3
'''def calc_area(storony, dlina):
    area = (storony * dlina**2) / (4 * math.tan(math.pi / storony))

    return area

storony = int(input("Input number of sides: "))
dlina = int(input("Input the length of a sides: "))
area = calc_area(storony, dlina)
print("The area of the polygon is: ", area)

storony = int(input("Input num of sides: "))
dlina = int(input("Input the length of a sides: "))
area = storony/2
print("The area: ", pow(dlina, area))'''
#lab4 math4
'''len = float(input("Length of base: "))
hei = float(input("Height of parallelogram: "))
A = len * hei
print(A)'''
#lab4 generators1
'''num_N = int(input())
def square_nums():
    for i in range(1, num_N):
        yield i**2

a = square_nums()
print(next(a))'''
#lab4 generators2
'''num_N = int(input())
def even_nums():
    for i in range(1, num_N, 2):
        yield i
a = even_nums()
print(next(a),end=' ')'''
#lab4 generators3
'''n = int(input())
def my_func():
    for i in range(0, n):
        if i%3==0 or i%4==0:
            yield i

a = my_func()
print(next(a))'''
#lab4 generators4
# def squares(a, b):
#     for i in range(a, b):
#         yield i**2
# a = squares(1, 10)
# for a_b in a:
#     print(a_b, end=' ')

#lab4 gen5
# def my(n):
#     for i in range(n+1):
#         yield (i-n)*(-1)
# hh = int(input())
# a = my(hh)
# for ii in a:
#     print(ii)
# lab5 №2
# import re
# pattern = input()
# x = re.search('ab{2,3}', pattern)
# print(x)
# lab5 №3
# words = input()
# xc = re.findall("[a-z]+_[a-z]",words)
# print(xc)
#lab5 №4
# p = input()
# o = re.findall("^[A-Z].[a-z]", p)
# print(o) 
#lab5 №5
# p = input()
# l = re.search(r"a.*b$", p)
# print("There urs answer: ", l)
import pygame 
screen = pygame.display.set_mode((400, 300))

while True:
    for sobytie in pygame.event.get():
        if sobytie.type == pygame.QUIT:
            pygame.quit()
        if sobytie.type == pygame.KEYDOWN:
            pygame.
            
    pygame.display.update()

    pygame.draw.rect(screen, (150, 0, 0), pygame.Rect(30, 30, 200, 60))

    pygame.display.flip()




    #import pygame

pygame.init()

w = 600
h = 400

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Pain 2.0")

run = True
while run:
    screen.fill((255, 250, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()