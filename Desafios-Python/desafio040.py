nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota + nota2) / 2
if media < 5:
    print(f'Sua média foi {media}|\033[31mREPROVADO\033[m')
elif media == 5 or media < 6.9:
    print(f'Sua média foi {media}|\033[34mRECUPERAÇÃO\033[m')
else:
    print(f'Sua média foi {media}|\033[32mAPROVADO\033[m')
#Outra alternativa
# elif media >= 7:
