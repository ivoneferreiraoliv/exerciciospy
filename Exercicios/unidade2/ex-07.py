idades = []
alturas = []
for i in range(10):
    idades.append(int(input("Digite a idade: ")))
    alturas.append(float(input("Digite a altura: ")))
maior_altura = max(alturas)
indice_maior_altura = alturas.index(maior_altura)
print(f"A pessoa com maior altura tem {idades[indice_maior_altura]} anos.")
