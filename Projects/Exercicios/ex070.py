total = quantidade = preco_mais1000=0
while True:
    produto = str(input('Qual o produto?'))
    preco = int(input('Qual o preço do produto? R$'))
    quantidade += 1
    if quantidade == 1:
        menor = preco
        menorP = produto
    else:
        if preco < menor:
            menor = preco
            menorP = produto
    total += preco
    if preco > 1000:
        preco_mais1000 += 1
    resp = str(input('Voce quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'O valor dos produtos é R${total}')
print(f'A quantidade de produtos que custam mais que R$1000 é {preco_mais1000}')
print(f'O produto mais barato é {menorP} no valor de R${menor}.')
print('Programa acabou!')