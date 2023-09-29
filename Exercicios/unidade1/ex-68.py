# 68.	A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
# Média do salário da população;
# Média do número de filhos;
# Maior salário;
# Percentual de pessoas com salário até R$250,00.

loop = True
maiorSalario = somaSalario = somaFilhos = qtdSalarioAte250 = 0
while loop:
    salario = float(input("Digite o salário: "))
    if salario <= 0:
        loop = False
    else:
        filhos = int(input("Digite o número de filhos: "))
        somaSalario += salario
        somaFilhos += filhos
        if salario > maiorSalario:
            maiorSalario = salario
        if salario <= 250:
            qtdSalarioAte250 += 1
mediaSalario = somaSalario / (qtdSalarioAte250 + 1)
mediaFilhos = somaFilhos / (qtdSalarioAte250 + 1)
print("Média do salário da população: ", mediaSalario)
print("Média do número de filhos: ", mediaFilhos)
print("Maior salário: ", maiorSalario)
print("Percentual de pessoas com salário até R$250,00: ", (qtdSalarioAte250 + 1) / 100, "%")

