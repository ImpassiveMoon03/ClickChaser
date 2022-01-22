import pygame
from pygame import mouse
from pygame.locals import *

class Button:
    def __init__(self, *, width:int, height:int, posx:int, posy:int, button_text:str = None, border_color:tuple = None, fill_color:tuple ,text_color:tuple = (0,0,0), font_size:int = None):
        self.rect = pygame.Rect(posx, posy, width, height)
        self.border = pygame.Rect(posx, posy, width, height)
        self.button_text = button_text
        if self.button_text is not None:
            if font_size is None:
                font_size = 32
            self.font_size = font_size
            self.font = pygame.font.SysFont("georgia", font_size)
            self.textbox = self.font.render(button_text, True, (text_color))
        else:
            self.textbox = None
        self.width = width
        self.height = height
        self.posx = posx
        self.posy = posy
        self.border_color = border_color
        self.fill_color = fill_color
        if self.border_color is None:
            self.border_color = self.fill_color
        self.text_color = text_color
        self.font_size = font_size
    
    def render(self, screen):
        pygame.draw.rect(screen, self.fill_color, self.rect)
        pygame.draw.rect(screen, self.border_color, self.border, 2)
        if self.textbox is not None:
            screen.blit(self.textbox, (self.width/2 - self.textbox.get_width() / 2 + self.posx, self.height/2 - self.textbox.get_height() / 2 + self.posy))

    def clicked(self, event):
        return (mouse.get_pos()[0] < self.width + self.posx
        and mouse.get_pos()[0] > self.posx
        and mouse.get_pos()[1] < self.height + self.posy
        and mouse.get_pos()[1] > self.posy
        and event.type == pygame.MOUSEBUTTONDOWN)
    
    def hovered(self, screen):
        return (mouse.get_pos()[0] < self.width + self.posx
        and mouse.get_pos()[0] > self.posx
        and mouse.get_pos()[1] < self.height + self.posy
        and mouse.get_pos()[1] > self.posy)
    
    def move(self, posx:int, posy:int):
        self.rect = pygame.Rect(posx, posy, self.width, self.height)
        self.border = pygame.Rect(posx, posy, self.width, self.height)
        self.posx = posx
        self.posy = posy
    
    def resize(self, width, height):
        self.rect = pygame.Rect(self.posx, self.posy, width, height)
        self.border = pygame.Rect(self.posx, self.posy, width, height)
        self.width = width
        self.height = height
        self.font_size = self.width / 4
        self.font = pygame.font.SysFont("georgia", round(self.font_size))
        self.textbox = self.font.render(self.button_text, True, (self.text_color))