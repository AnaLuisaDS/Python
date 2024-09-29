s = 0
c = 0
for num in range(3, 500, 6):
    print(num, end=' ')
    s += num
    c += 1
print()
print(f'A soma de todos os {c} valores é {s}.')