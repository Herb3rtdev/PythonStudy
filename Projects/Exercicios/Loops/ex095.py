
registros = []
while True:
    dados = {}
    gols_marcados = []
    total_gols = 0
    print('---'*10)
    dados['nome'] = str(input('Nome do jogador:'))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou?'))
    for p in range(1,partidas+1):
        gols = int(input(f'Quantos gols na partida {p}?'))
        gols_marcados.append(gols)
        total_gols += gols
    dados['gols'] = gols_marcados
    dados['total'] = total_gols
    registros.append(dados.copy())
    resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if resp in 'Nn':
        break
print('-='*14)
print(f'{"Cod":<2}{"nome":<4}{"gols":>8}{"total":>14}')
for pos, termos in enumerate(registros):
    print(f'{pos:<2}{termos["nome"]:<4}{termos["gols"]:>8}{termos["total"]:>14}')
print('---'*10)
