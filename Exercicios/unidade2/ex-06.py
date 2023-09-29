numeros = []
soma = 0
multiplicacao = 1
for i in range(50):
    numeros.append(int(input("Digite um número: ")))
    soma += numeros[i]
    multiplicacao *= numeros[i]
print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")
print(f"Números: {numeros}")
