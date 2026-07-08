from config import WIDTH

class EstrategiaProxima:

    def escolher_alvo(self, bolas, jogador):
        if len(bolas) == 0:
            return WIDTH // 2

        menor = 999999
        alvo = None

        for bola in bolas:
            distancia = abs(bola.x - (jogador.x + jogador.largura/2))

            if distancia < menor:
                menor = distancia
                alvo = bola
        
        # O uso de self era o que fazia a plataforma seguir/lock on uma bolinha, então o removi pra seguir um workflow parecido com o da outra estratégia, 
        # mudei para esse diferente pois ele tenta ir um pouco mais a frente da trajetória da bolinha pra ficar mais cleann
        return alvo.x + alvo.vx * 8