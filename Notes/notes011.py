n = 0 #Tem que definir um valor incial para quê ele possa começar
while n != 0:
    n = int(input("Escreva um número : "))
print("Fim")
r = "S" #Ele não finaliza devido as aspas
while r == "S":
    number = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [N/S] ")).upper()
print("Até o próximo!")

