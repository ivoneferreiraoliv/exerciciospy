altura = float(input('Digite a altura: '))
sexo = input('Digite o sexo: ')
if sexo == 'm':
    peso = (72.7 * altura) - 58
    print(f'O peso ideal é {peso}')
elif sexo == 'f':
    peso = (62.1 * altura) - 44.7
    print(f'O peso ideal é {peso}')
else:
    print('Sexo inválido')

