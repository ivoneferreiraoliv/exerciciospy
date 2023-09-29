# Programa que lê 10 números e os imprime na ordem inversa de leitura
numeros = []
for i in range(10):
    numeros.append(float(input("Digite um número: ")))
numeros.reverse()

print(numeros)




