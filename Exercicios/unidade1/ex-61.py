idades = [] 
for i in range(0, 5):
    idade = int(input('Informe a idade: '))
    idades.append(idade)
media = sum(idades) / len(idades)
if media >= 0 and media <= 25:
    print('Turma jovem')
elif media >= 26 and media <= 60:
    print('Turma adulta')
else:
    print('Turma idosa')
