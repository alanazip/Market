chute = int (input("Digite um numero: \n"))
numero_secreto = 20
if (numero_secreto	==	chute):
    print('Você	acertou!')
elif (chute	> numero_secreto):
    print('Você	errou! O seu	chute	foi	maior	que	o	número secreto')
elif (chute	<	numero_secreto):
    print('Você	errou! O seu	chute	foi	menor	que	o	número	secreto')