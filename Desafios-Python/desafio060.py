n = int(input("Digite um número: "))
c = n
fact = 1
print(f'{n}! = ',end="")
while c > 0:
    print(f'{c}', end="")
    print(' x ' if c > 1 else " = ", end="")
    fact *= c
    c -= 1 #Decrementar para o Loop não ficar infinito
print(fact)

