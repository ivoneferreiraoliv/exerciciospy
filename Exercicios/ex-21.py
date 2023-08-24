ganhoPorHora = float(input("Quanto você ganha por hora? "))
horasTrabalhadas = float(input("Quantas horas você trabalhou no mês? "))
salarioBruto = ganhoPorHora * horasTrabalhadas
impostoDeRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - impostoDeRenda - inss - sindicato
print("Salário Bruto: R$", salarioBruto)
print("Imposto de Renda: R$", impostoDeRenda)
print("INSS: R$", inss)
print("Sindicato: R$", sindicato)
print("Salário Líquido: R$", salarioLiquido)

