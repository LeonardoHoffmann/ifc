import random
import math
from config import *
from Classes.bola import Bola
from Classes.bloco import Bloco
from Classes.mapa import mapa1
from Classes.jogador import Jogador
from pygame import mouse
from pygame import image
from pygame import transform
from estrategia_proxima import EstrategiaProxima
from estrategia_quantia import EstrategiaQuantia
import pgzrun

CENTRO = 600

esquerda_count = 0
direita_count = 0

capturadas = 0
perdidas = 0
bolas = []
blocos = []

# Spawna as bolas
for i in range(5):
    bolas.append(
        Bola(
            random.randint(50, WIDTH - 50),
            random.randint(0, 100)
        )
    )

jogador = Jogador(
    WIDTH // 2 - 60,
    HEIGHT - 30
)

# ia1 = EstrategiaProxima()
ia2 = EstrategiaQuantia()

# Mapa
mapa1(blocos)

# Transparencia blocos para mostrar a imagem
for bloco in blocos:
    bloco.visible = False

def colisoes_bolas():
    for i in range(len(bolas)):
        for j in range(i + 1, len(bolas)):

            bola_a = bolas[i]
            bola_b = bolas[j]

            dx = bola_b.x - bola_a.x
            dy = bola_b.y - bola_a.y

            distancia = math.sqrt(dx * dx + dy * dy)

            distancia_minima = bola_a.raio + bola_b.raio

            if distancia < distancia_minima:

                bola_a.vx, bola_b.vx = bola_b.vx, bola_a.vx
                bola_a.vy, bola_b.vy = bola_b.vy, bola_a.vy

                sobreposicao = distancia_minima - distancia

                if distancia != 0:
                    nx = dx / distancia
                    ny = dy / distancia

                    bola_a.x -= nx * sobreposicao / 2
                    bola_a.y -= ny * sobreposicao / 2

                    bola_b.x += nx * sobreposicao / 2
                    bola_b.y += ny * sobreposicao / 2

bg_image = image.load("Texturas/based.png").convert()
bg_image = transform.scale(bg_image, (WIDTH, HEIGHT))

center_1 = image.load("Texturas/losangulo.png").convert_alpha()
center_rect1 = center_1.get_rect()
center_rect1.center = (610, 470)

center_2 = image.load("Texturas/losangulo.png").convert_alpha()
center_rect2 = center_2.get_rect()
center_rect2.center = (0, 290)

center_3 = image.load("Texturas/losangulo.png").convert_alpha()
center_rect3 = center_3.get_rect()
center_rect3.center = (1200, 290)

def update():
    global capturadas, perdidas
    global esquerda_count, direita_count

    esquerda_count = 0
    direita_count = 0

    # Atualiza todas as bolas
    for bola in bolas:
        bola.update()
        bola.colidir_blocos(blocos)

    colisoes_bolas()

    # Conta quantas bolas existem em cada lado
    for bola in bolas:
        if bola.x < CENTRO:
            esquerda_count += 1
        else:
            direita_count += 1

    # IA escolhe para onde mover
    alvo = ia2.escolher_alvo(bolas, jogador, esquerda_count, direita_count)

    jogador.mover_para(alvo)
    jogador.update()

    # Verifica bolas capturadas ou perdidas
    for bola in bolas[:]: # [:] feito para o for ler uma cópia sem ter mudanças para ai sim mudar na lista real

        if jogador.rect.colliderect(bola.rect):
            bolas.remove(bola)
            capturadas += 1
            continue

        if bola.y - bola.raio > HEIGHT:
            bolas.remove(bola)
            perdidas += 1

def draw():
    screen.clear()
    screen.blit(bg_image, (0, 0))

    screen.blit(center_1, center_rect1)
    screen.blit(center_2, center_rect2)
    screen.blit(center_3, center_rect3)

    for bloco in blocos:
        bloco.draw(screen)
    
    jogador.draw(screen)

    for bola in bolas:
        bola.draw(screen)

    screen.draw.text("Física de bolas teste 019",(20, 10),color="white")
    screen.draw.text("Capturadas: " + str(capturadas),(20,40),color="green")
    screen.draw.text("Perdidas: " + str(perdidas),(20, 70),color="red")

    screen.draw.text(f"Esquerda: {esquerda_count}", (WIDTH - 220, 20), color="white")
    screen.draw.text(f"Direita: {direita_count}", (WIDTH - 90, 20), color="white")

def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        bolas.append(Bola(pos[0], pos[1]))

pgzrun.go()

# Teste de recolhamento de bolinhas:
# Seria testado por 2 métodos, 1° jogador seria o que reageria vendo a bolinha mais perto e indo pra ela
# e o 2° jogador seria vendo aonde mais bolinhas vão cair/tem bolinhas
# Velocidade do jogador seria limitada, se bolinhas cair abaixo dele = null
# 100 bolinhas por run, provavelmente fazer separado, tipo primeiro 1° e depois o 2°
# contabilizar quantas bolinhas são pegas por jogador
# ter um timer pra cada também só para estatísticas
# Ter um cenário default para ambos experimentos de umas plataformas inclinadas
# Cada bolinha ter o mesmo tamanho para mais accurate resultados
# Posições que as bolinhas cair ser total random com for com um timer de 60-90-120 segundos (1-1.5-2 minuto) cada bolinha spawnando
# em um intervalo de 1-1.5s (T.B.D)