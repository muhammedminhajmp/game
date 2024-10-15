import pygame
import random

# Initialize the pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Game dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game title
pygame.display.set_caption("Snake Game")

# Set the clock (to control the speed of the game)
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, BLACK)
    screen.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

# Message display function
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x = WIDTH // 2
    y = HEIGHT // 2

    # Change in position (starting with no movement)
    x_change = 0
    y_change = 0

    # List to store the snake's body segments
    snake_list = []
    length_of_snake = 1

    # Random position for the food
    food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        # If the player loses
        while game_close:
            screen.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Movement of the snake based on user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # If the snake hits the boundaries of the screen
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        x += x_change
        y += y_change

        # Fill screen with white
        screen.fill(WHITE)

        # Draw the food
        pygame.draw.rect(screen, BLUE, [food_x, food_y, snake_block, snake_block])

        # Update the snake's position
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake hits itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw the snake
        draw_snake(snake_block, snake_list)

        # Display the score
        display_score(length_of_snake - 1)

        # Update the screen
        pygame.display.update()

        # Check if the snake has eaten the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Control the game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game loop
game_loop()
