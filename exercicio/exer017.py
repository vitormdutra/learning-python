from math import hypot

cateto1 = float(input("Digite o numero do primerio cateto: "))
cateto2 = float(input("Digite o numero do segundo cateto: "))
hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** (1/2)
print("A hipotenusa vai medir {:.2f}".format(hipotenusa))

hipotenusa2 = hypot(cateto1,cateto2)
print("A hipotenusa vai medir {:.2f}".format(hipotenusa2))
