numero = int(input("Digite um número inteiro: "))
if numero >= -64 and numero <= 63:
    if numero >= 0:
        sinal = 0
    else:
        sinal = 1
        numero = -numero
    bits = []
    for i in range(7):
        bits.append(numero % 2)
        numero = numero // 2
    bits.append(sinal)
    bits.reverse()
    print(bits)
else:
    print("Número inválido!")
print("Fim do programa!")
