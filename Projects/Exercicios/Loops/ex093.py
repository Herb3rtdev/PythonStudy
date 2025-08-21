dados = {}
gols_lista = []
sgols = 0
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou?'))
for c in range(1,partidas+1):
     gols = int(input(f'Quantos gols na partida {c}?'))
     sgols += gols
     gols_lista.append(gols)
dados['gols'] = gols_lista
dados['total'] = sgols
print('-='*13)
for k,v in dados.items():
     print(f'O campo {k} tem o valor {v}.')
print('-='*13)
print(f'O {dados["nome"]} jogou {partidas} partidas.')
for pos,v in enumerate(gols_lista):
     print(f'   => Na partida {pos+1},fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols') 