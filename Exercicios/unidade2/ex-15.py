resultadoEnquete = [0, 0, 0, 0, 0, 0]
total = 0
print("Qual o melhor Sistema Operacional para uso em servidores?")
print("As possíveis respostas são:")
print("1- Windows Server")
print("2- Unix")
print("3- Linux")
print("4- Netware")
print("5- Mac OS")
print("6- Outro")
resposta = int(input("Digite sua resposta: "))
while resposta != 0:
    if resposta >= 1 and resposta <= 6:
        resultadoEnquete[resposta - 1] += 1
        total += 1
    else:
        print("Resposta inválida!")
    resposta = int(input("Digite sua resposta: "))
print("Sistema Operacional     Votos   %")
print("-------------------     -----   ---")
print(f"Windows Server           {resultadoEnquete[0]}   {resultadoEnquete[0] / total * 100:.0f}%")
print(f"Unix                     {resultadoEnquete[1]}   {resultadoEnquete[1] / total * 100:.0f}%")
print(f"Linux                    {resultadoEnquete[2]}   {resultadoEnquete[2] / total * 100:.0f}%")
print(f"Netware                  {resultadoEnquete[3]}   {resultadoEnquete[3] / total * 100:.0f}%")
print(f"Mac OS                   {resultadoEnquete[4]}   {resultadoEnquete[4] / total * 100:.0f}%")
print(f"Outro                    {resultadoEnquete[5]}   {resultadoEnquete[5] / total * 100:.0f}%")
print("-------------------     -----   ---")
print(f"Total                    {total}")
maior = 0
for i in range(1, 6):
    if resultadoEnquete[i] > resultadoEnquete[maior]:
        maior = i
print(f"O Sistema Operacional mais votado foi o {maior + 1}, com {resultadoEnquete[maior]} votos, correspondendo a {resultadoEnquete[maior] / total * 100:.0f}% dos votos.")
print("Fim do programa!")

