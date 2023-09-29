numeroDeTemperaturas = int(input('Digite o número de temperaturas: '))
cont = 1
soma = 0
while cont <= numeroDeTemperaturas:
    temperatura = float(input('Digite a temperatura: '))
    if cont == 1:
        maior = temperatura
        menor = temperatura
    else:
        if temperatura > maior:
            maior = temperatura
        if temperatura < menor:
            menor = temperatura
    soma += temperatura
    cont += 1
print('Maior temperatura: ', maior)
print('Menor temperatura: ', menor)
print('Média das temperaturas: ', soma/numeroDeTemperaturas)
