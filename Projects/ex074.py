from random import randint
print('Os valores sorteados foram: ',end='')
numero_sorteado = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
for n in numero_sorteado:
    print(f'{n} ',end=' ')
print(f'\nO maior valor sorteado foi {max(numero_sorteado)}')
print(f'O menor valor sorteado foi {min(numero_sorteado)}')