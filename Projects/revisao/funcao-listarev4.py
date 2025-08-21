def matriz():
    """Pede para o usuário digitar seis númeos e monta uma matriz 3x3
    x = linhas
    y = colunas
    """
    m = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    for x in range(0,3):
        for y in range(0,3):
            m[x][y] = int(input(f'Digite um numero na matriz [{x}, {y}]:'))
    for x in range(0,3):
        for y in range(0,3):
            print(f'[{m[x][y]:^5}]',end='')
        print()
   

#Programa principal
matriz()