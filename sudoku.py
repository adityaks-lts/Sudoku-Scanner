import pygame

pygame.init()

width,height = 500,500

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("   SUDOKU  ")

clock = pygame.time.Clock()

fps = 60

head = [(0,50)]



while not pygame.event.get(pygame.QUIT):

    clock.tick(fps)

    win.fill((250,250,250))
    for pos in head:
        pygame.draw.rect(win,(0,0,0),(pos[0],pos[1],50,50),2)
    pygame.display.update()

pygame.quit()