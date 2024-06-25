
print('\33[3:30:42m Testando cores\33[m')

nome = input('Qual o seu nome? ').strip()
print('Olá {}{}{}, seja bem-vindo(a)!' .format('\033[7:35m',nome, '\033[m'))

name = input('Qual é o seu nome completo?').strip().upper()
name_end = name.count('A')
color = {'fechar': '\033[m',
         'azul':'\033[4:34m',
         'amarelo':'\033[7:33m',}
print('Tem {} {} letras A{} em seu nome! '.format(color['azul'], name_end, color['fechar']))
