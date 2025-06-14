valor = int(input('Qual valor a ser sacado? R$'))
cedulas50 = valor // 50
print(f'Total de {cedulas50} cédulas de R$50')
cedulas20 = (valor - (cedulas50 * 50))//20
print(f'Total de {cedulas20} cédulas de R$20')
cedulas10 = (valor - ((cedulas50 * 50) + (cedulas20 * 20)))//10
print(f'Total de {cedulas10} cédulas de R$10')
cedulas1 = (valor - ((cedulas50 * 50) + (cedulas20 * 20) + (cedulas10 * 10)))//1
print(f'Total de {cedulas1} cédulas de R$1')