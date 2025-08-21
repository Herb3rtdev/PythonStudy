dados = {}
dados['Nome'] = str(input('Nome: '))
dados['Nota 1'] = float(input('Nota 1: '))
dados['Nota 2'] = float(input('Nota 2: '))
print('-='*15)
dados['Média'] = (dados['Nota 1'] + dados['Nota 2'])/ 2
if dados['Média'] >= 7:
    dados['Resultado'] = 'Aprovado'
elif 4 < dados['Média'] <= 6:
    dados['Resultado'] = 'Recuperaçao'
else:
    dados['Resultado'] = 'Reprovado'
for k,v in dados.items():
    print(f'{k} é igual a {v}')