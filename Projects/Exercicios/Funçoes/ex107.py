def imposto_de_renda(base):
    imposto = 0
    if base > 3000:
        imposto = imposto + ((base - 3000) * 0.35)
        base = 3000
    if base > 1000:
        imposto = imposto + ((base - 1000) * 0.20)
    return imposto


salario = float(input('Digite o seu salário: '))
base = salario 
imposto = imposto_de_renda(base)
print(f'Seu salário é R$ {salario:.2f} e o imposto que será pago é R$ {imposto:.2f}')
