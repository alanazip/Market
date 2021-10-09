numeroSecreto = 12
tentativas = 3
rodada = 1
while (tentativas > 0):
    print("Tentativa {} de {}".format(rodada, tentativas))
    chute = int (input('Digite um número: \n'))
    print('Você digitou o número {}'.format(chute))
    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto
    if(acertou):
        print('Você acertou!')
        break
    elif(maior):
        print('Você errou! O seu chute foi maior que o numero secreto.')
    elif(menor):
        print('Você errou! Seu chute foi menor que o numero secreto.')
    tentativas = tentativas - 1
print("Fim de Jogo.")