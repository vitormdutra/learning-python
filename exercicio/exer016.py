from math import trunc

numero = float(input("Digite um numero quebrado: "))
print("O valor digitado foi {} e sua porcao inteira eh {}".format(numero, trunc(numero)))

#sem import math
print("O valor digitado foi {} e sua porcao inteira eh {}".format(numero, int(numero)))