""" - Crie um programa que leia dois números e mostre a soma entre eles. """

number_one = int(input('Digite um número (Ex: 24):'))
number_two = int(input('Digite outro número (Ex: 88):'))
s1 = number_one + number_two
print('A soma entre {} e {}, vale {}' .format(number_one, number_two, s1))


#Não pode haver vírgula, pois o float não identifica.
#Sendo assim, por preocaução converter através do .replace()

number_three = input('Digite um número (Ex: 4,33 ):')
number_three = number_three.replace(',', '.')    #Primeiro fazer essa troca.
number_three = float(number_three)                           #Depois atribuir o valor necessário.
number_four = input('Digite outro número (Ex: 7,20 ):')
number_four = float(number_four.replace(',','.'))  #Ou realizar uma aplicação mais otimizada.
s2 = number_three + number_four
print(f'A soma entre {number_three:.2f} e {number_four:.2f}, vale {s2:.2f}')

