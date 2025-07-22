from random import randint
from time import sleep


def sorteio(lista):
    for c in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(n,end= ' ', flush = True)
        sleep(0.3)
    print('Pronto!')


def somapar(lista):
    spar = 0
    for valor in lista:
        if valor % 2 == 0:
            spar += valor
    print(spar)





numeros = []
print(f'Sorteando 5 valores da lista: ',end='')
sorteio(numeros)
print(f'Somando os valores pares de {numeros}, temos',end=' ')
somapar(numeros)