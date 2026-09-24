import pygame
import random

pygame.init()

#colours
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

#display setup
dis_width = 600
dis_height = 500

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake Game")

#Clock
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 5

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def message(msg, colour):
    m = font_style.render(msg, True, colour)
    dis.blit(m, [dis_width / 6, dis_height / 3])


def game_loop():
    game_over = False
    game_closes = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x2 = 0
    y2 = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_closes == True:
            dis.fill(blue)
            message("You lost, press C to play again or press Q to quit!", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_closes = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x2 = -snake_block
                    y2 = 0
                elif event.key == pygame.K_RIGHT:
                    x2 = snake_block
                    y2 = 0
                elif event.key == pygame.K_DOWN:
                    x2 = 0
                    y2 = snake_block
                elif event.key == pygame.K_UP:
                    x2 = 0
                    y2 = -snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_closes = True
        x1 += x2
        y1 += y2
        dis.fill(blue)
        pygame.draw.rect(dis, red,
                         [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(
                random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(
                random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)
        pygame.display.update()

    pygame.quit()
    quit()


game_loop()
