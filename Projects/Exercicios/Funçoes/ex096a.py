def area(l,c):
    a = l * c
    print(f'A área do seu terreno de {l:.2f} x {c:.2f} é {a}m2')



print('Controle de Terrenos')
print('-='*10)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura,comprimento)