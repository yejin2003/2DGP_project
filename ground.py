from pico2d import load_image


class Ground:
    def __init__(self):
        self.image = load_image('BG_Forest_Main01.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass
