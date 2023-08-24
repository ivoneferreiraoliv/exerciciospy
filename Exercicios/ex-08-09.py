grausFarenheit = float(input("Digite a temperatura em graus Farenheit: "))
grausCelsius = (grausFarenheit - 32) * 5 / 9
print(f"{grausFarenheit} graus Farenheit equivale a {grausCelsius} graus Celsius")

# O contrário:

grausCelsius = float(input("Digite a temperatura em graus Celsius: "))
grausFarenheit = (grausCelsius * 9 / 5) + 32
print(f"{grausCelsius} graus Celsius equivale a {grausFarenheit} graus Farenheit")
