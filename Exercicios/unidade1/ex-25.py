nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media >= 7 and media < 10:
    print(f'Sua média foi {media:.2f}. Aprovado!')
elif media <7:
    print(f'Sua média foi {media:.2f}. Reprovado!')
elif media == 10:
    print(f'Sua média foi {media:.2f}. Aprovado com Distinção!')
else:
    print('Digite uma nota válida!')