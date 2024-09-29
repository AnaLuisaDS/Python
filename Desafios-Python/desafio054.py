from datetime import date
c = 0
co = 0
for year in range(1, 8):
    num = int(input(f'Em que ano a {year}° pessoa nasceu? '))
    idade = date.today().year - num
    if idade < 18:
        c = c + 1
    else:
        co = co + 1
print('='*80)
print(f'Quantidade de pessoas maiores de 18 anos: {co}')
print(f'Quantidade de pessoas menores de 18 anos: {c}')