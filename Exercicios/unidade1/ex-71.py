pontos = 0
while True:
    gols = int(input("Digite o número de gols: "))
    if gols <= 0:
        break
    elif gols > 0:
        pontos += 3
    else:
        pontos += 1
print(f"Total de pontos: {pontos}")
