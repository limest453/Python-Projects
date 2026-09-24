# importing all the required libraries
import pygame
from pygame.locals import *
from sys import exit

# initiating pygame library to use it's functions
pygame.init()

# declaring windows/surface width and height
size = width, height = 740, 480
screen = pygame.display.set_mode(size)


# loads a new image from a file and convert() 
# will create a copy of image on surface
img = pygame.image.load("char.jpg").convert()

# declaring value to variables
clicking = False
right_clicking = False
middle_click = False

while True:
    mx, my = pygame.mouse.get_pos()  # gets mouse x,y coordinates
    location = [mx, my]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          
            # pygame.QUIT deactivates pygame
            exit()
            # exit() is sys function used to kill the program

    # MOUSEBUTTONDOWN event is triggered when a button is pressed
    if event.type == MOUSEBUTTONDOWN:
      
        # returns true when mouse left button is clicked
        if event.button == 1:  
            clicking = True
            
            # declaring new image file to update image
            # everytime left button clicking is true
            img = pygame.image.load("char1.png")
            pygame.display.update()  # update image
        
        # returns true when mouse right button is clicked
        if event.button == 3:  
            right_clicking = True
            
            # declaring new image file to update image
            # everytime right button is clicked
            img = pygame.image.load("char.jpg")
            pygame.display.update()  # update image
            
        # returns true when mouse middle button is clicked
        if event.button == 2:  
            middle_click = middle_click
            
            # rescale image when middle button clicking is true
            img = pygame.transform.scale(img, (100, 100))
            pygame.display.update()  # update image

    # MOUSEBUTTONUP is triggered when mouse button 
    # is released(not clicked)
    if event.type == MOUSEBUTTONUP:
        if event.button == 1:
            clicking = False

    screen.fill((255, 255, 255))
    
    # the function will fill the background
    # with white color
    screen.blit(img, (location[0], location[1]))
    
    # blit() function will copy image file 
    # to x,y coordinates.
    pygame.display.update()
    # draw the objects on screen