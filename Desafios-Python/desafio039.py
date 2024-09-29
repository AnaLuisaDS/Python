from datetime import date
birth = int(input('Ano de nascimento:'))
idade = date.today().year - birth
print(f'Você nasceu em {birth} e tem {idade} anos em { date.today().year}.')
if idade == 18:
    print('Você tem que se alistar \033[1:31mIMEDIATAMENTE!\033[m')
elif idade < 18:
    tempo = (18 - idade) + date.today().year
    print(f'Ainda faltam {18 - idade} anos.')
    print(f'Seu alistamento vai ser no ano de {tempo}')
elif idade > 18:
    print(f'Você deveria ter se alistado há \033[31m{idade - 18} anos\033[m.')
    print(f'O seu alistamento foi em \033[33m{date.today().year - (idade - 18)}\033[m . ')
