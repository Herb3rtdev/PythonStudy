
op = ''
quantidade = soma = maior = menor =0
while op != 'N':
    n = int(input('Digite um numero: '))
    op = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    soma += n
    quantidade += 1
    if quantidade == 1:
       menor = maior = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
media = soma / quantidade
print('Voce digitou {} numeros e a media foi {}'.format(quantidade,media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))