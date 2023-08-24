preçoDeCusto = float(input('Digite o preço de custo: '))
percentualDeLucro = float(input('Digite o percentual de lucro: '))
preçoDeVenda = preçoDeCusto + (preçoDeCusto * percentualDeLucro / 100)
print(f'O preço de venda é {preçoDeVenda:.2f}')
