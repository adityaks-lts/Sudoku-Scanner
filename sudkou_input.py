import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set the dimensions of the grid and cells
WIDTH, HEIGHT = 540, 540
CELL_SIZE = WIDTH // 9
GRID_SIZE = 9

# Set up the display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Input")

# Set up the colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GRAY = pygame.Color(128, 128, 128)
BLUE = pygame.Color(0, 0, 255)

# Create a blank Sudoku grid
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(grid)  # Print the grid to console
            elif pygame.K_1 <= event.key <= pygame.K_9:
                # Get the coordinates of the cell being clicked
                x, y = pygame.mouse.get_pos()
                row, col = y // CELL_SIZE, x // CELL_SIZE

                # Store the number in the corresponding cell of the grid
                grid[row, col] = event.key - pygame.K_0

    # Draw the grid
    window.fill(WHITE)
    for i in range(GRID_SIZE + 1):
        if i % 3 == 0:
            pygame.draw.line(window, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 4)
            pygame.draw.line(window, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 4)
        else:
            pygame.draw.line(window, GRAY, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 1)
            pygame.draw.line(window, GRAY, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 1)

    # Draw the numbers
    font = pygame.font.Font(None, 36)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i, j] != 0:
                text = font.render(str(grid[i, j]), True, BLUE)
                text_rect = text.get_rect(center=(j * CELL_SIZE + CELL_SIZE / 2, i * CELL_SIZE + CELL_SIZE / 2))
                window.blit(text, text_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
