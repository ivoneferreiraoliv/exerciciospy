#programa que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
#Álcool: até 20 litros, desconto de 3% por litro acima de 20 litros, desconto de 5% por litro 
#Gasolina: até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro.
numeroLitros = float(input('Digite o número de litros vendidos: '))
tipoCombustivel = input('Digite o tipo de combustível: ')
if tipoCombustivel == 'A':
    if numeroLitros <= 20:
        precoLitro = 1.90
        desconto = 0.03
    else:
        precoLitro = 1.90
        desconto = 0.05
elif tipoCombustivel == 'G':
    if numeroLitros <= 20:
        precoLitro = 2.50
        desconto = 0.04
    else:
        precoLitro = 2.50
        desconto = 0.06
else:
    print('Tipo de combustível inválido')
precoTotal = numeroLitros * precoLitro
precoTotal = precoTotal - (precoTotal * desconto)
print('Preço total: R$ {}'.format(precoTotal))

