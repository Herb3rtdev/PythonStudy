dados = {}
lista_dados = []
soma_idades = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F]')).strip().upper()
    dados['idade'] = int(input('Idade: '))
    soma_idades += dados['idade']
    lista_dados.append(dados.copy())
    resp = str(input('Voce quer continuar? [S/N]'))
    if resp in 'Nn':
        break 
media = soma_idades / len(lista_dados)
print('-='*15)
print(lista_dados)
print(f'- O grupo tem {len(lista_dados)} pessoas.')
print(f'- A média de idade é de {media} anos.')
print(f'- As mulheres foram:',end=' ')
for pessoas in lista_dados:
    if pessoas['sexo'] == 'F':
        print(pessoas['nome'],end=' ')
print('    \nLista das pessoas que estão acima da média:')
for pessoas in lista_dados:
    if pessoas['idade'] >= media:
        print(f'nome = {pessoas["nome"]}; sexo = {pessoas["sexo"]}; idade = {pessoas["idade"]};')