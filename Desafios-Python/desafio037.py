num = int(input('Digite um número inteiro:'))
print('Escolha alguma das opções abaixo:\n'
      '[ 1 ] converter para BINARIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print(f'{num} convertido para BINARIO é {bin(num[2:])}.')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é {oct(num[2:])}.')
else:
    print(f'{num} convertido para HEXADECIMAL é {hex(num[2:])}.')
