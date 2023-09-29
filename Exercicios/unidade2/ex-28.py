# 28.	Escreva um programa em Python para corrigir uma prova com 10 questões de múltipla escolha (a, b, c, d ou e), em uma turma com 15 alunos. Cada questão vale 1 ponto. Leia o gabarito apenas uma vez, e para cada aluno leia sua matricula (número inteiro) e suas respostas. Calcule e escreva para cada aluno: sua matrícula, suas respostas, e sua nota. OBS: utilizar matrizes na solução.
matriz = []
for i in range(15):
    matriz.append([])
    for j in range(11):
        matriz[i].append(0)
for i in range(15):
    matriz[i][0] = int(input("Digite a matrícula do aluno: "))
    for j in range(1, 11):
        matriz[i][j] = input(f"Digite a resposta da questão {j}: ")
gabarito = []
for i in range(1, 11):
    gabarito.append(input(f"Digite a resposta da questão {i}: "))
for i in range(15):
    nota = 0
    for j in range(1, 11):
        if matriz[i][j] == gabarito[j - 1]:
            nota += 1
    matriz[i].append(nota)
for i in range(15):
    print(f"Matrícula: {matriz[i][0]}")
    print("Respostas:")
    for j in range(1, 11):
        print(f"Questão {j}: {matriz[i][j]}")
    print(f"Nota: {matriz[i][11]}")
    print()
print("Fim do programa!")
