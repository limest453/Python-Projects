import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()

BASE_DIR = os.path.dirname(__file__)

size = width, height = 740, 480
screen = pygame.display.set_mode(size)

img = pygame.image.load(os.path.join(BASE_DIR, "char.jpg")).convert()

x, y = 0, 0
move_x, move_y = 0, 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -3
            elif event.key == K_RIGHT:
                move_x = 3
            elif event.key == K_UP:
                move_y = -3
            elif event.key == K_DOWN:
                move_y = 3

            elif event.key == K_LCTRL:
                img = pygame.image.load(os.path.join(BASE_DIR, "char1.png")).convert()
            elif event.key == K_BACKSPACE:
                img = pygame.image.load(os.path.join(BASE_DIR, "char.jpg")).convert()

        if event.type == KEYUP:
            if event.key in (K_LEFT, K_RIGHT):
                move_x = 0
            if event.key in (K_UP, K_DOWN):
                move_y = 0

    x += move_x
    y += move_y

    screen.fill((255, 255, 255))
    screen.blit(img, (x, y))

    pygame.display.update()
    clock.tick(60)
