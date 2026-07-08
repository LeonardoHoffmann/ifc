from config import *
from pygame import Rect

ALTURA = 15
LARGURA = 100

class Jogador:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.velocidade = 16
        self.alvo_x = self.x

        self.largura = LARGURA
        self.altura = ALTURA

        self.color = (0, 0, 0)

        # hitbox
        self.rect = Rect(self.x, self.y, self.largura, self.altura)

    def mover_para(self, x):
        self.alvo_x = x

    def update(self):

        centro = self.x + self.largura / 2

        if centro < self.alvo_x:
            self.x += self.velocidade

        elif centro > self.alvo_x:
            self.x -= self.velocidade

        if self.x < 0:
            self.x = 0

        if self.x + self.largura > WIDTH:
            self.x = WIDTH - self.largura

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.draw.filled_rect(self.rect, self.color)