def bem_vindo():
    print("Bem Vindo!")


def entrada(texto):
    return int(input(texto))


def somar(numero1,numero2):
    resultado = numero1 + numero2
    return resultado



n1 = entrada ("digite um número: \n")
n2 = entrada ("digite outro número: \n")


resultado = somar (n1,n2)

print (resultado)



