tentativas = 7
palavraSecreta = str ("abelha")
while (tentativas > 0):
    chute = str (input("Digite uma palavra: \n"))
    if chute == "abelha":
        print("Você acertou!")
        break
    else:
        print("Você errou...")
    tentativas = tentativas - 1