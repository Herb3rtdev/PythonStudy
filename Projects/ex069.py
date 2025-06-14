resp = ''
print('-=-'*10)
print('CADASTRE UMA PESSOA')
print('-=-'*10)
pessoasmais_18 = mulheresmenos_20 = homens = 0
while not resp == 'N':
    idade = int(input('Qual a sua idade:'))
    sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    resp = str(input('Voce quer continuar?[S/N]')).strip().upper()[0]
    while resp not in 'SsNn':
        resp = str(input('Voce quer continuar?[S/N]')).strip().upper()[0]
    print('=' * 35)
    if idade > 18:
        pessoasmais_18 += 1
    if sexo == 'F' and idade < 20:
        mulheresmenos_20 += 1
    if sexo == 'M':
        homens += 1
print(f'A quantidade de pessoas acima dos 18 é {pessoasmais_18}')
print(f'A quantidade de mulheres com menos de 20 anos é {mulheresmenos_20}')
print(f'A quantidade de homens cadastrados foi {homens}')