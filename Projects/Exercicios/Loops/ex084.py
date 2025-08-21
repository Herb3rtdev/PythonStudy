dados = []
compostos = []
mais_pesado = mais_leve = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso Kg: ')))
    compostos.append(dados[:])
    dados.clear()
    resp = str(input('Voce quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(compostos)
for posicao,dados in enumerate(compostos):
    if posicao == 0:
        mais_pesado = mais_leve = dados[1]
    else:
        if dados[1] > mais_pesado:
            mais_pesado = dados[1]
        if dados[1] < mais_leve:
            mais_leve = dados[1]
print(f'Ao todo voce cadastrou {len(compostos)} pessoas na lista')
print(f'O maior peso é {mais_pesado} e as pessoas mais pesadas são',end=' ')
for dados in compostos:
    if dados[1] == mais_pesado:
        print(dados[0],end=' ')
print(f'\nO menor peso é {mais_leve} e as pessoas mais leves são',end=' ')
for dados in compostos:
    if dados[1] == mais_leve:
        print(dados[0],end=' ')
    
    
