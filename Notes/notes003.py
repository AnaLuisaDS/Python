n1 = int(input('Digite um número:'))
n2 = int(input('Digite novamente um número:'))
s = n1+n2
print('A soma entre {} e {} é {}' .format(n1, n2, s))
print('A soma vale {}' .format(s))
print('A soma entre', n1, 'e', n2, 'é', n1+n2)
print('A soma é', n1+n2)
print('A soma é', s)

print(type(n1))
print(type(s))

n3 = int(input('Digite um número (Ex: 24):'))
n4 = int(input('Digite outro número (Ex: 88):'))
s1 = n3+n4
print('A soma entre {} e {}, vale {}' .format(n3, n4, s1))

n5 = float(input('Digite um número (Ex: 4.30 )'))
n6 = float(input('Digite outro número (Ex: 7.20 ):'))
s3 = n5+n6
print('A soma entre {} e {}, vale {}' . format(n5, n6, s3))

# n = bool(input(''))
#print(n) Caso não digite nada dará false
#Sempre que estiver chamando uma variável tem que colocar vírgula


box = input('Digite algo (Pode ser num ou letra):')

print('Seu tipo primitivo', box.type())
print('É um número?', box.isnumeric())
print('É uma letra?', box.isalpha())
print('É um alfanúmerico?', box.isalnum())
print('Está em maiúsculo?', box.isupper())
print('Está em minúsculo?', box.islower())
print('Contém espaços?', box.isspace())
print('Está capitalizada?', box.istitle())

n = float(bool(input('Digite uma letra:')))
print(n)





