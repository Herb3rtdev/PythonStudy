from random import randint
vitoriaImpar = vitoriaPar = 0
print('-=-' * 10)
print('ÍMPAR OU PAR')
print('-=-'*10)
while True:
    computador = randint(0, 10)
    n = int(input('Escolha um numero:'))
    escolha = str(input('PAR ou IMPAR? [P/I]')).strip().upper()[0]
    print('-' * 45)
    soma = computador + n
    print(f'Jogador escolheu {n} e a máquina {computador}.Total deu {soma}')
    print('-'* 45)
    if escolha == 'P':
        if soma % 2 == 0:
            print('Jogador VENCEU!Deu PAR\nVamos jogar de novo!')
            vitoriaPar += 1
        else:
            print('Jogador PERDEU!Deu IMPAR')
            break
    if escolha == 'I':
        if soma % 2 == 1:
            print('Jogador VENCEU! Deu IMPAR!\nVamos jogar de novo!')
            vitoriaImpar += 1
        else:
            print('Jogador PERDEU!Deu PAR')
            break
print('-=-'*10)
vitorialTotal = vitoriaPar + vitoriaImpar
print(f'GAME OVER! O jogador venceu {vitorialTotal} vezes')