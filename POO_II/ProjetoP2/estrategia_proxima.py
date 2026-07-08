from config import WIDTH

class EstrategiaProxima:

    def escolher_alvo(self, bolas, jogador):
        if len(bolas) == 0:
            return WIDTH // 2

        melhor_bola = None
        melhor_score = 999999999

        centro = jogador.x + jogador.largura / 2

        for bola in bolas:
            # Ignora bolas subindo
            if bola.vy <= 0:
                continue

            tempo = (jogador.y - bola.y) / bola.vy

            if tempo < 0:
                continue

            distancia = abs(bola.x - centro)

            score = distancia + tempo * 40

            if score < melhor_score:
                melhor_score = score
                melhor_bola = bola

        if melhor_bola == None:
            return WIDTH // 2
        
        # mudei para esse diferente pois ele tenta ir um pouco mais a frente da trajetória da bolinha pra ficar mais cleann
        return melhor_bola.x + melhor_bola.vx * 6