
print('\33[3:30:42m Testando cores\33[m')

nome = input('Qual o seu nome? ').strip()
print('Olá {}{}{}, seja bem-vindo(a)!' .format('\033[7:35m',nome, '\033[m'))

name = input('Qual é o seu nome completo?').strip().upper()
name_end = name.count('A')
color = {'fechar': '\033[m',
         'azul':'\033[4:34m',
         'amarelo':'\033[7:33m',}
print('Tem {} {} letras A{} em seu nome! '.format(color['azul'], name_end, color['fechar']))

#Explicação exercício 038
#Se num for maior que num1, imprime que o primeiro valor é maior e o segundo é menor.
#Se num1 for maior que num, imprime que o segundo valor é maior e o primeiro é menor.
#Se forem iguais, imprime que os valores são iguais.