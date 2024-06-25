"""
- Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.
"""
pp = input('Digite o valor do produto:')
pp = float(pp.replace(',' , '.'))
desc = pp * 0.05             #Ou, desc = pp - (pp * 0.05)
print(f'O produto que custava R${pp:.2f}, está saindo por R${pp-desc:.2f} com 5% de desconto!')

#Alternativa com menos variáveis
pp = input('Digite o valor do produto:')
pp = float(pp.replace(',' , '.'))
print(f'O produto que custava R${pp:.2f}, está saindo por R${pp - (pp * 0.05):.2f} com 5% de desconto!')
