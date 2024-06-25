num_one = int(input('Escreva o primeiro valor:'))
num_two = int(input('Escreva o segundo valor:'))
num_three = int(input('Escreva o terceiro valor:'))
maior = num_one
if num_two > num_one and num_two > num_three:
    maior = num_two
if num_three > num_one and num_three > num_two:
    maior = num_three
#Encontrando o menor número
menor = num_one
if num_two < num_one and num_two < num_three:
    menor = num_two
if num_three < num_two and num_three < num_one:
    menor = num_three
print(f'O maior valor é {maior}.')
print(f'O menor valor é {menor}.')

#Usando a propriedade max
num_one = int(input('Escreva o primeiro valor:'))
num_two = int(input('Escreva o segundo valor:'))
num_three = int(input('Escreva o terceiro valor:'))
maior = max(num_one, num_two, num_three)
menor = min(num_one, num_two, num_three)
print(f'O maior valor é {maior}.')
print(f'O menor valor é {menor}.')
