import pygame
from pygame.locals import * # imports more than 280 predefined constants (pygame.K_SPACE --> K_SPACE)

# Initialize Pygame (Always Required)
pygame.init()

# Set up the game window (Always Required)
win = pygame.display.set_mode((800, 600)) #game window
pygame.display.set_caption("Falling Blocks") #Title

# Sprite: A 2D object (like our square) displayed on the screen.
# Surface: A canvas for drawing (even the screen is a Surface)
# Rect: A rectangle object for positioning and collisions.

class Sq(pygame.sprite.Sprite): #class name() --> used to define what "name" should always have (unique charactersitcs can be added after) #pygame.sprite.Sprite is a the asset "Sprite" within the "sprite" folder of the Pygame library
    def __init__(self): #self --> placeholder variable referring to specific object when called later (inthis case s1, s2, s3, s4), __init__ --> “what happens when the object is created”. Double underscores show its a pygame keyword
        super().__init__() #intialises the parent class of "Sprite" to give baseline blueprint for adding specifc class detials
        self.surf = pygame.Surface((25, 25)) #this Sq has its own surface (a 25x25 square)
        self.surf.fill((0, 200, 255)) #colours square

# Create 4 squares
s1, s2, s3, s4 = Sq(), Sq(), Sq(), Sq() #each has own surface

# Game loop (Alwyas required)
run = True
while run: #keeps running
    for e in pygame.event.get(): #Handles all events
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_BACKSPACE): #if user clicks close button, backspace or down key, game quits
            run = False

    # win.blit() --> draws something on the window, in this case the squares we made and provides the coordinates on the screen
    win.blit(s1.surf, (40, 40)) 
    win.blit(s2.surf, (40, 530))
    win.blit(s3.surf, (730, 40))
    win.blit(s4.surf, (730, 530))

    pygame.display.flip() #refreshes the screen
