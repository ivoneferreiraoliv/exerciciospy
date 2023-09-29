# 66.	Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela abaixo: 
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1	0
# 310
#                   6	15

# Exemplo de saída do programa: 
# Valor da Dívida  Valor dos Juros  Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00              0                         1                                  R$  1.000,00
# R$ 1.100,00           100                        3                                 R$    366,00
# R$ 1.150,00           150                        6                                 R$    191,67

divida = float(input('Digite o valor da dívida: '))
juros = 0
parcelas = 1
valor_parcela = divida
print('Valor da Dívida  Valor dos Juros  Quantidade de Parcelas  Valor da Parcela')

while parcelas <= 6:
    if parcelas == 1:
        juros = 0
    elif parcelas == 3:
        juros = 10
    else:
        juros = 15
    valor_parcela = divida * (1 + juros/100) / parcelas
    print('R$ {:10.2f} {:10.2f} {:10d} {:10.2f}'.format(divida, divida * juros/100, parcelas, valor_parcela))
    parcelas += 1
    divida += divida * juros/100
print()
