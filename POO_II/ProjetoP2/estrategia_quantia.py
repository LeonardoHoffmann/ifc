from config import WIDTH

class EstrategiaQuantia:
    def __init__(self):
        # feito para agir como um "lembrete" do lado que estava por último pra não ficar travado no meio como acontecia antes.
        self.lado = "esquerda"

    def escolher_alvo(self, bolas, jogador, esquerda_count, direita_count):
        if len(bolas) == 0:
            return WIDTH // 2
        
        # decide qual lado será usado
        if esquerda_count > direita_count:
            self.lado = "esquerda"
        elif direita_count > esquerda_count:
            self.lado = "direita"

        melhor_bola = None
        melhor_score = 999999999

        centro = WIDTH // 2
        centro_jogador = jogador.x + jogador.largura / 2

        for bola in bolas:
            if self.lado == "esquerda":
                if bola.x >= centro:
                    continue
            else:
                if bola.x < centro:
                    continue

            if bola.vy <= 0:
                continue

            tempo = (jogador.y - bola.y) / bola.vy

            if tempo < 0:
                continue

            distancia = abs(bola.x - centro_jogador)

            score = distancia + tempo * 40

            if score < melhor_score:
                melhor_score = score
                melhor_bola = bola

        if melhor_bola == None:
            return WIDTH // 2

        return melhor_bola.x + melhor_bola.vx * 6