# Programa que intercala duas listas
lista1 = []
lista2 = []
lista3 = []
for i in range(10):
    lista1.append(int(input(f"Digite o {i + 1}º número da lista 1: ")))
    lista2.append(int(input(f"Digite o {i + 1}º número da lista 2: ")))
    lista3.append(lista1[i])
    lista3.append(lista2[i])
print(lista3)
# Altere o programa anterior, intercalando
lista1 = []
lista2 = []
lista3 = []
for i in range(10):
    lista1.append(int(input(f"Digite o {i + 1}º número da lista 1: ")))
    lista2.append(int(input(f"Digite o {i + 1}º número da lista 2: ")))
    lista3.append(lista1[i])
    lista3.append(lista2[i])
print(lista3)

