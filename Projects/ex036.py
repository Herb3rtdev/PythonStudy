casa = float(input('Qual o valor da casa que voce deseja comprar? R$'))
salario = float(input('Qual é o valor do seu salário? R$'))
ano = int(input('Em quantos anos voce deseja pagar?'))
prestacao = casa / (ano * 12)
print('As parcelas serao de R${:.2f}'.format(prestacao))
if (salario * 0.3) < prestacao:
    print('Infelizmente, Seu salário é R${} e a prestação ficou acima do permitido que 30%(R${:.2f}) do seu salário.'.format(salario,salario * 0.3))
else:
    print('Parabens! Seu emprestimo foi aprovado! Serao parcelas de R${:.2f} por mes, em um total de {} anos'.format(prestacao,ano))

