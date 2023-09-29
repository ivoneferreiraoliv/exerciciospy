idade = []
opiniao = []
soma_idade = 0
media_idade = 0
quantidade_regular = 0
quantidade_bom = 0
quantidade_otimo = 0
porcentagem_bom = 0

for i in range(15):
    idade.append(int(input('Digite a idade: ')))
    opiniao.append(int(input('Digite a opinião: ')))
    soma_idade += idade[i]
    if opiniao[i] == 1:
        quantidade_regular += 1
    elif opiniao[i] == 2:
        quantidade_bom += 1
    elif opiniao[i] == 3:
        quantidade_otimo += 1
media_idade = soma_idade / 15
porcentagem_bom = quantidade_bom / 15 * 100
print(f'A média das idades das pessoas que responderam ótimo é {media_idade:.2f}')
print(f'A quantidade de pessoas que responderam regular é {quantidade_regular}')
print(f'A porcentagem de pessoas que responderam bom entre todos os espectadores analisados é {porcentagem_bom:.2f}%')

