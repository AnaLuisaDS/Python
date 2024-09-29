num = int(input('Digite um número: '))
s = 0

for n in range(1, num+1):
    if num % n == 0 and num != 1:
        print(f'\033[34m{n}\033[0m', end=' ')
        s = s + 1
    else:
        print(f'\033[0m{n}\033[0m', end=' ')
if s == 2:
    print(f'\nO valor {num} é um número \033[36mPRIMO!\033[m')
else:
    print(f'\nO valor {num} \033[31mNÃO\033[m '
          f'é um número primo!')