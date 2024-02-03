dia = float(input("Quantos dias o carro foi alugado: "))
km = float(input("Quantos KM foram percorridos? "))
total = (dia * 60) + (km * 0.15)
print("O total a pagar eh de R${:.2f}".format(total))
