import math
def area_circulo(R):
    area = math.pi * R ** 2
    return print('A área do círculo é %.3f ' % area)
R = float(input('Insira o raio do círculo: '))
area_circulo(R)

# o %3f é para limitar o número de casas decimais a 3

def area_quadrado(L):
    area = L ** 2
    return print('A área do quadrado é: ', area*2)
L = float(input('Insira o lado: '))
area_quadrado(L)