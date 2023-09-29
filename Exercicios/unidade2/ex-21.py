matriz1 = []
matriz2 = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input(f"Digite o valor para a posição ({i}, {j}) da matriz 1: ")))
    matriz1.append(linha)
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input(f"Digite o valor para a posição ({i}, {j}) da matriz 2: ")))
    matriz2.append(linha)
matriz3 = []
for i in range(4):
    linha = []
    for j in range(4):
        if matriz1[i][j] > matriz2[i][j]:
            linha.append(matriz1[i][j])
        else:
            linha.append(matriz2[i][j])
    matriz3.append(linha)
print("Matriz 1:")
for i in range(4):
    for j in range(4):
        print(f"{matriz1[i][j]:^5}", end="")
    print()
print("Matriz 2:")
for i in range(4):
    for j in range(4):
        print(f"{matriz2[i][j]:^5}", end="")
    print()
print("Matriz 3:")
for i in range(4):
    for j in range(4):
        print(f"{matriz3[i][j]:^5}", end="")
    print()
print("Fim do programa!")
