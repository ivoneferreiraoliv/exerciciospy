numeroDoEmpregado = int(input('Digite o número do empregado: '))
mesesDeTrabalho = int(input('Digite o número de meses de trabalho: '))
maisRecente = numeroDoEmpregado
maisAntigo = numeroDoEmpregado
while numeroDoEmpregado != 0 and mesesDeTrabalho != 0:
    if mesesDeTrabalho > maisRecente:
        maisRecente = numeroDoEmpregado
    if mesesDeTrabalho < maisAntigo:
        maisAntigo = numeroDoEmpregado
    numeroDoEmpregado = int(input('Digite o número do empregado: '))
    mesesDeTrabalho = int(input('Digite o número de meses de trabalho: '))
print('O empregado mais recente é o {} e o mais antigo é o {}'.format(maisRecente, maisAntigo))
print()

