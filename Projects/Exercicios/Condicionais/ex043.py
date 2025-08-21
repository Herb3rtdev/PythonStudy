h = float(input('Digite sua altura (m):'))
m = float(input('Digite seu peso (Kg):'))
imc = m / (h ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Está abaixo do peso.')
elif  18.5 <= imc < 25:
    print('Está no peso ideal.')
elif  25 <= imc < 30:
    print('Está na faixa do sobrepeso.')
elif 30 <= imc < 40:
    print('Está na faixa de obeso')
elif imc > 40:
    print('Está na faixa de obesidade mórbida.')
