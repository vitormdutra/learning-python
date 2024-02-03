import math

angulo = float(input("Digite o angulo que voce deseja: "))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("O angulo de {} tem Seno de {:.2f}".format(angulo,seno),
      "O angulo de {} tem Cosseno de {:.2f}".format(angulo,cosseno),
      "O angulo de {} tem Tangente de {:.2f}".format(angulo,tangente))
