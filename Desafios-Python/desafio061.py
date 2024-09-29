print("="*30)
print("\033[7:30:45m10 TERMOS DE UMA PA - (WHILE)\033[m")
print("="*30)
primeiro = int(input("Digite o rimeiro termo: "))
r = int(input("Digite a razão da progressão: "))
termo = primeiro
cont = 10
while cont > 1:
    print(termo, end=" -> ")
    termo += r
    cont-=1
print('FIM!')