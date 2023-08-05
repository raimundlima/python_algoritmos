lista_de_numeros = range(3)
soma = 0 
for numero in lista_de_numeros:
    nota = float(input(f"digite a nota {numero}:\n"))
    soma+= nota

media = soma /len(lista_de_numeros)

print(f"Media:{media}")