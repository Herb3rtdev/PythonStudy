#Parametro opcional
def soma(a=0, b=0, c=0):
    """
    Soma no máximo tres variaveis ao passar disso da erro. Já seu colocar menos que tres vai funcionar.
    a=b=c Posso colocar qualquer valor ou até nao declarar nenhum valor que irá funcionar  
    """
    s = a + b + c
    print(s)
    


soma(4,5)
soma(1, 5, 6)
soma()
soma(b=5,c=10)
help(soma)