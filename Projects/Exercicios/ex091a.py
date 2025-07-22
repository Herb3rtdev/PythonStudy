from random import randint
from time import sleep
from operator import itemgetter
jogadores = {
    'Jogador 1': randint(1,6),
    'Jogador 2': randint(1,6),
    'Jogador 3': randint(1,6),
    'Jogador 4': randint(1,6)
}
for k,v in jogadores.items():
    print(f'O {k} tirou {v}')
ranking = ()
ranking = sorted(jogadores.items(),key = itemgetter(1), reverse = True)
print('Ranking dos jogadores:')
for pos,valor in enumerate(ranking):
    print(f'{pos+1}.o lugar: {valor[0]} com {valor[1]}')
