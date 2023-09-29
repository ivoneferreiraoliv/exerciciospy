# 73.	Faça um programa para validar o login e a senha de um usuário. Caso o usuário informe algum valor inválido informar o erro e pedir novamente os dados. A leitura dos dados deve ser encerrada quando o usuário digitar 3 vezes um valor inválido (login ou senha). Considere o login válido como "kezia" e a senha como "123".
login = input("Digite o login: ")
senha = input("Digite a senha: ")
tentativas = 0
while login != "kezia" or senha != "123":
    print("Login ou senha inválidos!")
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    tentativas += 1
    if tentativas == 3:
        break
if tentativas < 3:
    print("Login e senha válidos!")
else:
    print("Número máximo de tentativas excedido!")

