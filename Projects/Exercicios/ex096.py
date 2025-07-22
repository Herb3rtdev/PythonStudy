def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a} m2 ')


print('Controle de Terrenos')
print('--------------------')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)