from config import WIDTH

class EstrategiaProxima:
    def __init__(self):
        self.alvo = None

    def escolher_alvo(self, bolas, jogador):
        if self.alvo not in bolas:
            self.alvo = None

        if self.alvo == None:
            menor = 999999

            for bola in bolas:
                distancia = abs(bola.x - (jogador.x + jogador.largura/2))

                if distancia < menor:
                    menor = distancia
                    self.alvo = bola

        if self.alvo == None:
            return WIDTH // 2
        
        # Antes era só return self.alvo.x, mudei para esse diferente pois ele tenta ir um pouco mais a frente da trajetória da bolinha pra ficar mais cleann
        return self.alvo.x + self.alvo.vx * 8