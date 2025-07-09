numeros = []
maior = menor = 0
posicao_maior = posicao_menor = 0
for posicao in range(0,5):
    numero = int(input(f'Digite um numero na posicao {posicao}: '))
    numeros.append(numero)
    if posicao == 0:
         menor = maior = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print('-=-'*15)
print(f'Voce digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posicoes ',end='')
for pos, valor in enumerate(numeros):
    if valor == maior:
        print(pos,end='...')
print(f'\nO menor valor digitado foi {menor} na posicoes ',end='')
for pos, valor in enumerate(numeros):
    if valor == menor:
        print(pos,end='...')
