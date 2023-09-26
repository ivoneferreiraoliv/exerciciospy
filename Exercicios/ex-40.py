input('Responda as perguntas com "sim" ou "não"')
pergunta1 = input('Telefonou para a vítima? ')
pergunta2 = input('Esteve no local do crime? ')
pergunta3 = input('Mora perto da vítima? ')
pergunta4 = input('Devia para a vítima? ')
pergunta5 = input('Já trabalhou com a vítima? ')
respostas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]
respostasPositivas = 0
for resposta in respostas:
    if resposta == 'sim':
        respostasPositivas += 1
if respostasPositivas == 2:
    print('Você é suspeito')
elif respostasPositivas >= 3 and respostasPositivas <= 4:
    print('Você é cúmplice')
elif respostasPositivas == 5:
    print('Você é o assassino')
else:
    print('Você é inocente')