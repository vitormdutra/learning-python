n = float(input("Digite o nume que deseja saber da tabuada: "))

for i in range(1,11):
    print("{} x {:2} = {:.0f}".format(n, i, n*i))
    i + 1
