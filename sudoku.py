import pygame
from threading import Thread
from time import sleep

class sudoku():
    def __init__(self,win,x,y,width,height):
        self.win = win
        self.surface = pygame.Surface((width,height))
        self.rect = self.surface.get_rect(topleft=(x,y))
        self.animation_grid = [[50,50]]
        self.grid = {i:{j:{"value":0,"lock":False} for j in range(9)}for i in range(9)}
        self.head = 0
        self.start = True
        self.current_cell = (50,50)
        self.is_solved = False
        self.delay = 0.001

        self.animation_thread = Thread(target=self.animation,daemon=True)
        self.solve_thread = None

    def setup_puzzle(self,value_dict_2d:dict={}):
        self.current_cell = (50,50)
        for y in range(9):
            for x in range(9):
                if value_dict_2d.get(y) and value_dict_2d.get(y).get(x):
                    self.grid[y][x]["value"]=value_dict_2d[y][x]
                    self.grid[y][x]["lock"]=True
                else:
                    self.grid[y][x]["value"]=0
                    self.grid[y][x]["lock"]=False
        
        self.animation_grid.clear()
        self.animation_grid.append([50,50])
        self.head = 0

    def is_vaild(self,y,x,n):
        for i in range(9):
            if self.grid[y][i]["value"] == n:
                return False

        for i in range(9):
            if self.grid[i][x]["value"] == n:
                return False

        x1 = (x // 3)*3
        y1 = (y // 3)*3

        for i in range(3):
            for j in range(3):
                if self.grid[y1+i][x1+j]["value"] == n:
                    return False

        return True


    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j]["value"] == 0:
                    for k in range(1,10):
                        if self.is_vaild(i,j,k):
                            self.current_cell = (j*50+50,i*50+50)
                            self.grid[i][j]["value"] = k
                            sleep(self.delay)
                            self.solve()
                            if self.is_solved:
                                return    
                            self.grid[i][j]["value"] = 0
                    return
        self.is_solved = True
        self.start = True
        return

    def animation(self):
        while True:
            if self.head < 8:
                x = self.animation_grid[(self.head*(self.head+2))][0]

                if not x%50:
                    self.head+=1
                    for i in range(self.head):
                        self.animation_grid.append([i*50+50,(self.head)*50+50])
                        self.animation_grid.append([(self.head)*50+50,i*50+50])
                    self.animation_grid.append([(self.head)*50+50,(self.head)*50+50])
                sleep(0.05)
            else:
                sleep(0.2)
    
    def draw_text(self,txt):
        return pygame.font.SysFont("comicsans",20,True).render(txt,True,(0,0,0))

    def create_solve_thread(self):
        if self.start:
            self.is_solved=False
            self.start=False
            self.solve_thread=Thread(target=self.solve,daemon=True)
            self.solve_thread.start()

    def draw(self):
        self.win.blit(self.surface,self.rect)
        self.surface.fill((250,250,250))

        for pos in self.animation_grid:
            key_y,key_x = pos[1]//50-1,pos[0]//50-1
            pygame.draw.rect(self.surface,(0,0,0),(pos[0],pos[1],50,50),1,5)
            if self.grid[key_y][key_x]["lock"]: pygame.draw.rect(self.surface,(200,120,120),(pos[0]+10,pos[1]+10,30,30),2,4)
            pygame.draw.rect(self.surface,(0,180,0),(self.current_cell[0],self.current_cell[1],50,50),4,5)
            self.surface.blit(self.draw_text(f'{self.grid[key_y][key_x]["value"]}'),(pos[0]+20,pos[1]+10))

        if not self.animation_thread.is_alive(): self.animation_thread.start()
