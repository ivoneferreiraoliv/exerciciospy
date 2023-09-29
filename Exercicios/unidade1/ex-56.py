N = int(input('Digite o valor de N: '))
soma = 0
m = 1
for i in range(1, N + 1):
    soma += i / m
    m += 2
print(f'A soma dos {N} primeiros termos da série é {soma:.2f}')
