listaA = []
soma = 0
for i in range(10):
    listaA.append(int(input("Digite um número: ")))
    soma += listaA[i] ** 2
print(f"Soma dos quadrados: {soma}")
