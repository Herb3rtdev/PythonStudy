from random import randint
palpite = 0
numero = randint(0,10)
print('-=-'*10)
print('JOGO DA ADVINHAÇÃO')
print('-=-'*10)
print('Escolha um numero de 0 a 10')
n = int(input('Tente advinhar um número:'))
while not n == numero:
    if n > numero:
        print('MENOS...')
    else:
        print('MAIS...')
    n = int(input('Voce ERROU!Escolha outra vez:'))
    palpite += 1
print('Muito bem voce ACERTOU!. A máquina escolheu {} e o jogador escolheu {}'.format(numero, n))
print('Foram necessarias {} tentativas para o jogador acertar.'.format(palpite+1))