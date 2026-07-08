# IFC Campus Blumenau - Projeto POO II - BCC 3° Fase
![IFC Campus Blumenau](https://cecom.ifc.edu.br/wp-content/uploads/sites/10/2022/10/Logo_IFC_extendida_Blumenau.png)

## Comparação de Estratégias Autônomas sobre a Captura de Bolas
Este projeto foi feito na linguagem **Python** utilizando as bibliotecas **pygame**, **pygame-ce** e **pygame zero**. Seu objetivo é testar 2 Estratégias: Uma no qual foca em 'capturar' a bolinha mais perto da plataforma IA, e outra que o objetivo é ficar no lado em que mais tem bolinhas e ai tentar capturar a mais perto.

Esse teste pode se comparar á um *Benchmarking*, pois ele faz exatamente isso, ele simula essas 2 estratégias, e após as 2 acabarem, mostra o resultado de ambas com quantas bolinhas capturou e perdeu no total, e a estratégia ganhadora.

A Simulação inicia com 100 bolinhas sendo geradas a cada 1,5 segundos, cada uma tem física e pode se colidir ou colidir com os obstáculos pelo caminho, se a plataforma errar uma bolinha, ela é considerada como uma bolinha 'perdida', as que a plataforma consegue capturar, é uma bolinha 'capturada'.

Como isto é uma *Simulação*, sendo seu objetivo principal logo testar tais métodos e suas eficiências, esse código **não:** Garante os mesmos resultados, Possui interface para ser jogável, ou Foca em elementos visuais/design avançado.

###### A Versão exata que eu rodei o programa só para referência: ' pygame-ce 2.5.7 (SDL 2.32.10, Python 3.14.5) '

## Instruções em como executar o programa:
Como o programa foi feito utilizando bibliotecas, elas devem ser baixadas, sendo elas **pygame, pygame-ce e pygame zero**. Abaixo há os comandos no qual terá que se usar no Terminal para baixar todos os 3:

1. **Pygame:** ```pip install pygame``` (a versão do pygame normal quando eu fui fazer o jogo não funcionava, então se não funcionar, instale a Community Edition de pygame abaixo.)
2. **Pygame-ce:** ```pip install pygame-ce```
3. **Pygame Zero:** ```pip install numpy pyfxr``` ( <-- *dependências*), ```pip install pgzero``` (adicione *--no-deps* antes de *pgzero* caso não queira forçar a instalação do pygame antigo, permitindo assim que se o pygame normal não funcionar, que rode por cima do pygame-ce sem reinstalar algo.)

Após isso, para baixar o programa, baixe-o neste repositório ou dê **git pull** dele para alguma pasta sua.

![Imagem de como baixar no github ou dando pull.](https://helpdeskgeek.com/wp-content/pictures/2021/06/11CodeButtonDownloadZip.png)

Para Rodar o programa, você precisa abrir ele em um editor de código como VSCode ou até mesmo no Terminal e rodar a função *main.py* , Agora algo para ficar atento é, se o programa der **ERRO** ao rodar, é por que você não iniciou ele pela pasta que contém tudo, então se certifique que no Terminal mostre esse diretório: ```X:..\POO_II\ProjetoP2```

### - Leonardo Hoffmann