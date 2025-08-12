def area(l,c):
    area = l * c
    print(f'A área de um terreno {l}x{c} é de {area} m2.')


def tamanho_linha(txt):
    print(txt)
    print('-'*len(txt))


#programa principal
tamanho_linha('Controle de Terrenos')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura,comprimento)