n1 = float(input('Primeira nota:'))
n2 = float(input('Seguda nota:'))
media = (n1 + n2) / 2
if media > 7:
    print('Sua media foi \033[34m{}\033[m'.format(media))
else:
    print('Sua media foi \033[31m{}\033[m'.format(media))
print('Vou analisar qual será sua situação!')
if media >= 7:
    print('Parabéns voce foi \033[34mAPROVADO!\033[m')
elif 7 < media >= 5:
    print('Voce terá que fazer \033[33mRECUPERAÇAO\033[m!')
elif media < 5:
    print('Voce foi \033[31mREPROVADO\033[m')

