num = int(input('Digite um numero: '))

d = num * 2
t = num * 3
r = num ** (1/2)

print('O dobro do {} eh {}'.format(num, (num * 2)))
print('O triplo do {} eh {}'.format(num, (num * 3)))
print('O raiz quadrada do {} eh {:.2f}'.format(num, pow(num, (1/2))))
