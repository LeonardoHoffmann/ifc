from config import *
from pygame import Rect
from pygame import surface

TAMANHO = 20 # 20x20

class Bloco:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.largura = TAMANHO
        self.altura = TAMANHO

        self.color = (211, 211, 211)

        self.visible = True

        # hitbox
        self.rect = Rect(self.x, self.y, self.largura, self.altura)

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        if self.visible:
            screen.draw.filled_rect(self.rect, self.color)