quantidadeMorango = float(input('Digite a quantidade de morangos: '))
quantidadeMaca = float(input('Digite a quantidade de maçãs: '))
if quantidadeMorango <= 5:
    precoMorango = 2.50
else:
    precoMorango = 2.20
if quantidadeMaca <= 5:
    precoMaca = 1.80
else:
    precoMaca = 1.50
precoTotal = (quantidadeMorango * precoMorango) + (quantidadeMaca * precoMaca)
if (quantidadeMorango + quantidadeMaca) > 8 or precoTotal > 25:
    precoTotal = precoTotal - (precoTotal * 0.10)
print('Preço total: R$ {}'.format(precoTotal))
