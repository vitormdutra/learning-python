velocida = float(input("Qual velocidade esta o carro? "))
multa = (velocida - 80) * 7

if velocida > 80:
    print("Voce foi multado! estava a {}km a cimado do limite de 80km".format(velocida - 80))
    print("Valor da multa: R${:.2f}".format(multa))
else:
    print("Voce esta no limite de velocidade, dirija com cuidado.")