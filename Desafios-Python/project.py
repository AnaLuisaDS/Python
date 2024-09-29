opção = print('[ 1 ] Mercúrio\n'
              '[ 2 ] Saturno\n'
              '[ 3 ] Júpiter\n'
              '[ 4 ] Marte')
escolha = int(input('Informe sua escolha: '))
print('-'*30)

idade = int(input("Digite sua idade: "))

if escolha == 1:
    print(f'Você tem {idade/0.34 :.2f} anos em \033[34mMercúrio\033[m.')
elif escolha == 2:
    print(f'Em Saturno você tem \033[34m{idade/29.46 :.2f} anos\033[m.')
elif escolha == 3:
    print(f'Você tem {idade/11.86 :.2f} anos em \033[34mJúpiter\033[m')