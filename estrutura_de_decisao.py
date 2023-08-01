nota1 = float(input("Digite a sua nota 1:\n"))
nota2 = float(input("Digite a sua nota 2:\n"))

media = (nota1 + nota2) /2

aprovado = media >= 7

if aprovado:
    print (f"Parabéns! Você foi aprovado com a média {media}! :D")

else:
    print (f"Se fu! foi reprovado ehehehe com a média {media}")