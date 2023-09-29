notas = []
for i in range(30):
    nota = float(input('Digite a nota: '))
    notas.append(nota)
media = sum(notas) / len(notas)
print(f'A média é {media}')
for i in range(len(notas)):
    if notas[i] >= 7:
        print(f'O aluno {i} está aprovado')
    elif notas[i] >= 5 and notas[i] < 7:
        print(f'O aluno {i} está de recuperação')
    else:
        print(f'O aluno {i} está reprovado')