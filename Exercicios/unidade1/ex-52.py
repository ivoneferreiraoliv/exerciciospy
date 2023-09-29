N = int(input('Digite o valor de N: '))
H = 1
for i in range(2, N + 1):
    H += 1 / i
print(f'O valor de H é {H:.2f}')
