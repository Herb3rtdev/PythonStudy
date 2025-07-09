lista = []
expressao = str(input('Digite uma expressao:'))
for simbolos in expressao:
    if simbolos == '(':
        lista.append('(')
    elif simbolos == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressao válida.')
else:
    print('Expressao inválida.')        
