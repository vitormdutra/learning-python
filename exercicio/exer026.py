text = str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes na frase".format((text.count('A'))))
print("A primeira letra A aparece na posicao {}".format(text.find('A')+1))