maior = 0
menor = 0
print('LEITOR DE KG')
print('='*20)
for c in range(1,6):
    peso = float(input('Digite o peso da {}.o pessoa em KG: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}KG'.format(maior))
print('O menor peso lido foi de {}KG'.format(menor))