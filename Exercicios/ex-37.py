valorSaque = int(input('Digite o valor do saque: '))
if valorSaque >= 10 and valorSaque <= 600:
    print('Valor do saque: R$ {}'.format(valorSaque))
    notas100 = valorSaque // 100
    valorSaque = valorSaque % 100
    notas50 = valorSaque // 50
    valorSaque = valorSaque % 50
    notas10 = valorSaque // 10
    valorSaque = valorSaque % 10
    notas5 = valorSaque // 5
    valorSaque = valorSaque % 5
    notas1 = valorSaque // 1
    print('Notas de 100: {}'.format(notas100))
    print('Notas de 50: {}'.format(notas50))
    print('Notas de 10: {}'.format(notas10))
    print('Notas de 5: {}'.format(notas5))
    print('Notas de 1: {}'.format(notas1))
else:
    print('Valor de saque inválido')
