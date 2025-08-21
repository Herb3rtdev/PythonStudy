matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_par = soma_terceira = maior= 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]=int(input(f'Digite um valor para a posicao [{linha}, {coluna}]:'))
print('-=-'*15)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
    print()
print('-=-'*15)
print(f'A soma dos valores pare é {soma_par}')
for linha in range(0,3):
    if matriz[linha][2]:
        soma_terceira += matriz[linha][2]
print(f'A somados valores da terceira coluna é {soma_terceira}')
for coluna in range(0,3):
    if coluna == 0:
        maior = matriz[2][coluna]
    else:
        if matriz[2][coluna] > maior:
            maior = matriz[2][coluna]
print(f'O maior valor da segunda linha {maior}')

        
