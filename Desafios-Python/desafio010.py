""" - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar."""

real = input('Quantos reais você tem na carteira?')
real = real.replace('.', '')   #Atribuições em prol do UX
real = float(real.replace(',', '.'))
dolar = real / 5.29
print('Atualmente, você retém de US${:.2f}' .format(dolar))

#Aplicação com menos variáveis
real = input('Quantos reais você tem na carteira?')
real = real.replace('.' , '')
real = float(real.replace(',', '.'))  #Atribuição em prol do UX.
print(f'Atulamente, você retém de US$ {real / 5.29 :.2f}')
