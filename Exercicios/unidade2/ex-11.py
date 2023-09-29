idades = []
alturas = []
for i in range(30):
    idades.append(int(input("Digite a idade: ")))
    alturas.append(float(input("Digite a altura: ")))
media_alturas = sum(alturas) / len(alturas)
contador = 0
for i in range(len(idades)):
    if idades[i] > 13 and alturas[i] < media_alturas:
        contador += 1
print(f"{contador} alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.")

