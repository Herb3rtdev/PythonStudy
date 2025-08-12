def sorteio():
    from random import randint
    numero_sorteado = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
    print('Os valores sorteados foram: ',end='')
    for c in range(0,len(numero_sorteado)):
        print(numero_sorteado[c],end=' ')
    return numero_sorteado


def maior_menor(numeros):
    maior = numeros[0]
    menor = numeros[0]
    for c in range(1,len(numeros)):
            if numeros[c] > maior:
                maior = numeros[c]
            if numeros[c] < menor:
                menor = numeros[c]
    print(f'\nO maior valor sorteado foi: {maior}')
    print(f'O menor valor sorteado foi: {menor}')


numeros = sorteio()
maior_menor(numeros)