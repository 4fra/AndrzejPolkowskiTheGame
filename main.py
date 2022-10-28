import os

import pygame
from pygame.locals import *

from scripts.level import Level
from scripts.settings import *
from scripts.window import Window


class PlayerGame:
    def __init__(self, time):

        self.level = Level(level1, screen, True, time)

        self.level1 = [self.level]
        self.level2 = []
        self.level2 = []
        self.level3 = []

    def run(self):

        for level in self.level1:
            level.run()
            if level.next_level:
                self.level1.clear()
                self.level2.append(Level(level2, screen))
        for level in self.level2:
            level.run()
            if level.next_level:
                self.level2.clear()
                self.level3.append(Level(level3, screen))

        for level in self.level3:
            level.run()
            if level.next_level:
                timer = level.current_time
                self.level3.clear()
                end_loop(timer)


class MainMenu:

    def __init__(self):
        self.window = Window(screen)

    def build(self):
        window = self.window

        pygame.display.set_caption('Podwale')
        pygame.display.set_icon(player_img)

        window.add_background(background)
        window.add_text('Podwale', (425, 250), 150, (255, 255, 255))
        window.add_image((1400 - 390, 400), player_img)

    def build_buttons(self):
        window = self.window
        clicked = False

        if window.add_button((700, 600), start):
            clicked = True

        return clicked


class InfoMenu:
    def __init__(self):
        self.window = Window(screen)

    def build(self):
        self.window.add_background(background)
        self.window.add_background(pause_background)


class EndMenu:

    def __init__(self, time):
        self.window = Window(screen)
        self.time = time

    def build(self):
        self.window.add_background(background)
        self.window.add_text('Gratulacje! Uciekles z podwala!', (160, 250), 80, (255, 255, 255))
        self.window.add_text('Twoj czas: ' + str(self.time) + ' s', (400, 500), 60, (255, 255, 255))


if __name__ == '__main__':

    pygame.init()

    infostuffs = pygame.display.Info()

    monitorx, monitory = infostuffs.current_w, infostuffs.current_h

    dispx, dispy = win_width, win_height

    if dispx > monitorx:
        dispy /= dispx / monitorx
        dispx = monitorx
    if dispy > monitory:
        dispx /= dispy / monitory
        dispy = monitory

    dispx = int(dispx)
    dispy = int(dispy)

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((dispx, dispy), pygame.FULLSCREEN)

    bg_colour = (12, 12, 26)

    p_width, p_height = 44, 56

    player_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "character", 'idle', '1.png')),
                                        (p_width, p_height))

    start = pygame.image.load(os.path.join("assets", "start.png"))
    resume = pygame.image.load(os.path.join("assets", "resume.png"))
    pause_background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pausebg.png")), (1400, 800))

    background = pygame.transform.scale(pygame.image.load('assets/zslbackground.png'), (1400, 800))

    player_img = pygame.transform.scale(pygame.image.load('assets/titleimg.png'), (390, 426))

    paused = False

    main_menu = MainMenu()
    info_menu = InfoMenu()


    def playerLoop(game):

        run = True
        while run:
            clock.tick(45)
            screen.fill(bg_colour)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
            game.run()

            pygame.display.flip()


    def start_loop():

        run = True
        while run:
            clock.tick(45)
            screen.fill(bg_colour)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()

            main_menu.build()
            if main_menu.window.add_button((700, 600), start):
                start_time = pygame.time.get_ticks() / 1000
                game = PlayerGame(start_time)
                playerLoop(game)

            pygame.display.flip()


    def info_loop():
        run = True
        while run:
            clock.tick(45)
            screen.fill(bg_colour)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()

            info_menu.build()


    def end_loop(time):
        run = True
        while run:
            clock.tick(45)
            screen.fill(bg_colour)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()

            end_menu = EndMenu(time)

            end_menu.build()

            pygame.display.flip()


    start_loop()
