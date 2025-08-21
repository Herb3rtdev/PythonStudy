from random import randint
from time import sleep
numero = randint(0,5)
print('-=-'*8)
print('JOGO DA ADIVINHAÇÃO')
print('-=-'*8)
n = input('Escolha um numero de 0 a 5:')
print('Analisando...')
sleep(3)
if n == numero:
    print('Muito bem! Voce acertou!')
else:
    print('...Voce errou!')
print('O numero sorteado foi {} e o que voce escolheu foi {}'.format(numero,n))
