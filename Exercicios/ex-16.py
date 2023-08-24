nome = (input('Digite seu nome: '))
salarioFixo = float(input('Digite seu salário fixo: '))
totalVendas = float(input('Digite o total de vendas: '))
comissao = totalVendas * 1.15
salarioTotal = salarioFixo + comissao
print(f'Nome: {nome}', f'Salário fixo: R${salarioFixo}', f'Total de vendas: {totalVendas}', f'Salário total: R${salarioTotal}', sep='\n')