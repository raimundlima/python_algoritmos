nota1 = float(input("Digite a sua nota 1:\n"))
nota_invalida = nota1 < 0 or nota1 > 10
while nota_invalida:
    print("A nota de ser entre 0 e 10")
    nota1 = float(input("Digite a sua nota 1:\n"))
    nota_invalida = nota1 < 0 or nota1 > 10

nota2 = float(input("Digite a sua nota 2:\n"))
nota_invalida = nota2 < 0 or nota2 > 10
while nota_invalida:
    print("A nota de ser entre 0 e 10")
    nota2 = float(input("Digite a sua nota 2:\n"))
    nota_invalida = nota2 < 0 or nota2 > 10

nota3 = float(input("Digite a sua nota 3:\n"))
nota_invalida = nota3 < 0 or nota3 > 10
while nota_invalida:
    print("A nota de ser entre 0 e 10")
    nota3 = float(input("Digite a sua nota 3:\n"))
    nota_invalida = nota3 < 0 or nota3 > 10

media = (nota1 * 4 + nota2 * 5 + nota3 * 6) /15



aprovado = media >= 7
recuperacao = media > 3 and media < 7
reprovado = media < 3




elif aprovado:
    print (f"Parabéns! Você foi APROVADO com a média {media}! :D")

elif recuperacao:
    print (f"Quase! você está em RECUPERAÇÃO com a média {media}")

elif reprovado:
    print (f"que pena! você está REPROVADO com a média {media}")