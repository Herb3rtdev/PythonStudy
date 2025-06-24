lista_numeros = []
numeros_pares = []
numeros_impares = []
while True:
    lista_numeros.append(int(input('Digite um numero: ')))
    resp = str(input('Voce quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=-'*20)
print(f'A lista comppleta é:{lista_numeros}')
for contador in lista_numeros:
    if contador % 2 == 0:
        numeros_pares.append(contador)
    else:
        numeros_impares.append(contador)
print(f'A lista de numeros pares:{numeros_pares}')
print(f'A lista de numeros impares:{numeros_impares}')