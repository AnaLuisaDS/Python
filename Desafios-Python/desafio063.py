num = int(input("Digite quantos termos você quer saber Finabocci:"))

cont = 3
t1 = 0
t2 = 1
t3 = t1 + t2

print(t1, end=' -> ')
print(t2, end=' -> ')
while num >= cont:
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM!')