from curses import window
from turtle import right
from numpy import character
import pygame

screen = pygame.display.set_mode((1400, 800))

class tiles:
    def __init__(self):
        self.bottom_left = pygame.image.load("./assets/tileset/bottom-left.png")
        self.bottom_right = pygame.image.load("./assets/tileset/bottom-right.png")
        self.bottom = pygame.image.load("./assets/tileset/bottom.png")
        self.left = pygame.image.load("./assets/tileset/left.png")
        self.main = pygame.image.load("./assets/tileset/main.png")
        self.right = pygame.image.load("./assets/tileset/right.png")
        self.top_left = pygame.image.load("./assets/tileset/top-left.png")
        self.top_right = pygame.image.load("./assets/tileset/top-right.png")
        self.top = pygame.image.load("./assets/tileset/top.png")
        self.debel = pygame.image.load("./assets/debel.png")
        self.character = pygame.image.load("./assets/character/idle/1.png")
    def drawmenu(self):
        screen.blit(pygame.transform.scale(self.top_left, (50, 50)), (0, 0))
        screen.blit(pygame.transform.scale(self.top, (50, 50)), (50, 0))
        screen.blit(pygame.transform.scale(self.top_right, (50, 50)), (100, 0))
        screen.blit(pygame.transform.scale(self.left, (50, 50)), (0, 50))
        screen.blit(pygame.transform.scale(self.main, (50, 50)), (50, 50))
        screen.blit(pygame.transform.scale(self.right, (50, 50)), (100, 50))
        screen.blit(pygame.transform.scale(self.bottom_left, (50, 50)), (0, 100))
        screen.blit(pygame.transform.scale(self.bottom, (50, 50)), (50, 100))
        screen.blit(pygame.transform.scale(self.bottom_right, (50, 50)), (100, 100))
        screen.blit(pygame.transform.scale(self.debel, (50, 50)), (0, 150))
        screen.blit(pygame.transform.scale(self.character, (50, 50)), (50, 150))
        # draw a red 50x50 2 1 pixel grid from x,y 0, 0 to 150, 200
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 50, 50), 2)
        pygame.draw.rect(screen, (255, 0, 0), (50, 0, 50, 50), 2)
        pygame.draw.rect(screen, (255, 0, 0), (100, 0, 50, 50), 2)
        pygame.draw.rect(screen, (255, 0, 0), (0, 50, 50, 50), 2)
        pygame.draw.rect(screen, (255, 0, 0), (50, 50, 50, 50), 2)
        pygame.draw.rect(screen, (255, 0, 0), (100, 50, 50, 50), 2)
        pygame.draw.rect(screen, (255, 0, 0), (0, 100, 50, 50), 2)
        pygame.draw.rect(screen, (255, 0, 0), (50, 100, 50, 50), 2)
        pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50), 2)
        pygame.draw.rect(screen, (255, 0, 0), (0, 150, 50, 50), 2)
        pygame.draw.rect(screen, (255, 0, 0), (50, 150, 50, 50), 2)
        pygame.draw.rect(screen, (255, 0, 0), (100, 150, 50, 50), 2)
        pygame.display.flip()

class editor:
    def __init__(self):
        self.selected = "none"
        self.tiles = tiles()
        self.tiles.drawmenu();
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #the square have to be on a grid
                    #disable drawing from 0,0 to 150,200
                    if event.pos[0] > 0 and event.pos[0] < 162.5 and event.pos[1] > 0 and event.pos[1] < 212.6:
                        if event.pos[0] > 0 and event.pos[0] < 50 and event.pos[1] > 0 and event.pos[1] < 50:
                            self.selected = "top_left"
                        elif event.pos[0] > 50 and event.pos[0] < 100 and event.pos[1] > 0 and event.pos[1] < 50:
                            self.selected = "top"
                        elif event.pos[0] > 100 and event.pos[0] < 150 and event.pos[1] > 0 and event.pos[1] < 50:
                            self.selected = "top_right"
                        elif event.pos[0] > 0 and event.pos[0] < 50 and event.pos[1] > 50 and event.pos[1] < 100:
                            self.selected = "left"
                        elif event.pos[0] > 50 and event.pos[0] < 100 and event.pos[1] > 50 and event.pos[1] < 100:
                            self.selected = "main"
                        elif event.pos[0] > 100 and event.pos[0] < 150 and event.pos[1] > 50 and event.pos[1] < 100:
                            self.selected = "right"
                        elif event.pos[0] > 0 and event.pos[0] < 50 and event.pos[1] > 100 and event.pos[1] < 150:
                            self.selected = "bottom_left"
                        elif event.pos[0] > 50 and event.pos[0] < 100 and event.pos[1] > 100 and event.pos[1] < 150:
                            self.selected = "bottom"
                        elif event.pos[0] > 100 and event.pos[0] < 150 and event.pos[1] > 100 and event.pos[1] < 150:
                            self.selected = "bottom_right"
                        elif event.pos[0] > 0 and event.pos[0] < 50 and event.pos[1] > 150 and event.pos[1] < 200:
                            self.selected = "debel"
                        elif event.pos[0] > 50 and event.pos[0] < 100 and event.pos[1] > 150 and event.pos[1] < 200:
                            self.selected = "character"
                        elif event.pos[0] > 100 and event.pos[0] < 150 and event.pos[1] > 150 and event.pos[1] < 200:
                            self.selected = "none"
                        print(self.selected)
                    else:
                        self.x = event.pos[0] - event.pos[0] % 20
                        self.y = event.pos[1] - event.pos[1] % 20
                        #draw the selected tile
                        if self.selected == "top_left":
                            screen.blit(pygame.transform.scale(self.tiles.top_left, (20, 20)), (self.x, self.y))
                        elif self.selected == "top":
                            screen.blit(pygame.transform.scale(self.tiles.top, (20, 20)), (self.x, self.y))
                        elif self.selected == "top_right":
                            screen.blit(pygame.transform.scale(self.tiles.top_right, (20, 20)), (self.x, self.y))
                        elif self.selected == "left":
                            screen.blit(pygame.transform.scale(self.tiles.left, (20, 20)), (self.x, self.y))
                        elif self.selected == "main":
                            screen.blit(pygame.transform.scale(self.tiles.main, (20, 20)), (self.x, self.y))
                        elif self.selected == "right":
                            screen.blit(pygame.transform.scale(self.tiles.right, (20, 20)), (self.x, self.y))
                        elif self.selected == "bottom_left":
                            screen.blit(pygame.transform.scale(self.tiles.bottom_left, (20, 20)), (self.x, self.y))
                        elif self.selected == "bottom":
                            screen.blit(pygame.transform.scale(self.tiles.bottom, (20, 20)), (self.x, self.y))
                        elif self.selected == "bottom_right":
                            screen.blit(pygame.transform.scale(self.tiles.bottom_right, (20, 20)), (self.x, self.y))
                        elif self.selected == "debel":
                            screen.blit(pygame.transform.scale(self.tiles.debel, (20, 20)), (self.x, self.y))
                        elif self.selected == "character":
                            screen.blit(pygame.transform.scale(self.tiles.character, (20, 20)), (self.x, self.y))
                        elif self.selected == "none":
                            #draw a black square
                            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 20, 20), 0)
                        pygame.display.flip()
editor()