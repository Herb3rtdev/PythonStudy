pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['Sexo'])
print(pessoas['idade'])
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
for values in pessoas.values():
    print(values)
for keys in pessoas.keys():
    print(keys)
for keys,values in pessoas.items():
    print(f'{keys}:{values}')
del pessoas ['idade']
pessoas['Peso'] = 76.6
pessoas['Sexo'] = 'Masculino'
print(pessoas)