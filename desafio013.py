"""
 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario = input('Informe o seu salário:')
salario = salario.replace('.','')
salario = float(salario.replace(',','.'))
desc = salario + (salario * 0.15)
print('De acordo com o reajuste salarial, com 15% de aumento, o seu novo salário é R${:.2f}' .format(desc))

#Aplicação com menos variáveis
salario = input('Informe o seu salário:')
salario = salario.replace('.','')
salario = float(salario.replace(',','.'))
print(f'De acordo com o reajuste salarial, com 15% de aumento, o seu novo salário é R${salario + (salario * 0.15):.2f}')

