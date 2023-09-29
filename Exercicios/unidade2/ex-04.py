numeros = []
pares = []
impares = []
for i in range(20):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"Números: {numeros}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")



