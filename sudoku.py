import pygame
from threading import Thread
from time import sleep
from random import randint

class sudoku():
    def __init__(self,win,x,y,width,height):
        self.win = win
        self.rel_x = x
        self.rel_y = y
        self.rect = pygame.Rect(x,y,width,height)
        self.animation_grid = [[self.rel_x,self.rel_y]]
        self.grid = {i:{j:{"value":0,"lock":False} for j in range(9)}for i in range(9)}
        self.head = 0
        self.start = True
        self.current_cell = (self.rel_x,self.rel_y)
        self.is_solved = False
        self.delay = 0.00001
        self.is_error = False
        self.error_surf = self.draw_text('  Given Sudoku is Unsolvable!!  ',(200,0,0))

        Thread(target=self.animation,daemon=True).start()
        self.solve_thread = None

    def setup_puzzle(self,value_dict_2d:dict={}):
        self.current_cell = (self.rel_x,self.rel_y)
        self.grid=value_dict_2d.copy()
        
        self.animation_grid.clear()
        self.animation_grid.append([self.rel_x,self.rel_y])
        self.head = 0

    def is_vaild(self,grid,y,x,n):
        for i in range(9):
            if grid[y][i]["value"] == n or grid[i][x]["value"] == n:
                return False

        x1 = x - x%3
        y1 = y - y%3

        for i in range(3):
            for j in range(3):
                if grid[y1+i][x1+j]["value"] == n:
                    return False

        return True

    def solve(self,grid,y,is_gen):
        for i in range(y,9):
            for j in range(9):
                if grid[i][j]["value"] != 0: continue
                for k in range(1,10):
                    if self.is_vaild(grid,i,j,k):
                        self.current_cell = (j*50+self.rel_x,i*50+self.rel_y)
                        grid[i][j]["value"] = k
                        if not is_gen: sleep(self.delay)
                        self.solve(grid,y,is_gen)
                        if self.is_solved: return
                        grid[i][j]["value"] = 0
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
                        self.animation_grid.append([i*50+self.rel_x,(self.head)*50+self.rel_y])
                        self.animation_grid.append([(self.head)*50+self.rel_x,i*50+self.rel_y])
                    self.animation_grid.append([(self.head)*50+self.rel_x,(self.head)*50+self.rel_y])
                sleep(0.05)
            else:
                sleep(0.2)
    
    def draw_text(self,txt,color=(0,0,0)):
        return pygame.font.SysFont("comicsans",20,True).render(txt,True,color)

    def is_solvable(self,grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j]["value"] != 0:
                    for x in range(len(grid[i])):
                        if x != j and grid[i][x]["value"] == grid[i][j]["value"]:   
                            return False
                    for y in range(len(grid[j])):
                        if y != i and grid[y][j]["value"] == grid[i][j]["value"]:   
                            return False
            subgrid_nums = []
            start_row = (i // 3) * 3
            start_col = (i % 3) * 3
            for x in range(start_row, start_row + 3):
                for y in range(start_col, start_col + 3):
                    if grid[x][y]["value"] != 0:
                        if grid[x][y]["value"] in subgrid_nums:
                            return False
                        subgrid_nums.append(grid[x][y]["value"])
        return True
    
    def create_solve_thread(self):
        self.is_error = False
        if not self.is_solvable(self.grid):
            self.is_error = True
            return
        if self.start:
            self.is_solved=False
            self.start=False
            self.solve_thread=Thread(target=self.solve,args=(self.grid,0,False),daemon=True)
            self.solve_thread.start()

    def draw(self):

        if self.head >= 8:
            for i in range(1,3):
                pygame.draw.line(self.win,(20,20,20),(self.rel_x+150*i-1,self.rel_y),(self.rel_x+150*i-1,self.rel_y+450),4)
                pygame.draw.line(self.win,(20,20,20),(self.rel_x,self.rel_y+150*i-1),(self.rel_x+450,self.rel_y+150*i-1),4)
        
        for pos in self.animation_grid:
            key_y,key_x = pos[1]//50-2,pos[0]//50-1
            pygame.draw.rect(self.win,(0,0,0),(pos[0],pos[1],50,50),1,5)
            pygame.draw.rect(self.win,(0,180,0),(self.current_cell[0],self.current_cell[1],50,50),4,5)
            if self.grid[key_y][key_x]["lock"]: self.win.blit(self.draw_text(f'{self.grid[key_y][key_x]["value"]}'),(pos[0]+20,pos[1]+10))
            else: self.win.blit(self.draw_text(f'{self.grid[key_y][key_x]["value"]}',(0,200,0)),(pos[0]+20,pos[1]+10))

        if self.is_error: self.win.blit(self.error_surf,(100,560))


    def reset(self):
        self.grid = {i:{j:{"value":0,"lock":False} for j in range(9)}for i in range(9)}
        self.current_cell = (self.rel_x,self.rel_y)
        self.animation_grid.clear()
        self.animation_grid.append([self.rel_x,self.rel_y])
        self.head = 0
        self.is_error = False

    def gen_puzzel(self):
        board = {i:{j:{'value':0,'lock':True} for j in range(9)} for i in range(9)}
        board[randint(0,8)][randint(0,8)]['value'] = randint(1,9)
        self.is_solved = False
        self.solve(board,0,True)
        for _ in range(40):
            x,y = randint(0,8),randint(0,8)
            board[x][y]={'value':0,'lock':False}
            board[y][x]={'value':0,'lock':False}
        self.setup_puzzle(board)

    def run(self):
        self.draw()
