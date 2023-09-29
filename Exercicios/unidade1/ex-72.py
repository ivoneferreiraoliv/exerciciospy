numero = int(input("Digite um número: "))
i = 1
while i * (i + 1) * (i + 2) < numero:
    i += 1
if i * (i + 1) * (i + 2) == numero:
    print(f"{numero} é triangular.")
else:
    print(f"{numero} não é triangular.")
    