import os

import pygame

from scripts.button import Button
from scripts.displaytext import Textbox
from scripts.door import door
from scripts.enemy import EnemyFly
from scripts.kebab import Kebab
from scripts.player import Player
from scripts.settings import *
from scripts.tile import Tile
from scripts.window import Window

pause_background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "pausebg.png")), (1400, 800))


class PauseMenu:

    def __init__(self, pause_time, screen):
        self.window = Window(screen)
        self.pause_time = pause_time

    def build(self):
        window = self.window

        window.add_background(pause_background)


class Level:
    def __init__(self, level_data, surface, start_instructions=False, time_offset=0):
        self.display_surface = surface

        self.start_bool = start_instructions

        self.level_data = level_data

        self.time_offset = time_offset

        t = tile_size

        self.pause_menu_list = []

        self.main = pygame.transform.scale(pygame.image.load('assets/tileset/main.png'), (t, t))
        self.left = pygame.transform.scale(pygame.image.load('assets/tileset/left.png'), (t, t))
        self.right = pygame.transform.scale(pygame.image.load('assets/tileset/right.png'), (t, t))
        self.topright = pygame.transform.scale(pygame.image.load('assets/tileset/top-right.png'), (t, t))
        self.topleft = pygame.transform.scale(pygame.image.load('assets/tileset/top-left.png'), (t, t))
        self.bottomleft = pygame.transform.scale(pygame.image.load('assets/tileset/bottom-left.png'), (t, t))
        self.bottomright = pygame.transform.scale(pygame.image.load('assets/tileset/bottom-right.png'), (t, t))
        self.top = pygame.transform.scale(pygame.image.load('assets/tileset/top.png'), (t, t))
        self.bottom = pygame.transform.scale(pygame.image.load('assets/tileset/bottom.png'), (t, t))

        self.robot = pygame.transform.scale(pygame.image.load('assets/debel.png'), (66, 66))
        self.kebab = [pygame.transform.scale(pygame.image.load('assets/hp.png'), (36, 48)),
                      pygame.transform.scale(pygame.image.load('assets/hp2.png'), (36, 48)),
                      pygame.transform.scale(pygame.image.load('assets/hp3.png'), (36, 48))]
        self.font = pygame.font.Font('assets/alagard.ttf', 45)

        self.kebab_pos = []

        self.captured_kebab_imgs = [pygame.transform.scale(pygame.image.load('assets/kebab/kebab1.png'), (24, 33)),
                                    pygame.transform.scale(pygame.image.load('assets/kebab/kebab2.png'), (24, 33)),
                                    pygame.transform.scale(pygame.image.load('assets/kebab/kebab3.png'), (24, 33)),
                                    pygame.transform.scale(pygame.image.load('assets/kebab/kebab4.png'), (24, 33))]

        self.resume = pygame.image.load(os.path.join("assets", "resume.png"))
        self.quit = pygame.image.load(os.path.join("assets", "quitpause.png"))

        self.started = False

        self.counter = 0

        self.door_img = pygame.transform.scale(pygame.image.load('assets/door.png'), (48, 64))

        self.setup_player(self.level_data['level_map'])
        self.setup_level(self.level_data['level_map'])

        self.shift = 0

        self.index = 0

        self.yshift = 0
        self.gravity = False
        self.stuck = False

        self.pausebutton = pygame.image.load(os.path.join("Assets", "pausebutton.png"))
        self.pause_button = Button(700, 100, self.pausebutton, self.display_surface)

        self.paused = False

        self.start_img = pygame.image.load('assets/text/movement_info.png')
        self.start_img2 = pygame.image.load('assets/text/podwale_info.png')
        self.start_instructions = Textbox(self.start_img, (220, 460), self.display_surface)
        self.start_instructions2 = Textbox(self.start_img2, (720, 660), self.display_surface)

        self.start_instructions_list = [self.start_instructions, self.start_instructions2]

        self.kebab_saved = 0

        self.ticker = 0

        self.playing_anim = False

        self.pause_offset = 0

        self.next_level = False

    def setup_player(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'P':
                    self.main_player = Player((x, y), self.display_surface)
                    self.px, self.py = x, y

    def setup_level(self, layout):
        self.tiles = []
        self.decos = []
        self.enemies = []
        self.captured_kebab = []

        level = self.level_data

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x, y), self.main)
                    self.tiles.append(tile)
                if cell == 'L':
                    tile = Tile((x, y), self.left)
                    self.tiles.append(tile)
                if cell == 'W':
                    tile = Tile((x, y), self.topleft)
                    self.tiles.append(tile)
                if cell == 'T':
                    tile = Tile((x, y), self.top)
                    self.tiles.append(tile)
                if cell == 'R':
                    tile = Tile((x, y), self.right)
                    self.tiles.append(tile)
                if cell == 'D':
                    tile = Tile((x, y), self.topright)
                    self.tiles.append(tile)
                if cell == 'A':
                    tile = Tile((x, y), self.bottomleft)
                    self.tiles.append(tile)
                if cell == 'S':
                    tile = Tile((x, y), self.bottomright)
                    self.tiles.append(tile)
                if cell == 'B':
                    tile = Tile((x, y), self.bottom)
                    self.tiles.append(tile)
                if cell == 'E':
                    tile = Tile((x, y), self.main)
                    self.tiles.append(tile)
                if cell == 'Q':
                    tile = Tile((x, y), self.main)
                    self.tiles.append(tile)
                if cell == 'Y':
                    tile = Tile((x, y), self.main)
                    self.tiles.append(tile)
                if cell == 'U':
                    tile = Tile((x, y), self.main)
                    self.tiles.append(tile)

                if cell == 's':
                    point = Kebab((x, y + 10), self.captured_kebab_imgs)
                    self.captured_kebab.append(point)
                    self.kebab_pos.append((x, y + 10))
                    self.counter += 1

                if cell == 'd':
                    self.door_obj = door((x, y - 16), self.door_img)

                if cell == 'e':
                    enemy = EnemyFly(self.robot, (x, y), self.display_surface, self.main_player.rect,
                                     level['enemy_dist'], level['enemy_speed'])
                    self.enemies.append(enemy)

    def horizontal_collision(self):
        player = self.main_player

        player.rect.x += player.direction.x * player.move_speed

        for tile in self.tiles:
            if tile.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = tile.rect.right
                elif player.direction.x > 0:
                    player.rect.right = tile.rect.left

        if player.rect.x >= win_width:
            player.rect.right = win_width
        elif player.rect.x <= 0:
            player.rect.left = 0

    def vertical_collision(self):
        player = self.main_player

        if not self.paused:
            player.apply_gravity()

        for tile in self.tiles:

            if tile.rect.colliderect(player.rect):

                if player.direction.y > 0:
                    player.rect.bottom = tile.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = tile.rect.bottom
                    player.direction.y = 0.1

        if player.rect.y >= win_height:
            self.reset()

    def bulletCollision(self):

        for tile in self.tiles:

            for enemy in self.enemies:
                for bullet in enemy.bullets[:]:
                    if bullet.bullet_rect.colliderect(tile):
                        enemy.bullets.remove(bullet)

    def enemy_bullet_player_collision(self):
        player = self.main_player

        for enemy in self.enemies:
            for bullet in enemy.bullets[:]:
                if bullet.bullet_rect.colliderect(player.rect):
                    self.index += 1
                    enemy.bullets.remove(bullet)

    def point_counter(self):

        if self.index > 2:
            self.reset()

        self.display_surface.blit(self.kebab[self.index], (1300, 60))

    def print_text(self):

        self.current_time = round(((pygame.time.get_ticks()) / 1000) - self.time_offset - self.pause_offset, 3)

        self.time_text = self.font.render(f"{self.current_time}", False, (255, 255, 255))
        self.display_surface.blit(self.time_text, (70, 65))

        self.point_text = self.font.render(f"{self.kebab_saved} / {self.counter}", False, (255, 255, 255))
        self.display_surface.blit(self.point_text, (70, 700))

    def reset(self):

        self.kebab_saved = 0
        self.index = 0

        self.main_player.rect.x, self.main_player.rect.y = self.px, self.py

        self.captured_kebab.clear()

        for pos in self.kebab_pos:
            point = Kebab(pos, self.captured_kebab_imgs)
            self.captured_kebab.append(point)

        if len(self.captured_kebab) < self.counter:
            pos_list = []

            for pos in self.kebab_pos:

                for point in self.captured_kebab:
                    pos_list.append(point.pos)

                    if pos not in pos_list:
                        self.captured_kebab.append(Kebab(pos, self.captured_kebab_imgs))

    def build_pause_menu(self):

        for pause in self.pause_menu_list:
            pause.build()

            if pause.window.add_button((200, 90), self.resume):
                self.paused = False

                resume_time = pygame.time.get_ticks()
                print(pause.pause_time)
                print(resume_time)

                time_paused = resume_time - pause.pause_time
                print(time_paused / 1000)

                self.pause_offset += time_paused / 1000

                self.pause_menu_list.remove(pause)

            if pause.window.add_button((200, 240), self.quit):
                pygame.quit()

    def run(self):

        if self.kebab_saved == self.counter:
            self.permittable = True
        else:
            self.permittable = False

        self.door_obj.draw(self.display_surface)

        if self.door_obj.rect.colliderect(self.main_player.rect) and self.permittable:
            self.next_level = True

        for tile in self.tiles:
            tile.draw(self.display_surface)

        for enemy in self.enemies:
            enemy.draw()
            if self.start_bool:

                if not self.paused and self.started:
                    enemy.update()

            else:
                if not self.paused:
                    enemy.update()

        for point in self.captured_kebab:
            point.draw(self.display_surface)
            point.animate()

            if point.rect.colliderect(self.main_player.rect):
                self.captured_kebab.remove(point)
                self.kebab_saved += 1

        if self.start_bool:

            self.start_instructions2.draw()
            self.start_instructions.draw()
            if self.main_player.direction.x != 0:
                self.start_instructions2.remove()
                self.start_instructions.remove()
                self.started = True

        if not self.paused:
            self.main_player.update()
            self.horizontal_collision()

        self.vertical_collision()

        self.main_player.draw(self.display_surface)

        self.bulletCollision()

        if not self.paused:
            self.print_text()
        if self.start_bool:
            if self.started:
                self.enemy_bullet_player_collision()
        elif not self.start_bool:
            self.enemy_bullet_player_collision()
        self.point_counter()

        if self.pause_button.draw() and not self.paused:
            self.paused = True

            pause_time = pygame.time.get_ticks()
            self.pause_menu_list.append(PauseMenu(pause_time, self.display_surface))
        self.build_pause_menu()
