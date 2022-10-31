from time import sleep
import pygame

pygame.init()
screen = pygame.display.set_mode((750, 400))

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
        self.coin = pygame.image.load("./assets/kebab/kebab1.png")
        self.door = pygame.image.load("./assets/door.png")
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
        screen.blit(pygame.transform.scale(self.coin, (50, 50)), (0, 200))
        screen.blit(pygame.transform.scale(self.door, (50, 50)), (50, 200))
        self.font = pygame.font.Font('./assets/alagard.ttf', 45)
        self.save = self.font.render("Save", True, (255, 255, 255))
        self.load = self.font.render("Load", True, (255, 255, 255))
        screen.blit(self.save, (0, 350))
        screen.blit(self.load, (0, 300))
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
        pygame.draw.rect(screen, (255, 0, 0), (0, 200, 50, 50), 2)
        pygame.draw.rect(screen, (255, 0, 0), (50, 200, 50, 50), 2)
        pygame.draw.rect(screen, (0, 255, 0), (160, 0, 590, 400), 2)
        pygame.draw.rect(screen, (255, 0, 0), (0, 200, 50, 50), 2)
        pygame.display.flip()

class editor:
    # left = L, right = R, top = T, bottom = B, main = X, topleft = W, topright = D, bottomleft = A, bottomright = S, insidetopleft = Q, insidetopright = E, insidebottomright = Y, insidebottomleft = U e = debel, s = coin, c = character, d = door
    map = [
        '                              ',
        '                              ',
        '                              ',
        '                              ',
        '                              ',
        '                              ',
        '                              ',                              
        '                              ',
        '                              ',
        '                              ',
        '                              ',
        '                              ',
        '                              ',
        '                              ',
        '                              ',
        '                              ',
        '                              ',
        '                              ',
        '                              ',
        '                              ',
        ]
    x = 0
    y = 0
    def level_map(self):
        self.pos_x = round(self.x / 20 - 8)
        self.pos_y = round(self.y / 20)
        if self.pos_x >= 0 and self.pos_x <= 30 and self.pos_y >= 0 and self.pos_y <= 19:
            self.map[self.pos_y] = self.map[self.pos_y][:self.pos_x] + self.symbol + self.map[self.pos_y][self.pos_x + 1:]
        #reverse the process to redraw the map
        for self.y in range(0, 400, 20):
            for self.x in range(160, 750, 20):
                if self.map[round(self.y / 20)][round((self.x - 160) / 20)] == 'X':
                    screen.blit(pygame.transform.scale(self.tiles.main, (20, 20)), (self.x, self.y))
                elif self.map[round(self.y / 20)][round((self.x - 160) / 20)] == 'L':
                    screen.blit(pygame.transform.scale(self.tiles.left, (20, 20)), (self.x, self.y))
                elif self.map[round(self.y / 20)][round((self.x - 160) / 20)] == 'R':
                    screen.blit(pygame.transform.scale(self.tiles.right, (20, 20)), (self.x, self.y))
                elif self.map[round(self.y / 20)][round((self.x - 160) / 20)] == 'T':
                    screen.blit(pygame.transform.scale(self.tiles.top, (20, 20)), (self.x, self.y))
                elif self.map[round(self.y / 20)][round((self.x - 160) / 20)] == 'B':
                    screen.blit(pygame.transform.scale(self.tiles.bottom, (20, 20)), (self.x, self.y))
                elif self.map[round(self.y / 20)][round((self.x - 160) / 20)] == 'W':
                    screen.blit(pygame.transform.scale(self.tiles.top_left, (20, 20)), (self.x, self.y))
                elif self.map[round(self.y / 20)][round((self.x - 160) / 20)] == 'D':
                    screen.blit(pygame.transform.scale(self.tiles.top_right, (20, 20)), (self.x, self.y))
                elif self.map[round(self.y / 20)][round((self.x - 160) / 20)] == 'A':
                    screen.blit(pygame.transform.scale(self.tiles.bottom_left, (20, 20)), (self.x, self.y))
                elif self.map[round(self.y / 20)][round((self.x - 160) / 20)] == 'S':
                    screen.blit(pygame.transform.scale(self.tiles.bottom_right, (20, 20)), (self.x, self.y))
                elif self.map[round(self.y / 20)][round((self.x - 160) / 20)] == 'e':
                    screen.blit(pygame.transform.scale(self.tiles.debel, (20, 20)), (self.x, self.y))
                elif self.map[round(self.y / 20)][round((self.x - 160) / 20)] == 's':
                    screen.blit(pygame.transform.scale(self.tiles.coin, (20, 20)), (self.x, self.y))
                elif self.map[round(self.y / 20)][round((self.x - 160) / 20)] == 'C':
                    screen.blit(pygame.transform.scale(self.tiles.character, (20, 20)), (self.x, self.y))
                elif self.map[round(self.y / 20)][round((self.x - 160) / 20)] == 'd':
                    screen.blit(pygame.transform.scale(self.tiles.door, (20, 20)), (self.x, self.y))
        pygame.display.flip()
        print(self.map)
    def save(self):
        with open("./editor/level.txt", "w") as file:
            file.write(str(self.map))
            file.close()
    def load(self):
        with open("./editor/level.txt", "r") as file:
            pygame.draw.rect(screen, (0, 0, 0), (160, 0, 590, 400), 0)
            self.map = file.read()
            self.map = self.map.replace(', ', ',')
            self.map = self.map.replace('[', '')
            self.map = self.map.replace(']', '')
            self.map = self.map.replace("'", '')
            self.map = self.map.split(',')
            file.close()
    def __init__(self):
        self.selected = "none"
        self.tiles = tiles()
        self.tiles.drawmenu()
        self.symbol = " "
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if event.pos[0] > 0 and event.pos[0] < 162.5 and event.pos[1] > 0 and event.pos[1] < 250:
                        if event.pos[0] > 0 and event.pos[0] < 50 and event.pos[1] > 0 and event.pos[1] < 50:
                            self.selected = "top_left"
                            self.symbol = "W"
                        elif event.pos[0] > 50 and event.pos[0] < 100 and event.pos[1] > 0 and event.pos[1] < 50:
                            self.selected = "top"
                            self.symbol = "T"
                        elif event.pos[0] > 100 and event.pos[0] < 150 and event.pos[1] > 0 and event.pos[1] < 50:
                            self.selected = "top_right"
                            self.symbol = "D"
                        elif event.pos[0] > 0 and event.pos[0] < 50 and event.pos[1] > 50 and event.pos[1] < 100:
                            self.selected = "left"
                            self.symbol = "L"
                        elif event.pos[0] > 50 and event.pos[0] < 100 and event.pos[1] > 50 and event.pos[1] < 100:
                            self.selected = "main"
                            self.symbol = "X"
                        elif event.pos[0] > 100 and event.pos[0] < 150 and event.pos[1] > 50 and event.pos[1] < 100:
                            self.selected = "right"
                            self.symbol = "R"
                        elif event.pos[0] > 0 and event.pos[0] < 50 and event.pos[1] > 100 and event.pos[1] < 150:
                            self.selected = "bottom_left"
                            self.symbol = "A"
                        elif event.pos[0] > 50 and event.pos[0] < 100 and event.pos[1] > 100 and event.pos[1] < 150:
                            self.selected = "bottom"
                            self.symbol = "B"
                        elif event.pos[0] > 100 and event.pos[0] < 150 and event.pos[1] > 100 and event.pos[1] < 150:
                            self.selected = "bottom_right"
                            self.symbol = "S"
                        elif event.pos[0] > 0 and event.pos[0] < 50 and event.pos[1] > 150 and event.pos[1] < 200:
                            self.selected = "debel"
                            self.symbol = "e"
                        elif event.pos[0] > 50 and event.pos[0] < 100 and event.pos[1] > 150 and event.pos[1] < 200:
                            self.selected = "character"
                            self.symbol = "C"
                        elif event.pos[0] > 100 and event.pos[0] < 150 and event.pos[1] > 150 and event.pos[1] < 200:
                            self.selected = "none"
                            self.symbol = " "
                        elif event.pos[0] > 0 and event.pos[0] < 50 and event.pos[1] > 200 and event.pos[1] < 250:
                            self.selected = "coin"
                            self.symbol = "s"
                        elif event.pos[0] > 50 and event.pos[0] < 100 and event.pos[1] > 200 and event.pos[1] < 250:
                            self.selected = "door"
                            self.symbol = "d"
                        
                        print(self.selected)
                    elif event.pos[0] > 160 and event.pos[0] < 750 and event.pos[1] > 0 and event.pos[1] < 400:
                        self.x = event.pos[0] - event.pos[0] % 20
                        self.y = event.pos[1] - event.pos[1] % 20
                        print(self.x, self.y)
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
                            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 20, 20), 0)
                        elif self.selected == "coin":
                            screen.blit(pygame.transform.scale(self.tiles.coin, (20, 20)), (self.x, self.y))
                        elif self.selected == "door":
                            screen.blit(pygame.transform.scale(self.tiles.door, (20, 20)), (self.x, self.y))
                        self.level_map()
                        self.tiles.drawmenu()
                        pygame.display.flip()
                    #save the level when clicking save button
                    elif event.pos[0] > 0 and event.pos[0] < 162.5 and event.pos[1] > 350 and event.pos[1] < 400:
                        self.save()
                        print("saved")
                        self.tiles.drawmenu()
                        pygame.display.flip()
                    elif event.pos[0] > 0 and event.pos[0] < 162.5 and event.pos[1] > 300 and event.pos[1] < 350:
                        self.load()
                        print("loaded")
                        self.tiles.drawmenu()
                        self.level_map()
                        pygame.display.flip()


editor()