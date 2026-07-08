from config import WIDTH

class EstrategiaProxima:

    def escolher_alvo(self, bolas, jogador):
        if len(bolas) == 0:
            return WIDTH / 2

        menor_distancia = 999999

        alvo = jogador.x
        centro = jogador.x + jogador.largura / 2

        for bola in bolas:
            distancia = abs(bola.x - centro)

            if distancia < menor_distancia:
                menor_distancia = distancia
                alvo = bola.x

        return alvo