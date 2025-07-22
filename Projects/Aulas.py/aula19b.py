estado = {}
brasil = []
for contador in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for lista in brasil:
    for values in lista.values():
        print(values,end=' ')
    print()
        