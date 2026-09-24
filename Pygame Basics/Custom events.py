import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

pygame.display.set_caption("Custom Events")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

bg_active_color = WHITE
screen.fill(WHITE)

CHANGE_COLOR = pygame.USEREVENT + 1

pygame.time.set_timer(CHANGE_COLOR, 500) #does event every 500ms/0.5s

ON_BOX = pygame.USEREVENT + 2

box = pygame.Rect((225, 225, 50, 50))
grow = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == CHANGE_COLOR:
            if bg_active_color == GREEN:
                screen.fill(GREEN)
                bg_active_color = WHITE
            elif bg_active_color == WHITE:
                screen.fill(WHITE)
                bg_active_color = GREEN
        
        if event.type == ON_BOX:
            if grow:
                box.inflate_ip(2, 2)
                if box.width >= 75:
                    grow = False      
            else:
                box.inflate_ip(-2, -2)
                if box.width <= 50:
                    grow = True
        
        if event.type == pygame.QUIT:
            running = False
        
    if box.collidepoint(pygame.mouse.get_pos()):
        pygame.event.post(pygame.event.Event(ON_BOX))

    pygame.draw.rect(screen, RED, box)

    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()