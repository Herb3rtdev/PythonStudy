from random import randint
def soma_par(numeros):
    soma_numeros_pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma_numeros_pares += numero
    return soma_numeros_pares



#Program  principal
numeros = []
print('Sorteando 5 valores da lista:',end=' ')
for contador in range(0,5):
    numero = randint(0,10)
    numeros.append(numero)
    print(numero,end=' ')
print('PRONTO')
pares = soma_par(numeros)
print(f'Somandon os valores pares de {numeros}, temos {pares}')