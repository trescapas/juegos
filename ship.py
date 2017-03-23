#!/usr/bin/env python
import pygame,sys
from pygame.locals import *
import random

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

pygame.mouse.set_visible(0)

ship = pygame.image.load("images/ship.png")
ship = pygame.transform.scale(ship, (100, 20))
ship_top = screen.get_height() - ship.get_height()-10
ship_left = screen.get_width()/2 - ship.get_width()/2
screen.blit(ship, (ship_left, ship_top ))

shot = pygame.image.load("images/shot.png")
shot = pygame.transform.scale(shot, (20, 20))

walle = pygame.image.load("images/walle.jpeg")
walle = pygame.transform.scale(walle, (800, 600))
shoot_y = 0

invasor = pygame.image.load("images/space-invaders.jpg")
invasor = pygame.transform.scale(invasor, (50, 50))
invasor_izquierda = screen.get_width() / 2 - invasor.get_width() / 2
invasor_arriba = screen.get_height() / 2


pygame.init()

def detectar_collision(shoot_x, shoot_y,invasor_iz,invasor_arriba):
    condition = (invasor_iz < shoot_x) and (shoot_x < invasor_izquierda + 50) and (invasor_arriba<shoot_y) and (shoot_y <invasor_arriba +50)

    return condition

x_invasor = invasor_arriba
y_invasor = invasor_izquierda
increment = 10

while True:
    clock.tick(60)
    screen.fill((0,0,0))
    x,y = pygame.mouse.get_pos()
    screen.blit(walle, (0, 0))
    screen.blit(ship, (x-ship.get_width()/2, ship_top))

    screen.blit(invasor, (x_invasor, y_invasor ))

    x_invasor += increment
    y_invasor += random.randint(-5,5)
    if (x_invasor > screen.get_width()) or (x_invasor<0):
        increment = -increment

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            shoot_y = 500
            shoot_x = x

    if shoot_y > 0:
        screen.blit(shot,(shoot_x, shoot_y))
        shoot_y -= 10
        collision = detectar_collision(shoot_x, shoot_y, x_invasor, y_invasor)
        if collision:
            soundfile = "/usr/share/sounds/KDE-Im-Contact-In.ogg"
            pygame.mixer.music.load(soundfile)
            pygame.mixer.music.play(0, 0)

    pygame.display.update()
