#calcula o fatorial de um dado número N
n = int(input('Digite o número: '))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(f'O fatorial de {n} é {fatorial}')
