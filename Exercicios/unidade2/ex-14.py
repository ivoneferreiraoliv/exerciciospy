numeros = []
numero = int(input("Digite um número: "))
while numero != -1:
    numeros.append(numero)
    numero = int(input("Digite um número: "))
print(f"Quantidade de valores lidos: {len(numeros)}")
print("Valores na ordem em que foram informados:")
for i in range(len(numeros)):
    print(numeros[i])
print("Valores na ordem inversa à que foram informados:")
for i in range(len(numeros) - 1, -1, -1):
    print(numeros[i])
soma = 0
for i in range(len(numeros)):
    soma += numeros[i]
print(f"Soma dos valores: {soma}")
media = soma / len(numeros)
print(f"Média dos valores: {media}")
contador = 0
for i in range(len(numeros)):
    if numeros[i] > media:
        contador += 1
print(f"Quantidade de valores acima da média: {contador}")
contador = 0
for i in range(len(numeros)):
    if numeros[i] < 7:
        contador += 1
print(f"Quantidade de valores abaixo de 7: {contador}")
print("Fim do programa!")


