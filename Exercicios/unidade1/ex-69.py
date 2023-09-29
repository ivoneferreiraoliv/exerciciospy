numeros = []
pares = []
impares = []
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"Quantidade de números pares: {len(pares)}")
print(f"Quantidade de números ímpares: {len(impares)}")
print(f"Média dos números pares: {sum(pares)/len(pares)}")
print(f"Média geral dos números: {sum(numeros)/len(numeros)}")
