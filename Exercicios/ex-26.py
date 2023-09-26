numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')
numero3 = input('Digite mais um número: ')
if numero1 > numero2 and numero1 > numero3:
    print('O maior número é o {}'.format(numero1))
elif numero2 > numero1 and numero2 > numero3:
    print('O maior número é o {}'.format(numero2))
else:
    print('O maior número é o {}'.format(numero3))
