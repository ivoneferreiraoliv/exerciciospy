numero = int(input('Digite um número: '))
contador = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        contador += 1
if contador == 2:
    print(f'{numero} é um número primo')
else:
    print(f'{numero} não é um número primo')