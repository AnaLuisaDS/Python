"""
 - Faça um programa que leia a largura e a altura de uma parede em metros.
 Calcule a sua área e a quantidade de tinta necessária para pintá-la,
 sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

# 1L(Tinta) = 2 m²

lag = float(input('Infomer, em metros, a largura da parede:'))
alt = float(input('Informe, em metros, a altura da parede:'))
a = lag * alt
l = a / 2
print('De acordo com os dados fornecidos, a área da parede é {:.2f}m²\n'
'e será necessário {}L de tinta para pinta-lá.' .format(a, l))

#Aplicação com menos variáveis

lag = float(input('Informe, em metros, a largura da parede:'))
alt = float(input('Informe, em metros, a altura da parede:'))
print(f'De acordo com os dados fornecidos,  a área é de {lag * alt :.2f}m², \n'
f' e será necessário {(lag * alt)/2 :.1f}L de tinta para pinta-lá. ')