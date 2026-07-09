import random
import math
import pygame
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

pygame.mixer.init()
som_boing = pygame.mixer.Sound("SFX/Boing.wav")
som_victory = pygame.mixer.Sound("SFX/victory.wav")
som_platform = pygame.mixer.Sound("SFX/electronicpingshort.wav")

CENTRO = 600
nome_estrategia = "Estratégia Próxima"
estado = "SIMULACAO"
simulacao_atual = 1

TOTAL_BOLAS = 100
bolas_spawnadas = 0
tempo_spawn = 0
INTERVALO_SPAWN = 90 # 1.5 segundos a 60 FPS
tempo_resultado = 0

resultado_atual = ""
resultado_proxima = None
resultado_quantia = None
resultado_final = False

esquerda_count = 0
direita_count = 0

capturadas = 0
perdidas = 0
bolas = []
blocos = []

jogador = Jogador(WIDTH // 2 - 60,HEIGHT - 30)
ia = EstrategiaProxima()

# Mapa
mapa1(blocos)

# Transparencia blocos para mostrar a imagem
for bloco in blocos:
    bloco.visible = False

# Sombra atras de telas finais
def mostrar_imagem_resultado(valor):
    global resultado_alpha
    resultado_alpha = valor
    resultado_image.set_alpha(resultado_alpha)

# Funções da Simulação
def reset_simulacao():
    global bolas
    global capturadas, perdidas
    global bolas_spawnadas
    global tempo_spawn
    global ia
    global nome_estrategia
    global estado
    global simulacao_atual

    bolas.clear()

    capturadas = 0
    perdidas = 0

    bolas_spawnadas = 0
    tempo_spawn = 0
    mostrar_imagem_resultado(0)

    jogador.x = WIDTH // 2 - jogador.largura / 2
    jogador.rect.x = jogador.x

    if simulacao_atual == 1:
        ia = EstrategiaProxima()
        nome_estrategia = "Estratégia Próxima"

    elif simulacao_atual == 2:
        ia = EstrategiaQuantia()
        nome_estrategia = "Estratégia Quantia"

    estado = "SIMULACAO"

def terminar_simulacao():
    global capturadas, perdidas
    global estado
    global resultado_atual
    global resultado_proxima
    global resultado_quantia
    global tempo_resultado
    global simulacao_atual

    if simulacao_atual == 1:
        resultado_proxima = (capturadas,perdidas)
        resultado_atual = "Estratégia Próxima"
        simulacao_atual = 2

    elif simulacao_atual == 2:
        resultado_quantia = (capturadas,perdidas)
        resultado_atual = "Estratégia Quantia"
        estado = "FINAL"
        som_victory.play()
        return

    estado = "RESULTADO"
    tempo_resultado = 0
    mostrar_imagem_resultado(180)

def desenhar_resultado():
    if resultado_atual == "Estratégia Próxima":
        resultado = resultado_proxima
    else:
        resultado = resultado_quantia

    screen.draw.text(resultado_atual + " terminou.",center=(WIDTH//2, HEIGHT//2 - 80),fontsize=50,color="white")
    screen.draw.text("Capturadas: " + str(resultado[0]),center=(WIDTH//2, HEIGHT//2),fontsize=40,color="green")
    screen.draw.text("Perdidas: " + str(resultado[1]),center=(WIDTH//2, HEIGHT//2 + 60),fontsize=40,color="red")

def desenhar_final():
    p = resultado_proxima[0]
    q = resultado_quantia[0]

    if p > q:
        vencedor = "Estratégia Próxima"
    elif q > p:
        vencedor = "Estratégia Quantia"
    else:
        vencedor = "Empate"

    screen.draw.text("Benchmark Finalizado",center=(WIDTH//2,130),fontsize=60,color="white")
    screen.draw.text("Estratégia Próxima",center=(WIDTH//2,330),fontsize=40,color="white")
    screen.draw.text("Capturadas: " + str(resultado_proxima[0]),center=(WIDTH//2,380),fontsize=35,color="green")
    screen.draw.text("Perdidas: " + str(resultado_proxima[1]),center=(WIDTH//2,430),fontsize=35,color="red")
    screen.draw.text("========----------------------------------------------========",center=(WIDTH//2,480),fontsize=30,color="white")
    
    screen.draw.text("Estratégia Quantia",center=(WIDTH//2,550),fontsize=40,color="white")
    screen.draw.text("Capturadas: " + str(resultado_quantia[0]),center=(WIDTH//2,600),fontsize=35,color="green")
    screen.draw.text("Perdidas: " + str(resultado_quantia[1]),center=(WIDTH//2,650),fontsize=35,color="red")
    screen.draw.text("Vencedor: " + vencedor,center=(WIDTH//2,830),fontsize=50,color="yellow")

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
                som_boing.play()

                sobreposicao = distancia_minima - distancia

                if distancia != 0:
                    nx = dx / distancia
                    ny = dy / distancia

                    bola_a.x -= nx * sobreposicao / 2
                    bola_a.y -= ny * sobreposicao / 2

                    bola_b.x += nx * sobreposicao / 2
                    bola_b.y += ny * sobreposicao / 2

bg_image = image.load("Texturas/basedV2.jpg").convert()
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

resultado_image = image.load("Texturas/backgroundevil.png").convert_alpha()
resultado_image = transform.scale(resultado_image, (WIDTH, HEIGHT))
resultado_alpha = 0
resultado_image.set_alpha(resultado_alpha)

def update():
    global capturadas, perdidas
    global esquerda_count
    global direita_count
    global tempo_spawn
    global bolas_spawnadas
    global tempo_resultado
    global estado

    if estado == "RESULTADO":
        tempo_resultado += 1
        if tempo_resultado >= 180: # 3 segundos
            reset_simulacao()
        return

    if estado == "FINAL":
        return

    # SIMULACAO
    esquerda_count = 0
    direita_count = 0

    # Spawn automatico
    if bolas_spawnadas < TOTAL_BOLAS:
        tempo_spawn += 1

        if tempo_spawn >= INTERVALO_SPAWN:
            bolas.append(Bola(random.randint(50, WIDTH - 50),0))
            bolas_spawnadas += 1
            tempo_spawn = 0

    # Física
    for bola in bolas:
        bola.update()
        bola.colidir_blocos(blocos)
    colisoes_bolas()

    # Contagem lados
    for bola in bolas:
        if bola.x < CENTRO:
            esquerda_count += 1
        else:
            direita_count += 1

    # Escolha IA
    if simulacao_atual == 1:
        alvo = ia.escolher_alvo(bolas,jogador)
    else:
        alvo = ia.escolher_alvo(bolas, jogador, esquerda_count, direita_count)

    jogador.mover_para(alvo)
    jogador.update()

    # Captura / Perda
    for bola in bolas[:]:
        if jogador.rect.colliderect(bola.rect):
            bolas.remove(bola)
            capturadas += 1
            
            som_platform.play()

        elif bola.y - bola.raio > HEIGHT:
            bolas.remove(bola)
            perdidas += 1

    # Acabou?
    if bolas_spawnadas == TOTAL_BOLAS and len(bolas) == 0:
        terminar_simulacao()

def draw():
    screen.clear()
    screen.blit(bg_image, (0, 0))
    if resultado_alpha > 0:
        screen.blit(resultado_image,(0,0))

    screen.blit(center_1, center_rect1)
    screen.blit(center_2, center_rect2)
    screen.blit(center_3, center_rect3)

    for bloco in blocos:
        bloco.draw(screen)
    
    jogador.draw(screen)

    for bola in bolas:
        bola.draw(screen)
    
    if estado == "RESULTADO":
        desenhar_resultado()
    elif estado == "FINAL":
        mostrar_imagem_resultado(180)
        desenhar_final()
    else:
        screen.draw.text("Simulação sobre a Comparação de Estratégias Autônomas sobre a Captura de Bolas",(20, 10),color="white")
        screen.draw.text("Capturadas: " + str(capturadas),(20,40),color="green")
        screen.draw.text("Perdidas: " + str(perdidas),(20, 70),color="red")

        screen.draw.text(f"Esquerda: {esquerda_count}", (WIDTH - 220, 20), color="white")
        screen.draw.text(f"Direita: {direita_count}", (WIDTH - 90, 20), color="white")

        screen.draw.text(f"{nome_estrategia}",(WIDTH - 220, 55),color="cyan")
        screen.draw.text(f"Simulação: {simulacao_atual} / 2",(WIDTH - 220, 80),color="white")

# Desativado para a Simulação, da pra ativar se quiser "debugar"..
# def on_mouse_down(pos, button):
#     if button == mouse.LEFT:
#         bolas.append(Bola(pos[0], pos[1]))

pgzrun.go()