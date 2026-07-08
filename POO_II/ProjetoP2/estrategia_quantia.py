from config import WIDTH

class EstrategiaQuantia:
    def escolher_alvo(self, bolas, jogador, esquerda_count, direita_count):
        if len(bolas) == 0:
            return WIDTH // 2

        centro = WIDTH // 2

        # Decide qual lado será usado
        if esquerda_count > direita_count:
            lado = "esquerda"
        elif direita_count > esquerda_count:
            lado = "direita"
        else:
            return WIDTH // 2

        menor_distancia = 999999
        alvo = None

        centro_jogador = jogador.x + jogador.largura / 2

        # Procura apenas bolas do lado escolhido
        for bola in bolas:
            if lado == "esquerda":
                if bola.x >= centro:
                    continue
            else:
                if bola.x < centro:
                    continue

            distancia = abs(bola.x - centro_jogador)

            if distancia < menor_distancia:
                menor_distancia = distancia
                alvo = bola

        if alvo == None:
            return WIDTH // 2

        # Mesma coisa feita na outra estratégia.
        return alvo.x + alvo.vx * 8