from time import sleep
from datetime import date
atual = date.today().year
nascimento = int(input('Qual sua data de nascimento?'))
nome = str(input('Qual é o seu nome:'))
digite = int(input('''Qual é o seu sexo: 
[1] masculino
[2] feminino
-->'''))
if digite == 1:
    print('Seu alistamento é obrigatório!')
elif digite == 2:
    print('Seu alistamento não é obrigatório.')
else:
    print('Não entendi...Digite novamente.')
idade = atual - nascimento
print('{} sua idade é {} e eu irei analisar sua situação.'.format(nome, idade))
print('Analisando...')
sleep(3)
if idade == 18:
    print('Está no momento exato para se alistar.')
elif idade > 18:
    print('já passou da ora de se alistar!\nTerá que pagar uma multa!\nA idade ideal é aos 18.\nO atraso é de {} anos'.format(idade - 18))
    tempcerto = atual - (idade - 18)
    print('Seu alistamento era para ter sido em {}'.format(tempcerto))
elif idade < 18:
    print('Aguarde mais um pouco, não é hora de se alistar ainda.Falta {} anos para voce poder se alistar'.format(18 - idade))
    tempfut = atual + (18 - idade)
    print('Seu alistamento vai ser em {}'.format(tempfut))