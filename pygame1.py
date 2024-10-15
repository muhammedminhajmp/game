import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Blocks")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the player
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 10

# Set up falling blocks
block_size = 50
block_pos = [random.randint(0, WIDTH - block_size), 0]
block_speed = 10

# Set up the game clock
clock = pygame.time.Clock()

# Game over flag
game_over = False

# Score tracker
score = 0

def detect_collision(player_pos, block_pos):
    p_x, p_y = player_pos
    b_x, b_y = block_pos
    if (b_x >= p_x and b_x < (p_x + player_size)) or (p_x >= b_x and p_x < (b_x + block_size)):
        if (b_y >= p_y and b_y < (p_y + player_size)) or (p_y >= b_y and p_y < (b_y + block_size)):
            return True
    return False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move player left or right
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    # Move the block down the screen
    block_pos[1] += block_speed

    # If the block goes off the screen, reset its position
    if block_pos[1] > HEIGHT:
        block_pos = [random.randint(0, WIDTH - block_size), 0]
        score += 1  # Increase score for every block avoided

    # Check for collision
    if detect_collision(player_pos, block_pos):
        game_over = True
        print(f"Game Over! Final Score: {score}")

    # Fill screen with white
    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, BLACK, (player_pos[0], player_pos[1], player_size, player_size))

    # Draw block
    pygame.draw.rect(screen, RED, (block_pos[0], block_pos[1], block_size, block_size))

    # Update display
    pygame.display.update()

    # Frame rate
    clock.tick(30)

# Quit pygame
pygame.quit()
