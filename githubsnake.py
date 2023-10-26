import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
SNAKE_SPEED = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize snake and food
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
direction = RIGHT
new_direction = RIGHT

# Score
score = 0

# Game over flag
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                new_direction = UP
            if event.key == pygame.K_DOWN and direction != UP:
                new_direction = DOWN
            if event.key == pygame.K_LEFT and direction != RIGHT:
                new_direction = LEFT
            if event.key == pygame.K_RIGHT and direction != LEFT:
                new_direction = RIGHT

    direction = new_direction

    # Move the snake
    x, y = snake[0]
    x += direction[0]
    y += direction[1]
    head = (x, y)

    # Check if the snake ate the food
    if head == food:
        snake.append(food)
        score += 1
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    # Check for collision with walls or self
    if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT or head in snake[1:]:
        game_over = True

    # Move the snake
    snake.insert(0, head)
    if len(snake) > score + 1:
        snake.pop()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw the food
    pygame.draw.rect(screen, WHITE, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Update the display
    pygame.display.flip()

    # Control game speed
    pygame.time.Clock().tick(SNAKE_SPEED)

# Quit pygame
pygame.quit()
sys.exit()
