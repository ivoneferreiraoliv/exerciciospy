# Exercício 3 - Média de notas
notas = []
for i in range(4):
    notas.append(float(input("Digite a nota: ")))
print(notas)
print(sum(notas) / len(notas))
5