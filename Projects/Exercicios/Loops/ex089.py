dados_completos = []
notas = []
dados = []
while True:
    dados.append(str(input('Nome: ')))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    notas.append(nota1)
    notas.append(nota2)
    dados.append(notas[:])
    notas.clear()
    dados.append(media)
    dados_completos.append(dados[:])
    dados.clear()
    resp = str(input('Voce quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(dados_completos)
print('-=-'*15)
print('No. Nome   Média')
print('---'*10)
for posicao,dados in enumerate(dados_completos):
    print(f'{posicao} {dados[0]}  {dados[2]}')
while True:
    for posicao, dados in enumerate(dados_completos):
        n = int(input('Mostrar notas de qual aluno? (999 interrompe):'))