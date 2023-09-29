# 64.	Escreva um programa que imprima os N termos de uma Progressão Aritmética, conforme fórmula a seguir. O usuário deverá fornecer o valor de: n (número de termos), r (razão) e a1 (primeiro termo da série).
n = int(input('Digite o número de termos: '))
r = int(input('Digite a razão: '))
a1 = int(input('Digite o primeiro termo: '))
cont = 1
while cont <= n:
    print(a1, end=' ')
    a1 += r
    cont += 1
print()

