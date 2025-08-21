soma_maior = 0
soma_menor = 0
from datetime import date
atual = date.today().year
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}.o pessoa?'.format(c)))
    idade = atual - nasc
    if idade >= 21:
        soma_maior += 1
    else:
        soma_menor += 1
print('A quantidade de pessoas acima da maioridade é {}'.format(soma_maior))
print('A quantidade de pessoas abaixo da maioridade é {}'.format(soma_menor))

