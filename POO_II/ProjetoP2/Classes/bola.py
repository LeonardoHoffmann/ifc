import random
from config import *
from Classes.bloco import Bloco
from pygame import Rect

class Bola:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.raio = 20

        self.vx = random.uniform(-4, 4)
        self.vy = random.uniform(-2, 2)

        self.color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )

        self.color_borda = (88, 88, 88)

        self.rect = Rect(self.x - self.raio,self.y - self.raio,self.raio * 2,self.raio * 2) # Jeito de ter Hitbox
    
    def colidir_blocos(self, blocos):
        for bloco in blocos:

            perto_x = max(bloco.rect.x, min(self.x, bloco.rect.x + bloco.rect.width))
            perto_y = max(bloco.rect.y, min(self.y, bloco.rect.y + bloco.rect.height))

            dx = self.x - perto_x
            dy = self.y - perto_y

            distancia_quadrado = dx * dx + dy * dy

            if distancia_quadrado < self.raio * self.raio:

                distancia = max(0.0001, distancia_quadrado ** 0.5)

                nx = dx / distancia
                ny = dy / distancia

                sobreposicao = self.raio - distancia

                self.x += nx * sobreposicao
                self.y += ny * sobreposicao

                dot = self.vx * nx + self.vy * ny

                self.vx -= 2 * dot * nx
                self.vy -= 2 * dot * ny

    def update(self):
        # Gravidade
        self.vy += GRAVITY

        # Movimento
        self.x += self.vx
        self.y += self.vy

        # Colisão com o chão (removido para elas sumirem pra não bugar a AI da plataforma)
        
        # Colisão com o céu talvez (Decidido nah, pois não é necessário já que tem paredes..)

        # Parede esquerda
        if self.x - self.raio <= 0:
            self.x = self.raio
            self.vx *= -BOUNCE

        # Parede direita
        if self.x + self.raio >= WIDTH:
            self.x = WIDTH - self.raio
            self.vx *= -BOUNCE
        
        # Hitbox update
        self.rect.x = self.x - self.raio
        self.rect.y = self.y - self.raio

    def draw(self, screen):
        screen.draw.filled_circle((self.x, self.y),self.raio,self.color)