preco1 = float(input('Digite o preço do produto: R$'))
preco2 = float(input('Digite o preço do produto: R$'))
preco3 = float(input('Digite o preço do produto: R$'))
if preco1 < preco2 and preco1 < preco3:
    print('O produto mais barato é o de R${:.2f}'.format(preco1))
elif preco2 < preco1 and preco2 < preco3:
    print('O produto mais barato é o de R${:.2f}'.format(preco2))
else:   
    print('O produto mais barato é o de R${:.2f}'.format(preco3))
