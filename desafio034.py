salario = float(input('Digite o salário do funcionário:'))
if salario > 1250:
    aumento =  salario + (salario * 0.10)
    print(f'De acordo com o reajuste, o novo salário é de R${aumento :.2f}')
else:
    aumento = salario + (salario * 0.15)
    print(f'De acordo com o reajuste, o novo novo salário é de R${aumento :.2f}')
