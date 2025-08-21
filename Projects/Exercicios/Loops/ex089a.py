dados = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    resp = str(input('Quer continuar? [S/N]'))
    dados.append([nome,[nota1, nota2], media])
    if resp in 'Nn':
        break
print('-='*15)
print(f'{"NO.":<4}{"NOME":^6}{"MÉDIA":>9}')
print('-='*20)
for posicao,dado in enumerate(dados):
    print(f'{posicao:<4}{dado[0]:^6}{dado[2]:>9}')
while True:
    print('-='*20)
    n = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if n == 999:
        print('Encerrando...')
        break
    if n <= len(dados) - 1:
        print(f'Notas de {dados[n][0]} são {dados[n][1]}')
