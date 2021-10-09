cadastro = 3
while (cadastro > 1): #aparece só 2
    nome = input("Digite seu nome: \n")
    idade = int(input("Digite sua idade: \n"))
    cadastro = cadastro - 1 #é sempre menos (-)
    if idade < 18:
        print("***Você é menor de idade***")
    else:
        print("Você é maior de idade ( ͡° ͜ʖ ͡°)")

