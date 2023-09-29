valorA = int(input('Digite o valor A: '))
valorB = int(input('Digite o valor B: '))
resultado = 1
for i in range(1, valorB + 1):
    resultado *= valorA
print(f'O valor de {valorA} elevado a {valorB} é {resultado}')

