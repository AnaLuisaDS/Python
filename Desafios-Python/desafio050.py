soma = 0
count = 0
for n in range(1, 7):
    num = int(input(f'Digite o {n}° valor: '))
    if num % 2 == 0:
        soma += num
        count += 1 #Cada vez que um número par é encontrado, a variável count é incrementada em 1.
print(f'Tem {count} números pares e a soma deles é {soma}')
