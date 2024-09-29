one = int(input("Primeiro valor: "))
two = int(input("Segundo valor: "))
option = 0
while option != 5:
    print('-'*15)
    print('[ 1 ] Somar\n'
          '[ 2 ] Multiplicar\n'
          '[ 3 ] Maior\n'
          '[ 4 ] Novos números\n'
          '[ 5 ] Sair do programa')
    print('-' * 15)
    option = int(input("Qual é a sua opção? "))
    if option == 1:
        print(f'O resultado da soma de {one} + {two} = {one+two}')
    elif option == 2:
        print(f'O resultado de {one} x {two} = {one*two}')
    elif option == 3:
        print(f'O maior valor entre os números {one} e {two} é {max(one,two)}')
    elif option == 4:
        one = int(input("Primeiro valor: "))
        two = int(input("Segundo valor: "))
    elif option == 5:
        print('Finalizando...')
    else:
        print("\033[31mOpção Inválida!\033[m")
print("\033[36mFim do programa\033[m")