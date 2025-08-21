def total(n='', g=''):
    if n == '':
        n = '<desconhecido>'
    if g == '':
        g = 0
    return f'O jogador {n} fez {g} gol(s) no campeonato.'


print('-='*15)
nome = str(input('Nome do jogador: '))
gols = str(input('Número de Gols: '))
print(total(nome,gols))
print('-='*15)