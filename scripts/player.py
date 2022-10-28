import pygame

from scripts.support import import_folder


class Player():
    def __init__(self, pos, screen):

        self.import_assets()

        self.screen = screen

        self.jump_speed = -12
        self.move_speed = 6

        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.6

        self.frame_index = 0
        self.animation_speed = 0.28

        self.img = self.animations['idle'][self.frame_index]

        self.rect = self.img.get_rect(topleft=pos)

        self.status = 'idle'
        self.face_right = True

    def import_assets(self):
        character_path = 'assets/character/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        if self.status == 'idle':
            self.frame_index += (self.animation_speed - 0.15)
        else:
            self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            self.frame_index = 0

        img = animation[int(self.frame_index)]

        if self.face_right:
            self.img = img
        else:
            self.img = pygame.transform.flip(img, True, False)

    def get_state(self):

        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:

            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jumpfunct(self):
        self.direction.y = self.jump_speed

    def getInput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.face_right = False

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.face_right = True

        else:
            self.direction.x = 0

        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and self.direction.y == 0:
            self.jumpfunct()

    def update(self):

        self.getInput()
        self.get_state()
        self.animate()

    def draw(self, surf):

        surf.blit(self.img, (self.rect.x, self.rect.y))
