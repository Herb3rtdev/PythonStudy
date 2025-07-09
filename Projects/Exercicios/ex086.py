matriz = [[0,0,0],[0,0,0],[0,0,0]]
for x in range(0,3):
    for y in range(0,3):
        matriz[x][y]=int(input(f'Digite um valor para a posicao [{x}, {y}]:'))
print('-=-'*15)
for x in range(0,3):
    for y in range(0,3):
        print(f'[{matriz[x][y]:^5}]',end='')
    print()