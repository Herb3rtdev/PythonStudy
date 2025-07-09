from datetime import date
ano = int(input('Em que ano voce nasceu?'))
atual = date.today().year
idade = atual - ano
print('Sua idade é de {} anos e voce se classifica como: '.format(idade))
if idade < 9:
    print('-->Mirim')
elif idade <= 14:
    print('-->Infantil')
elif idade <= 19:
    print('-->Junior')
elif idade <= 25:
    print('-->Senior')
elif idade > 25:
    print('-->Master')

