matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=" ")
    print()
print("Fim do programa!")
