import random
from time import sleep

computador = [0,1,2,3,4,5]
escolha = random.choice(computador)
print("-=-" * 20)
print("Vou pensar em um numero entre 0 e 5. Tente advinhar...")
print("-=-" * 20)
jogador = int(input("Em qual numero eu pensei? "))
print("PROCESSANDO...")
sleep(3)
if jogador == escolha:
    print("Numero escolhido foi {}".format(escolha))
    print("Acertou")
else:
    print("Numero escolhido foi {}".format(escolha))
    print("Errou")
