from random import randint
from time import sleep
item = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print('Suas opções:')
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
escolha = int(input('Qual é a sua jogada?'))
print('-=-'*10)
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
print('Computador escolheu {}'.format(item[pc].upper()))
print('Jogador escolheu {}'.format(item[escolha].upper()))
print('-=-'*10)
if pc == 0:#PEDRA
    if escolha == 0:#PEDRA
        print('EMPATE!')
    elif escolha == 1:#PAPEL
        print('o JOGADOR GANHOU')
    elif escolha == 2:#TESOURA
        print('A MAQUINA ganhou')
elif pc == 1:
    if escolha == 0:
        print('A MAQUINA GANHOU')
    elif escolha == 1:
        print('EMPATE!')
    elif escolha == 2:
        print('O JOGADOR GANHOU')
elif pc == 2:
    if escolha == 0:
        print('o JOGADOR GANHOU')
    elif escolha == 1:
        print('a MAQUINA GANHOU')
    elif escolha == 2:
        print('EMPATE')
