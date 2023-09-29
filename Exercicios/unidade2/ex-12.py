listaNomes = []
for i in range(10):
    listaNomes.append(input(f"Digite o {i + 1}º nome: "))
nome = input("Digite um nome qualquer: ")
if nome in listaNomes:
    print("ACHEI")
else:
    print("NÃO ACHEI")
