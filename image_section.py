import pygame
from tkinter.filedialog import askopenfile
import os

class button():
    def __init__(self,x,y,font,font_size,text,foreground_color,background_color=None):
        try:
            self.surf = pygame.font.SysFont(font,font_size,True).render(text,True,foreground_color,)
            self.rect = self.surf.get_rect(topleft=(x,y))
        except Exception as e:
            print(e)
    
    def draw(self,win):
        pygame.draw.rect(win,(130,150,130),self.rect,2,8)
        win.blit(self.surf,self.rect)

class image_section():
    def __init__(self,win,x,y,width,height):
        self.win = win
        self.first = True
        self.surface = pygame.Surface((width,height))
        self.rect = self.surface.get_rect(topleft=(x,y))
        self.browse_button = button(40,10,"comicsans",20,"***CHOOSE IMAGE***",(0,0,0))
        self.feed_button = button(width//2+60,10,"comicsans",20,"***FEED IMAGE***",(0,0,0))
        self.surface.fill((250,250,250))
        self.image = None
    
    def grab_image(self):
        temp = askopenfile('rb',defaultextension = '.png',filetypes = [("png",".png"),("jpeg",[".jpeg",".jpg"])],initialdir=os.getcwd(),title="select image file ")
        if temp:
            self.image = temp
            self.image = pygame.transform.smoothscale(pygame.image.load(self.image).convert_alpha(),(450,450))
            self.first = True

    def feed_image(self):
        if self.image:
            print("***feed***")

    def draw(self):
        self.win.blit(self.surface,self.rect)
        m_x,m_y = pygame.mouse.get_pos()
        if self.rect.collidepoint((m_x,m_y)) or self.first:
            self.first = False

            m_x-=self.rect.x
            m_y-=self.rect.y

            self.surface.fill((250,250,250))

            self.browse_button.draw(self.surface)
            self.feed_button.draw(self.surface)

            if self.image: self.surface.blit(self.image,(50,50))

            keys = pygame.mouse.get_pressed()
            
            if keys:
                if self.browse_button.rect.collidepoint((m_x,m_y)) and keys[0]:
                    self.grab_image()

                elif self.feed_button.rect.collidepoint((m_x,m_y)) and keys[0]:
                    self.feed_image()