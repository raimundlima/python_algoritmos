# crie uma função que retorne o valor de imposto de previdencia social de um dado salario 


def calcular_imposto_previdencia(salario):
    if salario <= 1320:
        imposto = salario * 0.075
    elif salario <= 2571.29:
        imposto = (salario - 1320.01) * 0.09 + 99
    elif salario <= 3856.94:
        imposto = (salario - 2571.30) * 0.12 + 211.61
    elif salario <= 7507.79:
        imposto = (salario - 3856.95) * 0.14 + 365.89

    else:
        imposto = 876.97
    return imposto

salario = float(input("Digite o salário: "))
imposto_previdencia = calcular_imposto_previdencia(salario)
print(f"O valor do imposto de previdência social é: R${imposto_previdencia:.2f}")