def matriz():
    m = [[0, 0, 0,],[0, 0, 0],[0, 0, 0]]
    for x in range(0,3):
        for y in range(0,3):
            m[x][y] = int(input(f'Digite um valor para a matriz [{x}, {y}]:'))
    print('-=-'*15)
    for x in range(0,3):
        for y in range(0,3):
            print(f'[{m[x][y]:^5}]',end='')
        print()
    print('-=-'*15)
    return m

def soma(matriz):
    soma_par = 0
    for linha in matriz:#vai pecorrer cada linha da matriz.Ex([0, 0, 0], que são 3)
        for valor in linha:#vai pecorrer os numeros dentro de cada linha da matriz
            if valor % 2 == 0:
                soma_par += valor
    print(f'A Soma dos valores pares é {soma_par}')


def soma_terceira_coluna(matriz):
    soma_terceira = 0
    for linha in matriz:
        soma_terceira += linha[2]
    print(f'A soma dos valores da terceira coluna é {soma_terceira}')


def maior_valor_segunda_linha(matriz):
    maior = matriz[1][0]
    for numeros in matriz[1]:
        if numeros > maior:
            maior = numeros
    print(f'O maior valor da segunda linha {maior}')
    

        

matrizes = matriz()
soma(matrizes)
soma_terceira_coluna(matrizes)
maior_valor_segunda_linha(matrizes)

