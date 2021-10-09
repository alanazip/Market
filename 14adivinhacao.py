print('*****************************')
print('*    Jogo da Adivinhação    *')
print('*****************************')
numeroSecreto = 12
chute = int (input("digite um numero \n"))
print('Você digitou o número {}'.format(chute))
if(numeroSecreto == chute):
    print("Você acertou!")
else:
    print("Você errou...")