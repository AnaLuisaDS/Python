name = input('Qual é o seu nome?').strip().lower()
if name[0] == 'a':
    print(f'Olá {name}, seu nome é bem comum! :p')
else:
    print(f'Olá {name}, o seu nome não é tão comum! ;)')
print('Bom dia, {}!'.format(name.capitalize()))

name1 = input('Qual é o seu nome?').strip().capitalize()
if name1 == 'Hyacinth':
    print('O seu nome é igual do personagem Bridgerton! :0')
elif name1[0] in ['K', 'G', 'J', 'W', 'X']:  #IN pois está chamando várias strings
    print('O seu nome é bem raro! :)')
elif name1[:2] == 'Ch':
    print('O seu nome é MUITO raro!!! :0')
else:
    print('O seu nome é lindo!')
