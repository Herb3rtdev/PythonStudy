from random import randint


#Irá fazer o sorteio de numeros 
def sorteando(lista):   
    for cont in range(0,5):
        sorteados = randint(0,10)
        lista.append(sorteados)
        print(sorteados,end=' ')
    print('Pronto!')


#Irá somar os numeros pares
def somapar(lista):
    spar = 0
    for valor in lista:
        if valor % 2 == 0:
            spar += valor
    print(spar)


valores = []
print(f'Os valores sorteados foram: ',end ='')
sorteando(valores)
print('A soma dos numeros pares é: ',end='')
somapar(valores)