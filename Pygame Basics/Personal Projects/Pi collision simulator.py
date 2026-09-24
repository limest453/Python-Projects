import pygame
import math
import sys

class Square(object):
    def __init__(self, size, XY, mass, velocity): #initialises the values for the square object
        self.x = XY[0]
        self.y = XY[1]
        self.mass = mass
        self.size = size
        self.v = velocity

    def collision(self, otherblock):
        if self.x + self.size < otherblock.x or self.x > otherblock.x + otherblock.size: #if block1 right (left side + size) less than block 2 right or other way around then not touching
            return False
        return True

    def NewVelocity(self, otherblock): #using the velocity equation for the velcity of the 2nd blcok
        #equation used: 1D elastic collision velocity equation.
        sumM = self.mass + otherblock.mass
        newV = (self.mass - otherblock.mass)/sumM * self.v
        newV += (2 * otherblock.mass / sumM) * otherblock.v
        return newV

    def collide_wall(self):
        if self.x <= 0: 
            self.x = 0  # Hard reset position to prevent clipping behind wall
            self.v *= -1 #resets velocity to bounce back
            return True
        return False

    def update(self):
        self.x += self.v #moves the block

    def draw(self, surface): #to draw the sqaure
        pygame.draw.rect(surface, red, [self.x, self.y, self.size, self.size]) #makes square based on initialised values
        

def redraw(): #so the block moves by removing the previous frames
    background.fill(white)
    
    #Ground layout scales dynamically with window dimensions
    pygame.draw.rect(background, gray, [0, 0, width, height - 150])
    
    #Render both blocks
    SquareSmall.draw(background)
    SquareBig.draw(background)
    
    #Text updates relative to window height
    font = pygame.font.SysFont(None, 40)
    text_count = font.render(f"Collisions: {count}", True, (0,0,0))
    text_mass = font.render(f"Block Mass: 100^{mass_power}", True, (0,0,0))
    
    background.blit(text_count, [50, height - 100])
    background.blit(text_mass, [50, height - 60])
    pygame.display.update() #updating everything

#Screen values
width, height = 800, 400
white = (255, 255, 255)
gray = (190, 190, 190)
red = (200, 0, 0)

pygame.init()

#user input
print("----Pi Collision Physics Simulator----\n")
print("Notes: Making the velocity or exponent of the block's mass too high causes the simulation to bug out.\nThe slower the block is, the higher you can make the mass without it clipping through the wall.\nAdvanced mode can handle larger masses but will slow down when the blocks are moving to each other\nIf 'Y' is not entered for advanced mode, it will automiatically disable it\nEnjoy!\n\n")
advanced = input("Do you want to enable advanced mode? (Y/N): ").strip().lower() == "y"



mass_power = int(input("Enter exponent for the block's mass (0 - 5): ") or 3)
power = 100**mass_power

velocity_input = float(input("Enter velocity (1-15): ") or 3) 
velinput = -velocity_input * 0.00001 

#starting positions
small_start_x = 100
big_start_x = small_start_x + 100 + (mass_power * 80)  #Pushes large block further right as mass increases

#window setup
background = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Pi Collision simulator")

#block initalising
SquareSmall = Square(20, (small_start_x, height - 170), 1, 0) #not moving
SquareBig = Square(50, (big_start_x, height - 200), power, velinput)#moving left

count = 0
running = True

while running:
    for event in pygame.event.get(): #gets all evens in pygame
        if event.type == pygame.QUIT: #required if they close it
            running = False
        
        #window resizing
        elif event.type == pygame.VIDEORESIZE:#checks if they resizd
            width, height = event.w, event.h
            background = pygame.display.set_mode((width, height), pygame.RESIZABLE) #recreates background with new dimensions
            
            #moves blcks based on window size 
            SquareSmall.y = height - 170
            SquareBig.y = height - 200 #its higher cuz the block is bigger

    #physics loop
    for i in range(10000): #frame rate
        if advanced:
            if SquareSmall.collision(SquareBig) and SquareSmall.v > SquareBig.v: #checks colission and ONLY when the big one is moving
                count += 1
                v1 = SquareSmall.NewVelocity(SquareBig) #physics stuff
                v2 = SquareBig.NewVelocity(SquareSmall)
                SquareSmall.v = v1 #DOING the physics stuff
                SquareBig.v = v2
                SquareSmall.x = SquareBig.x - SquareSmall.size #so not overlapping, moves the small box left when the big one touches
            
            if SquareSmall.collide_wall():
                count += 1
        else:
            if SquareSmall.collision(SquareBig): #checks colission 
                count += 1
                v1 = SquareSmall.NewVelocity(SquareBig) #physics stuff
                v2 = SquareBig.NewVelocity(SquareSmall)
                SquareSmall.v = v1 #DOING the physics stuff
                SquareBig.v = v2
                SquareSmall.x = SquareBig.x - SquareSmall.size #so not overlapping, moves the small box left when the big one touches
            
            if SquareSmall.collide_wall():
                count += 1
            
            
        SquareBig.update()
        SquareSmall.update()
        
    redraw()

pygame.quit()
sys.exit()
