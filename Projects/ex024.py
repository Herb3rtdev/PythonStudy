cidade = str(input('Digite o nome da sua cidade:')).strip()
maisc = cidade.upper()
separa = maisc.split()
nome ='SANTO' in separa[0]
print(nome)
#guanabara
cidade = str(input('Digite o nome da sua cidade:')).strip()
print(cidade[:5].upper() == 'SANTO')