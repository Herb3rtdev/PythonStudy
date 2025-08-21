nome = str(input('Digite um nome:')).strip()
separado = nome.split()
print('Primeiro:{}'.format(separado[0]))
print('último:{}'.format(separado[len(separado)-1]))