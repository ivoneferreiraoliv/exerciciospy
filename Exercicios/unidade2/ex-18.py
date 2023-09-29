matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input(f"Digite o valor para a posição ({i}, {j}): ")))
    matriz.append(linha)
contador = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] > 10:
            contador += 1
print(f"A matriz possui {contador} valores maiores que 10.")
print("Fim do programa!")
