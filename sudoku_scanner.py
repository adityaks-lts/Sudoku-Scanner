import pygame
from sudoku import sudoku
from image_section import image_section

pygame.init()

width,height = 1200,600

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("   SUDOKU  ")

clock = pygame.time.Clock()

fps = 120

image_section_window = image_section(win,600,0,600,600)
sudoku_window = sudoku(win,25,25,550,550)

while not pygame.event.get(pygame.QUIT):

    clock.tick(fps)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_s]:
        sudoku_window.create_solve_thread()
    if keys[pygame.K_c]:
        x={0: {0: 5, 1: 3, 4: 7}, 1: {0: 6, 3: 1, 4: 9, 5: 5}, 2: {1: 9, 2: 8, 7: 6}, 3: {0: 8, 4: 6, 8: 3}, 4: {0: 4, 3: 8, 5: 3, 8: 1}, 5: {0: 7, 4: 2, 8: 6}, 6: {1: 6, 6: 2, 7: 8}, 7: {3: 4, 4: 1, 5: 9, 8: 5}, 8: {4: 8, 7: 7, 8: 9}}
        sudoku_window.setup_puzzle(x)

    image_section_window.draw()
    sudoku_window.draw()
    
    pygame.display.update()

pygame.quit()