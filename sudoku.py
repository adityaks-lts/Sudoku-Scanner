import pygame
from threading import Thread
from time import sleep

pygame.init()

width,height = 1200,600

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("   SUDOKU  ")

clock = pygame.time.Clock()

fps = 120

child_window_1 = pygame.Surface((550,600))
child_rect_1 = child_window_1.get_rect(topleft=(0,0))
child_window_2 = pygame.Surface((600,600))
child_rect_2 = child_window_2.get_rect(topleft=(600,0))

grid = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

anim_grid = [[0,50]]
head = 0

#Grid draw animation
def animation():
    global anim_grid,head

    while True:
        if head < 8:
            x = anim_grid[(head*(head+2))][0]

            if not x%50:
                head+=1
                for i in range(head):
                    anim_grid.append([i*50,(head)*50+50])
                    anim_grid.append([(head)*50,i*50+50])
                anim_grid.append([(head)*50,(head)*50+50])
            sleep(0.05)
        else:
            sleep(0.2)

#Thread creation
th = Thread(target=animation,daemon=True)

while not pygame.event.get(pygame.QUIT):

    # clock.tick(fps)

    win.blit(child_window_1,child_rect_1)
    win.blit(child_window_2,child_rect_2)
    child_window_1.fill((250,250,250))
    child_window_2.fill((250,250,250))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        anim_grid.clear()
        anim_grid.append([0,50])
        head = 0

    
    for pos in anim_grid:
        pygame.draw.rect(child_window_1,(0,0,0),(pos[0],pos[1],50,50),1)

    if not th.is_alive(): th.start()

    pygame.display.update()

pygame.quit()