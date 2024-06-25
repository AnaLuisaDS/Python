#Desafio 008 - Conversor de Medidas

metros = float(input('Digite quanto metros há na área desejada: '))
dm = metros * 10
cm = metros * 100
mm = metros * 1000
dam = metros / 10
hm = metros / 100
km = metros / 1000
print('De acordo com as informações fornecidas, é uma área que corresponde a: \n'
'{} decímetros, {} centímetros,\n'
'{} milimetros, {} decâmetros,\n'
'{:.3f} hectômetro e a {:.3f} quilometros.' .format( dm, cm, mm, dam, hm, km))

#aplicação com menos variáveis

metros = float(input('Digite quanto metros há na área desejada:'))
print(f'De acordo com as informações fornecidas, é uma área que corresponde a :\n'
f'{metros*10} decímetros,{metros*100:.4f} centímetros,\n'
f'{metros*1000} milimetros, {metros/10} decâmetros,\n'
f' {metros/100 :.3f} hectômetro e a {metros/1000:.3f} quilometros.')