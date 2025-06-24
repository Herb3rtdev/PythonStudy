numeros = []
while True:
    numero = int(input('Digite um valor: '))
    if numero not in numeros:
        numeros.append(numero)
        print(f'Valor adicionado com sucesso...')
    else:
        print('Resposta inválida.')
    resp = str(input('Voce quer continuar? [S/N]'))
    if resp in 'nN':
        break 
    while not resp in 'SsnN':
        print('Resposta inválida.')
        resp = str(input('Voce quer continuar? [S/N]'))
    if resp in 'Nn':
        break
numeros.sort()
print(numeros)