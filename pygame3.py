import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Player attributes
player_width = 50
player_height = 60
player_x = 100
player_y = SCREEN_HEIGHT - player_height - 40
player_speed = 5
player_jump_speed = 15
is_jumping = False
player_velocity_y = 0

# Gravity
GRAVITY = 0.5

# Define platforms (x, y, width, height)
platforms = [
    (0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20),
    (150, 450, 100, 20),
    (300, 350, 100, 20),
    (450, 250, 100, 20),
    (600, 150, 100, 20)
]

# Enemy properties
enemy_width = 40
enemy_height = 40
enemy_speed = 3
enemy_list = [
    {"x": 150, "y": 430, "direction": 1},
    {"x": 300, "y": 330, "direction": -1},
    {"x": 450, "y": 230, "direction": 1}
]

# Coins
coin_radius = 10
coins = [(random.randint(100, 700), random.randint(50, 400)) for _ in range(5)]

# Score and health
score = 0
health = 3
font = pygame.font.SysFont(None, 35)

# Functions for game elements
def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, [x, y, player_width, player_height])

def draw_platforms():
    for platform in platforms:
        pygame.draw.rect(screen, BLACK, platform)

def draw_enemies():
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, [enemy["x"], enemy["y"], enemy_width, enemy_height])

def draw_coins():
    for coin in coins:
        pygame.draw.circle(screen, (255, 215, 0), coin, coin_radius)

def draw_text(text, font, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])

def player_hit_enemy(player_x, player_y, enemies):
    for enemy in enemies:
        if player_x < enemy["x"] + enemy_width and player_x + player_width > enemy["x"]:
            if player_y < enemy["y"] + enemy_height and player_y + player_height > enemy["y"]:
                return True
    return False

def player_collect_coin(player_x, player_y, coins):
    for coin in coins:
        if (player_x + player_width > coin[0] - coin_radius and player_x < coin[0] + coin_radius) and \
                (player_y + player_height > coin[1] - coin_radius and player_y < coin[1] + coin_radius):
            return coin
    return None

# Main game loop
def game_loop():
    global player_x, player_y, is_jumping, player_velocity_y, score, health

    game_over = False

    while not game_over:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Handle keypresses for movement and jumping
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_SPACE] and not is_jumping:
            is_jumping = True
            player_velocity_y = -player_jump_speed

        # Gravity and jumping mechanics
        if is_jumping:
            player_velocity_y += GRAVITY
            player_y += player_velocity_y

            if player_y + player_height >= SCREEN_HEIGHT - 20:
                player_y = SCREEN_HEIGHT - player_height - 20
                is_jumping = False

        # Collision detection with platforms
        for platform in platforms:
            if player_x + player_width > platform[0] and player_x < platform[0] + platform[2]:
                if player_y + player_height > platform[1] and player_y + player_height - player_velocity_y < platform[1]:
                    player_y = platform[1] - player_height
                    is_jumping = False

        # Move enemies
        for enemy in enemy_list:
            enemy["x"] += enemy["direction"] * enemy_speed
            if enemy["x"] <= 0 or enemy["x"] + enemy_width >= SCREEN_WIDTH:
                enemy["direction"] *= -1

        # Check for collision with enemies
        if player_hit_enemy(player_x, player_y, enemy_list):
            health -= 1
            if health == 0:
                game_over = True

        # Check for coin collection
        collected_coin = player_collect_coin(player_x, player_y, coins)
        if collected_coin:
            coins.remove(collected_coin)
            score += 10

        # Redraw game screen
        screen.fill(WHITE)
        draw_platforms()
        draw_enemies()
        draw_coins()
        draw_player(player_x, player_y)
        draw_text(f"Score: {score}", font, BLACK, 10, 10)
        draw_text(f"Health: {health}", font, BLACK, SCREEN_WIDTH - 150, 10)

        # Update the display
        pygame.display.update()

        # Frame rate
        clock.tick(60)

    # Game Over screen
    screen.fill(WHITE)
    draw_text("Game Over!", font, RED, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 30)
    draw_text(f"Final Score: {score}", font, BLACK, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 30)
    pygame.display.update()
    pygame.time.wait(2000)

    pygame.quit()

# Start the game
game_loop()
