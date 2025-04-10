import pygame
import time

# Initialize pygame
pygame.init()

# Constants
CANVA_WIDTH = 400
CANVA_HEIGHT = 400
CELL_SIZE = 20
ERASER_SIZE = 20

# Colors
BLUE = (0, 0, 225)
WHITE = (255, 255, 255)
PINK = (225, 182, 193)

# Screen setup
screen = pygame.display.set_mode((CANVA_WIDTH, CANVA_HEIGHT))
pygame.display.set_caption("Eraser Effect in Pygame")

# Create grid of rectangles
grid = []
for row in range(0, CANVA_HEIGHT, CELL_SIZE):
    for col in range(0, CANVA_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
        grid.append(rect)

# Eraser setup
eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Update eraser position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x, mouse_y)

    # Remove collided rectangles
    new_grid = []
    for rect in grid:
        if not eraser.colliderect(rect):
            new_grid.append(rect)
        else:
            pygame.draw.rect(screen, PINK, rect)  # Visual feedback

    grid = new_grid

    # Draw remaining grid
    for rect in grid:
        pygame.draw.rect(screen, BLUE, rect)

    # Draw eraser
    pygame.draw.rect(screen, PINK, eraser)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    time.sleep(0.05)

# Quit pygame
pygame.quit()
