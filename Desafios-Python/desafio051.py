print('='*30)
print('10 PRIMEIROS TERMOS DE UMA PA!')
print('='*30)
n = int(input('Primeiro termo: '))
r =int(input('Razão: '))
decimo = n + ( 10 - 1 ) * r #Formúla PA, senão não contaria os décimos termos
for c in range(n, decimo, r):
    print(f'{c}', end=' -> ' )
print('\033[32mFIM\033[m')
