listaTemperaturas = []
for i in range(12):
    listaTemperaturas.append(float(input(f"Digite a temperatura média do {i + 1}º mês: ")))
mediaTemperaturas = sum(listaTemperaturas) / len(listaTemperaturas)
print(f"A média anual das temperaturas é {mediaTemperaturas}ºC.")
print("Temperaturas acima da média anual:")
for i in range(len(listaTemperaturas)):
    if listaTemperaturas[i] > mediaTemperaturas:
        print(f"{i + 1} - {listaTemperaturas[i]}ºC")
