from xml.dom.expatbuilder import parseFragmentString
import pygame
from pygame.locals import *
import random
from classes.Button import Button
from pygame import mouse

game_state = 0
score = 0
posx = 310
posy = 80
step = 1
cost = round((step/0.4)*(step/0.4))
high_score = 0

class Main():
    global game_state
    global score
    global posx
    global posy
    global step
    global cost
    global high_score

    def __init__(self):
        global game_state
        global score
        global posx
        global posy

        while game_state != 2:
            WIDTH, HEIGHT = 720, 480
            screen = self.setup("Clicker Game", WIDTH, HEIGHT)
            
            if game_state == 0:
                self.main_menu(screen)
            if game_state == 1:
                self.play_screen(screen)
            if game_state == 3:
                self.how_to_menu(screen)

    def setup(self, title, width, height):
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        pygame.init()
        return screen
    
    def reset(self):
        global game_state
        global score
        global posx
        global posy
        global step
        global cost

        game_state = 0
        score = 0
        posx = 310
        posy = 80
        step = 1
        cost = round((step/0.4)*(step/0.4))

    def main_menu(self, screen):
        global game_state

        font = pygame.font.SysFont("georgia", 20)
        welcometext = font.render("Welcome to ClickChaser!", True, (255, 255, 255))
        start_button = Button(
            width = 500,
            height = 30,
            posx = 110,
            posy = 15 + welcometext.get_height(),
            button_text = "Play!",
            border_color = (255,255,255),
            fill_color = (0,0,0),
            text_color = (255,255,255),
            font_size = 25
        )
        how_button = Button(
            width = 500,
            height = 30,
            posx = 110,
            posy = 50 + welcometext.get_height(),
            button_text = "How to Play",
            border_color = (255,255,255),
            fill_color = (0,0,0),
            text_color = (255,255,255),
            font_size = 25
        )
        quit_button = Button(
            width = 500,
            height = 30,
            posx = 110,
            posy = 85 + welcometext.get_height(),
            button_text = "Quit Game",
            border_color = (255,255,255),
            fill_color = (0,0,0),
            text_color = (255,0,0),
            font_size = 25
        )
        screen.fill((0,0,0))
        screen.blit(welcometext, (360 - welcometext.get_width() /2, 10))
        start_button.render(screen)
        how_button.render(screen)
        quit_button.render(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = 2
            if start_button.clicked(event):
                game_state = 1
            if how_button.clicked(event):
                game_state = 3
            if quit_button.clicked(event):
                game_state = 2
    
    def play_screen(self, screen):
        global game_state
        global score
        global posx
        global posy
        global step
        global cost
        global high_score

        clicker_button = Button(
            width = 100,
            height = 100,
            posx = posx,
            posy = posy,
            button_text = "Click",
            border_color = (255,255,255),
            fill_color = (0,0,0),
            text_color = (255,255,255),
            font_size = 25
        )
        upgrade_button = Button(
            width = 500,
            height = 30,
            posx = 110,
            posy = 40,
            button_text = F"Upgrade - Cost {cost}",
            border_color = (255,255,255),
            fill_color = (0,0,0),
            text_color = (255,255,255),
            font_size = 25
        )
        return_button = Button(
            width = 50,
            height = 20,
            posx = 10,
            posy = 5,
            button_text = "Menu",
            border_color = (255,255,255),
            fill_color = (0,0,0),
            text_color = (255,255,255),
            font_size = 15
        )
        font = pygame.font.SysFont("georgia", 20)
        screen.fill((0,0,0))
        scoretext = font.render(F"Score - {score}", True, (255,255,255))
        high_scoretext = font.render(F"High Score - {high_score}", True, (255,255,255))
        screen.blit(scoretext, (360 - scoretext.get_width()/2, 10))
        screen.blit(high_scoretext, (720 - high_scoretext.get_width(), 480 - high_scoretext.get_height()))
        clicker_button.render(screen)
        return_button.render(screen)
        upgrade_button.render(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = 2
            if clicker_button.clicked(event):
                score += step
                posx = random.randrange(15, 720 - 115)
                posy = random.randrange(90, 480 - 115)
                if high_score < score:
                    high_score = score
            if return_button.clicked(event):
                game_state = 0
            if upgrade_button.clicked(event):
                if score >= cost:
                    score -= cost
                    step += 1
                    cost = round((step/0.4)*(step/0.4))
            if mouse.get_pos()[1] > 80 and event.type == pygame.MOUSEBUTTONDOWN and not clicker_button.clicked(event):
                self.reset()
    
    def how_to_menu(self, screen):
        global game_state
        back_button = Button(
            width = 500,
            height = 30,
            posx = 110,
            posy = 10,
            button_text = "Go Back",
            border_color = (255,255,255),
            fill_color = (0,0,0),
            text_color = (255,255,255),
            font_size = 25
        )
        skip_button = Button(
            width = 500,
            height = 30,
            posx = 110,
            posy = 405,
            button_text = "Play Game",
            border_color = (255,255,255),
            fill_color = (0,0,0),
            text_color = (255,255,255),
            font_size = 25
        )
        quit_button = Button(
            width = 500,
            height = 30,
            posx = 110,
            posy = 440,
            button_text = "Quit Game",
            border_color = (255,255,255),
            fill_color = (0,0,0),
            text_color = (255,0,0),
            font_size = 25
        )
        font = pygame.font.SysFont("georgia", 20)
        line1 = font.render("Hello, and welcome to ImpassiveMoon's ClickChaser", True, (255,255,255))
        line2 = font.render("Playing the game is acutally quite simple! All you do", True, (255,255,255))
        line3 = font.render("is click the button, and then it will move. To increase", True, (255,255,255))
        line4 = font.render("your score, just follow the button and keep clicking it!", True, (255,255,255))
        screen.fill((0,0,0))
        back_button.render(screen)
        skip_button.render(screen)
        quit_button.render(screen)
        screen.blit(line1, (360 - line1.get_width()/2, 40))
        screen.blit(line2, (360 - line2.get_width()/2, 65))
        screen.blit(line3, (360 - line3.get_width()/2, 90))
        screen.blit(line4, (360 - line4.get_width()/2, 115))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = 2
            if back_button.clicked(event):
                game_state = 0
            if skip_button.clicked(event):
                game_state = 1
            if quit_button.clicked(event):
                game_state = 2


game = Main()