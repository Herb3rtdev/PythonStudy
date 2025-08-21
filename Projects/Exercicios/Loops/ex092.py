from datetime import date
dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
data_atual = date.today()
dados['idade'] = data_atual.year - nascimento
dados['ctps'] = int(input('Carteira de trabalho (0 não tem):'))
if dados['ctps'] > 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: R$'))
    dados['sexo'] = str(input('Sexo [M/F]:'))
    if dados['sexo'] in 'Mm':
        temp_contribuicao = 40
    else:
        temp_contribuicao = 30
    anos_aposentadoria = dados['contratação'] + temp_contribuicao
    dados['aposentadoria'] = anos_aposentadoria - nascimento
print('-='*15)
for k,v in dados.items():
    print(f'{k} tem o valor {v}')