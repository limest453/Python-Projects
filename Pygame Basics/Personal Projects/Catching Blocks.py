import pygame
import random
import sys #imports system commands

pygame.init()

#Setup
W = 600
H = 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Catch the falling blocks!")

WHT, BLU, RED, BLK = (255, 255, 255), (0, 200, 255), (255, 0, 0), (0, 0, 0) #made capital cuz its a constant

#Clock & Font
clock = pygame.time.Clock() #used to limit fps of game
font = pygame.font.SysFont(None, 36) #default system font, size 36

#Making Paddle and Block
paddle = pygame.Rect(W // 2 - 60, H - 20, 120, 10) #stores a rectangle with these values
block = pygame.Rect(random.randint(0, W - 20), 0, 20, 20)
b_speed = 5

#Rectangles have attributes
#paddle.x → x position
#paddle.y → y position
#paddle.left → left edge position
#paddle.right → right edge
#paddle.top → top edge
#paddle.bottom → bottom edge

score = 0

#!Game Loop
run = True
while True:
    #Setup
    screen.fill(BLK)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Moving Paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0: #checks which key is pressed within the pygame.key.getpressed() function --> square brackets index function. If left of tile is not on edge
        paddle.move_ip(-8,0) #move_ip --> move in place (eg. 8 pixles to left)
    if keys[pygame.K_RIGHT] and paddle.right < W:
        paddle.move_ip(8, 0)
    
    #Moving Block
    block.y += b_speed #sends block down 

    #Block caught
    if block.colliderect(paddle): #checks if 2 rectangles are overlapping
        block.y = 0 #sends back up
        block.x = random.randint(0, W - 20) #moves around randomly
        score += 1
        b_speed += 0.5 #speeds up
    
    #Block missed
    if block.y > H:
        game_over = font.render(f"Game Over! Final Score: {score}", True, RED) #Text code ("True" makes it smooth)
        screen.blit(game_over, (W // 2 - 150, H // 2)) #adds text surface onto screen surface
        pygame.display.flip()
        pygame.time.wait(2000)
        run = False
    
    #Draw objects
    pygame.draw.rect(screen, WHT, paddle) #pygame.draw.rect(which surface, color, an object or positon&size, optional border width)
    pygame.draw.rect(screen, BLU, block)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHT) 
    screen.blit(score_text, (10, 10))

    pygame.display.flip() #refreshes screen
    clock.tick(60) #sets to 60fpsimport pygame