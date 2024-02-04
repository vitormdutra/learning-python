d = float(input("Qual a distancia da viagem? "))
if d > 200:
    p = d * 0.45
    print("O valor da sua viagem eh de R${}".format(p))
else:
    p = d * 0.50
    print("O valor da sua viagem eh de R${}".format(p))
