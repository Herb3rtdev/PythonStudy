#Diferença entre uma função com parametro e outra sem parametro

#Sem parametro
def linha():
    print('-'*15)


#Com parametro
def mensagem(txt):
    print('-'*15)
    print(txt)
    print('-'*15)

    
linha()
print('PYTHON CURSO')
linha()
print('ESTUDANDO PYTHON')
linha()
linha()
mensagem('Python Curso')
mensagem('Estudando Python')

