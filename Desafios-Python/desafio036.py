from time import sleep
casa = float(input('Qual é o valor da casa?'))
salario = float(input('Qual é o sálario do comprador?'))
years = int(input('Quantos anos de financiamente?'))
pm = casa / (years * 12)   #Primeiro saber quanto vale a prestação
print(f'Para pagar uma casa de R${casa:.2f} em {years} anos, a prestação mensal ficará R${pm:.2f}')
print('Aguarde um momento...')
sleep(3)
if (salario * 0.30) >= pm:
    print('Emprestimo \033[1;32mAPROVADO!\033[m')
else:
    print('Emprestimo \033[1;31mNEGADO!\033[m')