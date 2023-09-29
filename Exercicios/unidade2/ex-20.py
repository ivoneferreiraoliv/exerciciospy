matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input(f"Digite o valor para a posição ({i}, {j}): ")))
    matriz.append(linha)
x = int(input("Digite um valor para buscar na matriz: "))
encontrado = False
for i in range(5):
    for j in range(5):
        if matriz[i][j] == x:
            print(f"O valor {x} foi encontrado na posição ({i}, {j}) da matriz.")
            encontrado = True
if not encontrado:
    print(f"O valor {x} não foi encontrado na matriz.")
print("Fim do programa!")