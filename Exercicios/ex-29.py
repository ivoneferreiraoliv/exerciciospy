salario = float(input('Digite o valor do salário: '))
if salario <= 280 :
    #aumento de 20%
    salario = salario + (salario * 0.2)
    print('Salário antes do reajuste: R$ {:.2f}'.format(salario - (salario * 0.2)))
    print('Percentual de aumento aplicado: 20%')
    print('Valor do aumento: R$ {:.2f}'.format(salario * 0.2))
    print('Novo salário: R$ {:.2f}'.format(salario))
elif salario > 280 and salario <= 700 :
    salario = salario + (salario * 0.15)
    print('Salário antes do reajuste: R$ {:.2f}'.format(salario - (salario * 0.15)))
    print('Percentual de aumento aplicado: 15%')
    print('Valor do aumento: R$ {:.2f}'.format(salario * 0.15))
    print('Novo salário: R$ {:.2f}'.format(salario))
elif salario > 700 and salario <= 1500 :
    print('Salário antes do reajuste: R$ {:.2f}'.format(salario - (salario * 0.1)))
    print('Percentual de aumento aplicado: 10%')
    print('Valor do aumento: R$ {:.2f}'.format(salario * 0.1))
    print('Novo salário: R$ {:.2f}'.format(salario))
else :
    print('Salário antes do reajuste: R$ {:.2f}'.format(salario - (salario * 0.05)))
    print('Percentual de aumento aplicado: 5%')
    print('Valor do aumento: R$ {:.2f}'.format(salario * 0.05))
    print('Novo salário: R$ {:.2f}'.format(salario))
    