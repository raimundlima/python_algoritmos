nota1 = float(input("Digite a sua nota 1:\n"))
nota2 = float(input("Digite a sua nota 2:\n"))
nota3 = float(input("Digite a sua nota 3:\n"))

media = (nota1 * 4 + nota2 * 5 + nota3 * 6) /15

media_invalida = media <0 or media> 10
aprovado = media >= 7
recuperacao = media > 3 and media < 7
reprovado = media < 3


if media_invalida:
    print(f"media inválida ->{media}")

elif aprovado:
    print (f"Parabéns! Você foi APROVADO com a média {media}! :D")

elif recuperacao:
    print (f"Quase! você está em RECUPERAÇÃO com a média {media}")

elif reprovado:
    print (f"que pena! você está REPROVADO com a média {media}")