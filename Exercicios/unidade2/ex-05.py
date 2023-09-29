notas = []
for i in range(10):
    notas.append([])
    for j in range(4):
        notas[i].append(float(input("Digite a nota do aluno %d: " % (i + 1))))
    print("Média do aluno %d: %.2f" % (i + 1, sum(notas[i]) / 4))
    if sum(notas[i]) / 4 >= 7:
        print("Aluno %d aprovado." % (i + 1))
    else:
        print("Aluno %d reprovado." % (i + 1))
