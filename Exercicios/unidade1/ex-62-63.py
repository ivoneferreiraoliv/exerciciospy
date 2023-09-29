termo1 = int(input('Digite o primeiro termo: '))
termo2 = int(input('Digite o segundo termo: '))
n = int(input('Digite o número de termos: '))
if n < 3:
    print('O número de termos deve ser maior ou igual a 3')
else:
    cont = 3
    while cont <= n:
        if cont % 2 == 1:
            termo1 = termo1 + termo2
        else:
            termo2 = termo2 + termo1
        cont += 1
    print(termo1, termo2)