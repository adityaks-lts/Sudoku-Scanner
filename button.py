from pygame import font, draw

class button():
    def __init__(self,x,y,font_style,font_size,text,font_color,background_color=None):
        try:
            self.surf = font.SysFont(font_style,font_size,True).render(text,True,font_color,background_color)
            self.rect = self.surf.get_rect(topleft=(x,y))
        except Exception as e:
            print(e)

    def draw(self,win):
        draw.rect(win,(130,150,130),self.rect,2,8)
        win.blit(self.surf,self.rect)