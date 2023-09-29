matriz1 = []
matriz2 = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(float(input(f"Digite o valor para a posição ({i}, {j}) da matriz 1: ")))
    matriz1.append(linha)
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(float(input(f"Digite o valor para a posição ({i}, {j}) da matriz 2: ")))
    matriz2.append(linha)
matriz3 = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(0)
    matriz3.append(linha)
for i in range(2):
    for j in range(2):
        matriz3[i][j] = matriz1[i][j] + matriz2[i][j]
print("Matriz 1:")
for i in range(2):
    for j in range(2):
        print(f"{matriz1[i][j]:^5}", end="")
    print()
print("Matriz 2:")
for i in range(2):
    for j in range(2):
        print(f"{matriz2[i][j]:^5}", end="")
    print()
print("Matriz 3:")
for i in range(2):
    for j in range(2):
        print(f"{matriz3[i][j]:^5}", end="")
    print()
print("Fim do programa!")
