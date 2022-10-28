from scripts.button import Button


class Textbox:
    def __init__(self, img, pos, surface):

        self.list = []
        self.button = Button(pos[0], pos[1], img, surface)
        self.list.append(self.button)

    def draw(self):

        for text in self.list:
            if text.draw():
                None

    def remove(self):

        for text in self.list:
            self.list.remove(text)
