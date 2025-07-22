from random import randint
from time import sleep
jogadores = {}
for c in range(1,5):
    sorteado = randint(1,6)
    jogadores[f'Jogador {c}'] = sorteado
    print(f'O jogador {c} tirou {sorteado}')
print('Ranking dos jogadores')
ranking = ()
ranking = sorted(jogadores.items(), key = lambda item: item[1], reverse =True)
for pos, valor in enumerate(ranking):
    print(f'{pos+1}.o lugar: {valor[0]} com {valor[1]}')