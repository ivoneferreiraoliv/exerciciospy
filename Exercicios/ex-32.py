nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >=9 and media <=10:
    print('A média do aluno é {} e ele está APROVADO com conceito A'.format(media))
elif media >= 7.5 and media < 9:
    print('A média do aluno é {} e ele está APROVADO com conceito B'.format(media))
elif media >= 6 and media < 7.5:
    print('A média do aluno é {} e ele está APROVADO com conceito C'.format(media))
elif media >= 4 and media < 6:
    print('A média do aluno é {} e ele está REPROVADO com conceito D'.format(media))
elif media >= 0 and media < 4:
    print('A média do aluno é {} e ele está REPROVADO com conceito E'.format(media))
else:
    print('Digite uma nota válida')

