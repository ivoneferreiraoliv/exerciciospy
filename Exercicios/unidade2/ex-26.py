matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input(f"Digite o valor para a posição ({i}, {j}): ")))
    matriz.append(linha)
print("Matriz original:")
for i in range(4):
    for j in range(4):
        print(f"{matriz[i][j]:^5}", end="")
    print()
for i in range(4):
    for j in range(4):
        if i < j:
            matriz[i][j] = 0
print("Matriz transformada:")
for i in range(4):
    for j in range(4):
        print(f"{matriz[i][j]:^5}", end="")
    print()
print("Fim do programa!")