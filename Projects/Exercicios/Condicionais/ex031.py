d = int(input('Qual a distancia da viagem km:'))
if d <= 200:
    print('O preço da sua viagem foi de R${}.\nSua distancia foi {} km'.format(d * 0.5, d))
else:
    print('O preço da sua viagem foi de R${}.\nSua distancia foi {} km'.format(d * 0.45, d))
print('Muito obrigado por nos escolher!')