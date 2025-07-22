brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'Rj'}
estado2 = {'uf': 'São Paulo','Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
for lista in brasil:
    for values in lista.values():
        print(values,end='...')
    print()
