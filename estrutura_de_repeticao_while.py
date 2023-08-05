contador = 1
resposta_nao_for_sim = True
while resposta_nao_for_sim:
    resposta = input(f"Você gosta de mim?\n Tentativa {contador}\n")
    resposta_nao_for_sim = resposta != "sim"
    if resposta_nao_for_sim:
        print("que pena, repita novamente")
    
    else:
        print("Parabens, você é um otimo amigo")

    contador +=1 

