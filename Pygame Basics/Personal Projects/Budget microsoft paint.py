import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,600),pygame.RESIZABLE)

circlep = []

circler = 10
colors = [(0,0,255), (255, 0, 0), (0, 255, 0)]
c_pick = 0

clock = pygame.time.Clock()
print("\n------Info------\n\nLeft/Right arrow key: Brush Size\nDown arrow key: colour")
run = True
while run:
    screen.fill((255,255,255))  

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                c_pick += 1
                if c_pick >= len(colors):
                    c_pick = 0
            
            elif event.key == K_RIGHT:
                circler += 10
            elif event.key == K_LEFT:
                circler -= 10

            elif event.key == K_e:
                circlep.clear()  
    
    mouse = pygame.mouse.get_pressed()

    if mouse[0]:  # left mouse button
        position = pygame.mouse.get_pos()
        circlep.append((position, colors[c_pick], circler))


    for position, color, radius in circlep:
        pygame.draw.circle(screen, color, position, radius)

    pygame.display.update()
    clock.tick(90)
pygame.quit()
