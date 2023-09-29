matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Digite o valor para a posição ({i}, {j}): ")))
    matriz.append(linha)
soma = 0
for i in range(3):
    for j in range(3):
        if i + j == 2:
            soma += matriz[i][j]
print(f"A soma dos elementos da diagonal secundária é {soma}.")
print("Fim do programa!")
