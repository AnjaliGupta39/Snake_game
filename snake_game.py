import pygame
import random

pygame.init()

# Colors
black = (0, 0, 0)
blue = (50, 153, 213)
green = (0, 255, 0)
red = (255, 0, 0)

# Fullscreen window
dis = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = dis.get_size()

pygame.display.set_caption("Snake Game Fullscreen")

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def show_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    dis.blit(value, [10, 10])

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(dis, black, [x, y, snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])

def game_loop():
    x1 = width // 2
    y1 = height // 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Generate food on 10x grid
    foodx = random.randrange(0, width - snake_block, 10)
    foody = random.randrange(0, height - snake_block, 10)

    game_over = False
    game_close = False

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press C to Play Again or Q to Quit", red)
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return
                    if event.key == pygame.K_c:
                        return game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True

                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Update snake position (integer)
        x1 = int(x1 + x1_change)
        y1 = int(y1 + y1_change)

        # Boundary hits
        if x1 < 0 or x1 >= width or y1 < 0 or y1 >= height:
            game_close = True

        dis.fill(blue)

        # Draw food
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # Snake body
        snake_list.append([x1, y1])
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Self collision
        for part in snake_list[:-1]:
            if part == [x1, y1]:
                game_close = True

        draw_snake(snake_list)
        show_score(length_of_snake - 1)
        pygame.display.update()

        # PERFECT FOOD EATING COLLISION FIX
        if abs(x1 - foodx) < snake_block and abs(y1 - foody) < snake_block:
            foodx = random.randrange(0, width - snake_block, 10)
            foody = random.randrange(0, height - snake_block, 10)
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()

game_loop()
