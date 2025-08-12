def numero():
    n = (int(input('Digite um numero: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite mais um numero: ')),
        int(input('Digite o ultimo numero: ')),)
    print(f'Voce digitou os valores: {n}')    
    print(f'O numero 9 apareceu {n.count(9)} vezes')
    print(f'O numero 3 apreceu na {n.index(3)+1}.o posição')
    return n

def par(valores):
    soma_par = 0
    for valor in valores:
        if valor % 2 == 0:
            soma_par += 1
    print(f'Os valores pares digitados foaram: {soma_par}')

valores = numero()
par(valores)