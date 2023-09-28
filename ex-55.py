numero = float(input('Digite o valor de x: '))
soma = 0
for i in range(1, 51):
    if i % 2 == 0:
        soma -= numero ** (2 * i - 1) / (2 * i - 1)
    else:
        soma += numero ** (2 * i - 1) / (2 * i - 1)
print(f'O valor do arco tangente de {numero} é {soma:.2f}')

