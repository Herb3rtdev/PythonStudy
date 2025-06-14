s = float(input('Qual é o seu salário R$:'))
if s >= 1250:
    print('Seu salário era R${}. \nSeu novo salário será de R${:.2f}'.format(s,s * 1.10))
else:
    print('Seu salário era R${}. \nSeu novo salário será de R${:.2f}'.format(s,s * 1.15))
print('Parabéns pelo seu aumento!')
