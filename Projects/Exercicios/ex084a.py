dados = []
pesados = []
leves = []
maisp = menosp = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso Kg: '))
    dados.append([nome,peso])
    if len(dados) == 1:
        maisp = menosp = peso
    else:
        if peso > maisp:
            maisp = peso
        if peso < menosp:
            menosp = peso
    resp = str(input('Voce quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for dado in dados:
    if dado[1] == maisp:
        pesados.append(dado[0])
    if dado[1] == menosp:
        leves.append(dado[0])
print(f'O total de pessoas cadastradas foi {len(dados)}')
print(f'O mais pesado foi {maisp:.1f}kg e as pessoas mais pesadas são {", ".join(pesados)}')
print(f'O mais leve foi {menosp:.1f}kg e as pessoas mais leves são {", ".join(leves)}')

