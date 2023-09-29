pedido = True
total = 0

while pedido:
    codigo = int(input("Digite o código do produto: "))
    if codigo == 0:
        pedido = False
    else:
        quantidade = int(input("Digite a quantidade: "))
        if codigo == 100:
            total += 1.2 * quantidade
        elif codigo == 101:
            total += 1.3 * quantidade
        elif codigo == 102:
            total += 1.5 * quantidade
        elif codigo == 103:
            total += 1.2 * quantidade
        elif codigo == 104:
            total += 1.3 * quantidade
        elif codigo == 105:
            total += 1 * quantidade
        else:
            print("Código inválido!")
print(f"Total: {total:.2f}")

