nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:=^14}!'.format(nome))

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
pt = n1 ** n2
mult = n1 * n2
div = n1 / n2
di = n1 // n2
dr = n1 % n2
so = n1 + n2
sub = n1 - n2
rad = n1 ** (1/2)
rad2 = n2 **(1/2)

print('A potenciação entre os valores é {:.3f}, a multiplicação é {}, a divisão é {:.3f},\n'
      ' a divisão inteira é {}, a divisão de resto é {}, a soma é {}, a subtração é {}\n e a raiz quadrada do primeiro valor é {} '
      'e a do segundo é {}'.format(pt, mult, div, di, dr, so, sub, rad, rad2))

