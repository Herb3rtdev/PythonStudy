def numero_extenso(n):
    numeros = ('zero','um ','dois' , 'tres','quatro',' cinco', 'seis' ,'sete' ,'oito' , 'nove' , 'dez')
    return numeros[n]


n = int(input('Digite um número entre 0 e 10:'))
print(numero_extenso(n))