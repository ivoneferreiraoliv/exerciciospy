matriz = []
for i in range(3):
    matriz.append([])
    for j in range(4):
        matriz[i].append(0)
for i in range(3):
    for j in range(4):
        matriz[i][j] = float(input(f"Digite a quantidade de grãos da região {i + 1} e tipo {j + 1} no ano de 2017: "))
for i in range(3):
    for j in range(4):
        matriz[i][j] = float(input(f"Digite a quantidade de grãos da região {i + 1} e tipo {j + 1} no ano de 2018: "))
for i in range(3):
    for j in range(4):
        matriz[i][j] = float(input(f"Digite a quantidade de grãos da região {i + 1} e tipo {j + 1} no ano de 2019: "))
for i in range(3):
    for j in range(4):
        matriz[i][j] = float(input(f"Digite a quantidade de grãos da região {i + 1} e tipo {j + 1} no ano de 2020: "))
for i in range(3):
    for j in range(4):
        matriz[i][j] = float(input(f"Digite a quantidade de grãos da região {i + 1} e tipo {j + 1} no ano de 2021: "))
for i in range(3):
    for j in range(4):
        matriz[i][j] = float(input(f"Digite a quantidade de grãos da região {i + 1} e tipo {j + 1} no ano de 2022: "))
for i in range(3):
    for j in range(4):
        matriz[i][j] = float(input(f"Digite a quantidade de grãos da região {i + 1} e tipo {j + 1} no ano de 2023: "))
for i in range(3):
    for j in range(4):
        matriz[i][j] = float(input(f"Digite a quantidade de grãos da região {i + 1} e tipo {j + 1} no ano de 2024: "))
for i in range(3):
    for j in range(4):
        matriz[i][j] = float(input(f"Digite a quantidade de grãos da região {i + 1} e tipo {j + 1} no ano de 2025: "))
for i in range(3):
    for j in range(4):
        matriz[i][j] = matriz[i][j] * 1.3
print("Previsão de produção para 2026:")
for i in range(3):
    for j in range(4):
        print(f"{matriz[i][j]:^5}", end="")
    print()
print("Fim do programa!")

