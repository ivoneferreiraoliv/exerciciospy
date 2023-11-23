def ler_angulos():
    entrada = input("Digite os ângulos separados por espaço (ex: 18g25m1s 30g15m30s): ")
    angulos_str = entrada.split()
    return angulos_str

def converter_para_graus_minutos_segundos(angulo_str):
    partes = angulo_str[:-1].split('g')
    
    graus = int(partes[0]) if partes[0] else 0
    
    if len(partes) > 1:
        minutos_partes = partes[1].split('m')
        minutos = int(minutos_partes[0]) if minutos_partes[0] else 0
    else:
        minutos = 0
    
    if len(partes) > 2:
        segundos_partes = partes[2].split('s')
        segundos = int(segundos_partes[0]) if segundos_partes[0] else 0
    else:
        segundos = 0
    
    return graus, minutos, segundos


def criar_dicionario(angulos_str):
    dicionario_angulos = {}
    for angulo_str in angulos_str:
        tupla_angulo = converter_para_graus_minutos_segundos(angulo_str)
        dicionario_angulos[angulo_str] = tupla_angulo
    return dicionario_angulos

def encontrar_maior_menor_angulo(dicionario_angulos):
    angulos = list(dicionario_angulos.values())
    maior_angulo = max(angulos)
    menor_angulo = min(angulos)
    return maior_angulo, menor_angulo

angulos_str = ler_angulos()
dicionario_angulos = criar_dicionario(angulos_str)
maior_angulo, menor_angulo = encontrar_maior_menor_angulo(dicionario_angulos)

print("Dicionário de ângulos:")
for chave, valor in dicionario_angulos.items():
    print(f"{chave}: {valor}")

print(f"\nMaior ângulo: {maior_angulo[0]}g{maior_angulo[1]}m{maior_angulo[2]}s")
print(f"Menor ângulo: {menor_angulo[0]}g{menor_angulo[1]}m{menor_angulo[2]}s")
