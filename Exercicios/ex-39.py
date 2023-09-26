#eia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é: par ou ímpar; positivo ou negativo; inteiro ou decimal. 
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação desejada: ')
if operacao == '+':
    print('O resultado da soma é: {}'.format(numero1 + numero2))
    if (numero1 + numero2) % 2 == 0:
        print('O resultado da soma é par')
    else:
        print('O resultado da soma é ímpar')
    if (numero1 + numero2) >= 0:
        print('O resultado da soma é positivo')
    else:
        print('O resultado da soma é negativo')
    if (numero1 + numero2) % 1 == 0:
        print('O resultado da soma é inteiro')
    else:
        print('O resultado da soma é decimal')
elif operacao == '-':
    print('O resultado da subtração é: {}'.format(numero1 - numero2))
    if (numero1 - numero2) % 2 == 0:
        print('O resultado da subtração é par')
    else:
        print('O resultado da subtração é ímpar')
    if (numero1 - numero2) >= 0:
        print('O resultado da subtração é positivo')
    else:
        print('O resultado da subtração é negativo')
    if (numero1 - numero2) % 1 == 0:
        print('O resultado da subtração é inteiro')
    else:
        print('O resultado da subtração é decimal')
elif operacao == '*':
    print('O resultado da multiplicação é: {}'.format(numero1 * numero2))
    if (numero1 * numero2) % 2 == 0:
        print('O resultado da multiplicação é par')
    else:
        print('O resultado da multiplicação é ímpar')
    if (numero1 * numero2) >= 0:
        print('O resultado da multiplicação é positivo')
    else:
        print('O resultado da multiplicação é negativo')
    if (numero1 * numero2) % 1 == 0:
        print('O resultado da multiplicação é inteiro')
    else:
        print('O resultado da multiplicação é decimal')
elif operacao == '/':
    print('O resultado da divisão é: {}'.format(numero1 / numero2))
    if (numero1 / numero2) % 2 == 0:
        print('O resultado da divisão é par')
    else:
        print('O resultado da divisão é ímpar')
    if (numero1 / numero2) >= 0:
        print('O resultado da divisão é positivo')
    else:
        print('O resultado da divisão é negativo')
    if (numero1 / numero2) % 1 == 0:
        print('O resultado da divisão é inteiro')
    else:
        print('O resultado da divisão é decimal')
else:
    print('Operação inválida')        

