num = float(input('Digite o primeiro valor:'))
num1 = float(input('Digite o segundo valor:'))
maior = max(num, num1)
menor = min(num, num1)
if num > num1:
    print(f'O PRIMEIRO valor é maior: \033[4:34m {maior:.2f}\033[m')
    print(f'O SEGUNDO valor é menor: \033[4:35m {menor:.2f}\033[m')
elif num1 > num:
    print(f'O SEGUNDO valor é maior: \033[4:34m {maior:.2f}\033[m')
    print(f'O PRIMEIRO valor é menor: \033[4:35m {menor:.2f}\033[m')
else:
    print(f'Opa! Não há valores \033[4:31m diferentes.\033[m')
