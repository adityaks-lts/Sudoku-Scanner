import pygame
from sudoku import sudoku
from image_section import image_section
from button import button

pygame.init()

width,height = 1200,600

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("   SUDOKU   ")

clock = pygame.time.Clock()

fps = 60

image_section_window = image_section(win,700,100,600,600)
sudoku_window = sudoku(win,50,100)

buttons = []
buttons.append(button(50,30,"comicsans",20,"**SOLVE**",(0,0,0)))
buttons.append(button(240,30,"comicsans",20,"**NEW**",(0,0,0)))
buttons.append(button(390,30,"comicsans",20,"**RESET**",(0,0,0)))
buttons.append(button(700,30,"comicsans",20,"**CHOOSE IMAGE**",(0,0,0)))
buttons.append(button(980,30,"comicsans",20,"**FEED IMAGE**",(0,0,0)))

while not pygame.event.get(pygame.QUIT):

    clock.tick(fps)

    if mouse_click:=pygame.event.get(pygame.MOUSEBUTTONDOWN):
        if buttons[0].rect.collidepoint(mouse_click[0].pos):
            sudoku_window.create_solve_thread()
        elif buttons[1].rect.collidepoint(mouse_click[0].pos):
            sudoku_window.gen_puzzel()
        elif buttons[2].rect.collidepoint(mouse_click[0].pos):
            sudoku_window.reset()
        elif buttons[3].rect.collidepoint(mouse_click[0].pos):
            image_section_window.grab_image()
        elif buttons[4].rect.collidepoint(mouse_click[0].pos) and image_section_window.image:
            image_section_window.feed_image()
            sudoku_window.grid = image_section_window.digit_dict

    win.fill((230,230,230))

    image_section_window.run()
    sudoku_window.run()

    for btn in buttons: btn.draw(win)
    
    pygame.display.update()

pygame.quit()