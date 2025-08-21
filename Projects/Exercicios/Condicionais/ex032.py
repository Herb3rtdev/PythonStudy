from datetime import date
ano = int(input('Qual ano voce quer verificar? Digite 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:#nao pode ser divisível ou diferente de é o sinal '!='
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} nao é bissexto'.format(ano))
