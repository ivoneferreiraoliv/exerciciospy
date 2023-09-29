listaOriginal = []
for i in range(20):
    listaOriginal.append(int(input("Digite um número: ")))
lista = listaOriginal.copy()
maior = lista[0]
for i in range(1, len(lista)):
    if lista[i] > maior:
        maior = lista[i]
lista.remove(maior)
segundoMaior = lista[0]
for i in range(1, len(lista)):
    if lista[i] > segundoMaior:
        segundoMaior = lista[i]
print(f"O segundo maior elemento da lista é {segundoMaior}.")
print("Fim do programa!")
