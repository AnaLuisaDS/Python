from time import sleep
preco = input('Digite o preço do produto escolhido: ').replace(',' , '.')
preco1 = float(preco)
print('Aguarde alguns segundos . . .')
sleep(3)
print('Escolha sua forma de pagamento: \n'
      '[ 1 ] À VISTA DINHEIRO OU CHEQUE\n'
      '[ 2 ] À VISTA NO CARTÃO\n'
      '[ 3 ] EM ATÉ 2x NO CARTÃO\n'
      '[ 4 ] 3x OU MAIS NO CARTÃO')
esc = int(input('Digite sua escolha: '))
if esc == 1:
    print(f'O produto que custava R${preco1:.2f}, sairá por R$\033[35m{preco1 - (preco1 * 0.10):.2f}\033[m. ')
elif esc == 2:
    print(f'O produto que custava R${preco1} sairá por R$\033[35m{preco1 - (preco1 * 0.05 ):.2f}\033[m.')
elif esc == 3:
    print(f'O valor original R${preco1:.2f} se mantém! ')
elif esc == 4:
    print(f'Aconteceu um acréscimo de 20% de juros | R$\033[35m{preco1 + (preco1 * 0.20):.2f}\033[m.')
else:
    print('\033[31mOPÇÃO INVÁLIDA!\033[m Tente novamente.')