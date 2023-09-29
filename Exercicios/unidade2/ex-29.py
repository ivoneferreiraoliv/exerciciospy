tamanhos = [35, 36, 37, 38, 39, 40]
marcas = ["A", "B", "C"]
matriz = []
for i in range(3):
    matriz.append([])
    for j in range(6):
        matriz[i].append(0)
for i in range(3):
    for j in range(6):
        matriz[i][j] = int(input(f"Digite a quantidade de sapatos da marca {marcas[i]} e tamanho {tamanhos[j]}: "))
maior = matriz[0][0]
linha = 0
coluna = 0
for i in range(3):
    for j in range(6):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha = i
            coluna = j
print(f"Numeração com maior quantidade em estoque: {tamanhos[coluna]} ({matriz[linha][coluna]} unidades)")
print("Fim do programa!")


