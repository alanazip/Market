numeroSecreto = 6
tentativas = 3
for rodada in range(1, tentativas):
    print("Tentativa {} de {}".format(rodada, tentativas))

    chute = int (input("Digite seu numero: \n"))
    print("Você digitou: ", chute)

    acertou = numeroSecreto == chute
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    if (acertou):
        print("Você acertou!")
        break
    elif (maior):
        print("Você errou. O numero é maior que o número secreto")
    elif (menor):
        print("Você errou. O numero é menor que o número secreto")
print("Fim de jogo.")
