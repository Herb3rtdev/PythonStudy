expressao = str(input('Digite uma expressao: '))
lista = []
quant1 = quant2 = 0
for colchetes in expressao:
    if colchetes == '(':
        lista.append('(')
        quant1 += 1
    elif colchetes == ')':
        lista.append(')')
        quant2 += 1
if quant1 == quant2:
    print('Sistema válido')
else:
    print('Sistema ínvalido')