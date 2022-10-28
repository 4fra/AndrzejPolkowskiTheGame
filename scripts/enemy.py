import pygame

from scripts.bullet import Bullet2


class EnemyFly:

    def __init__(self, img, pos, screen, rect, dist, speed):

        self.pos = pos
        self.img = img

        self.original_pos = pos

        self.rect = self.img.get_rect(center=pos)

        self.bullet_surf = pygame.Surface((12.75, 6)).convert_alpha()

        self.screen = screen

        self.bullets = []

        self.shot = False

        self.cooldown = 1200

        self.speed = speed

        self.player_rect = rect

        self.rects = []

        self.create_rects(dist)

    def create_rects(self, dist):

        self.rect_left = pygame.Rect((self.pos[0] - dist, self.pos[1]), (2, 44))
        self.rect_right = pygame.Rect((self.pos[0] + dist, self.pos[1]), (2, 44))

        self.rects.append(self.rect_left)
        self.rects.append(self.rect_right)

    def bullet_recharge(self):

        if self.shot:
            current_time = pygame.time.get_ticks()
            if current_time - self.bullet_time >= self.cooldown:
                self.shot = False

    def bullet_update_draw(self):

        if self.shot == False:
            self.bullets.append(Bullet2(self.rect.centerx, self.rect.bottom, self.bullet_surf, self.player_rect))
            self.shot = True
            self.bullet_time = pygame.time.get_ticks()

        for bullet in self.bullets[:]:
            bullet.draw(self.screen)
            bullet.update()

    def draw(self):

        self.screen.blit(self.img, (self.rect.x, self.rect.y))

    def movement(self):

        self.rect.x += self.speed

        for rect in self.rects:
            if rect.colliderect(self.rect):
                self.speed *= -1
                self.img = pygame.transform.flip(self.img, True, False)

    def update(self):

        self.bullet_recharge()
        self.bullet_update_draw()
        self.movement()
