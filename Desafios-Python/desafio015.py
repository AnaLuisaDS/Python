"""
 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
    e a quantidade de dias pelos quais ele foi alugado.
    Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

time = int(input('Por quantos dias o carro foi alugado?'))
distance = input('Quantos quilometros o carro percorreu?')
distance = float(distance.replace('.',''))
amount = (time * 60) + (distance * 0.15)
print('O valor a ser pago é de R${:.2f}' .format(amount))

#Programa que informará quantos centímetros o quadro ocupurá na parede.

lag = float(input('Qual é a largura, em centímentros, do seu quadro?'))
alt = float(input('Qual é a altura, em centímetros, do seu quadro?'))
print(f'O espaço que o seu quadro ocupará na parede sera de {(lag * alt) :.2f} cm².')
