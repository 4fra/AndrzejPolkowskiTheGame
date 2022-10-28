class Kebab:
    def __init__(self, pos, img):
        self.index = 0

        self.pos = pos
        self.animation = img
        self.img = self.animation[0]
        self.rect = self.img.get_rect(topleft=self.pos)

        self.animate_speed = 0.08

    def animate(self):
        self.index += self.animate_speed

        if self.index >= len(self.animation):
            self.index = 0

        img = self.animation[int(self.index)]
        self.img = img

    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))
