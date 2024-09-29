soma = 0
count = 0
oldest = 0
oldname = ''
young = float('inf') # Inicializa com infinito para garantir que qualquer idade será menor
youngname = ''
for p in range(1,5):
    print('-'*4 + f' {p}° PESSOA'+ '-'*4 )
    name = input(f'Nome: ')
    idade = int(input(f'Idade: '))
    soma += idade
    sex = input('Sexo [M/F]: ').upper()

    if sex in 'M':
        if idade > oldest:
            oldest = idade
            oldname = name
        if idade < young:
            young = idade
            youngname = name

    if idade < 20 and sex in 'Ff':
        count = count + 1
media = soma / 8

print(f'A média das idades é \033[33m{media} anos.\033[m')
print(f'\033[33m{count} mulher(es)\033[m que contêm menos de 20 anos.')
print(f'O homem mais velho tem {oldest} anos e se chama {oldname}. \n'
      f'O homem mais novo tem {young} anos e se chama {youngname}.')
