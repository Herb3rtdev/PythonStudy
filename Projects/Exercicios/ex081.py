resp = ''
numeros = []
while resp in 'Ss':
    numero = int(input('Digite um numero: '))
    numeros.append(numero)
    resp = str(input('Voce quer continuar? [S/N]').strip())
    if resp in 'Nn':
        break
print('---'*15)
if 5 in numeros:
    print(f'O valor 5 foi digitado na lista e a posicao é {numeros.index(5)}')
else:
    print('O valor 5 não foi digitado na lista.')
print(f'Os numeros na lista são:{numeros}')
print(f'O total de numeros digitados foi {len(numeros)}')
numeros.sort(reverse=True)
print(f'Os numeros em ordem decrescente é {numeros}')

      