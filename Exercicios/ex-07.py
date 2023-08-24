ganhoPorHora = float(input("Quanto você ganha por hora? "))
horasTrabalhadas = float(input("Quantas horas você trabalhou no mês? "))
salario = ganhoPorHora * horasTrabalhadas
print(f"Seu salário é de R${salario:.2f}")

# o .2f é para limitar o número de casas decimais a 2