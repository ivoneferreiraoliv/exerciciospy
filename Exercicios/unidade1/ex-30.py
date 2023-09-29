valorHora = float(input('Quanto você ganha por hora? '))
horasTrabalhadas = float(input('Quantas horas você trabalhou no mês? '))
salarioBruto = valorHora * horasTrabalhadas
if salarioBruto <= 900 :
    print('Salário Bruto: R$ {:.2f}'.format(salarioBruto))
    print('(-) IR (Isento)')
    print('(-) INSS (10%) : R$ {:.2f}'.format(salarioBruto * 0.1))
    print('FGTS (11%) : R$ {:.2f}'.format(salarioBruto * 0.11))
    print('Total de descontos : R$ {:.2f}'.format(salarioBruto * 0.1))
    print('Salário Líquido : R$ {:.2f}'.format(salarioBruto - (salarioBruto * 0.1)))
elif salarioBruto > 900 and salarioBruto <= 1500 :
    print('Salário Bruto: R$ {:.2f}'.format(salarioBruto))
    print('(-) IR (5%) : R$ {:.2f}'.format(salarioBruto * 0.05))
    print('(-) INSS (10%) : R$ {:.2f}'.format(salarioBruto * 0.1))
    print('FGTS (11%) : R$ {:.2f}'.format(salarioBruto * 0.11))
    print('Total de descontos : R$ {:.2f}'.format(salarioBruto * 0.15))
    print('Salário Líquido : R$ {:.2f}'.format(salarioBruto - (salarioBruto * 0.15)))
elif salarioBruto > 1500 and salarioBruto <= 2500 :
    print('Salário Bruto: R$ {:.2f}'.format(salarioBruto))
    print('(-) IR (10%) : R$ {:.2f}'.format(salarioBruto * 0.1))
    print('(-) INSS (10%) : R$ {:.2f}'.format(salarioBruto * 0.1))
    print('FGTS (11%) : R$ {:.2f}'.format(salarioBruto * 0.11))
    print('Total de descontos : R$ {:.2f}'.format(salarioBruto * 0.2))
    print('Salário Líquido : R$ {:.2f}'.format(salarioBruto - (salarioBruto * 0.2)))
else :
    print('Salário Bruto: R$ {:.2f}'.format(salarioBruto))
    print('(-) IR (20%) : R$ {:.2f}'.format(salarioBruto * 0.2))
    print('(-) INSS (10%) : R$ {:.2f}'.format(salarioBruto * 0.1))
    print('FGTS (11%) : R$ {:.2f}'.format(salarioBruto * 0.11))
    print('Total de descontos : R$ {:.2f}'.format(salarioBruto * 0.3))
    print('Salário Líquido : R$ {:.2f}'.format(salarioBruto - (salarioBruto * 0.3)))
    
