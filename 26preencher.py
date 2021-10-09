nome = 'Alana Souza'
nomeFormat = '{:@>50}'.format(nome) #completa com @ ate oq faltou pra dar 50
print(nomeFormat)
cebola = 'no omelete nao'
omelete = 'com salsa e cebolinha'
omeletePronto = '{0:$^50} {1:#^50}'.format(cebola,omelete)
print(omeletePronto)
# o espaço entre 50} {1 aparece no codigo
# o sinal de ^ serve pra deixar a palavra no centro e dividir os caracteres que precisa preencher
# o 0 e o 1 é a posição onde ficam as strings

nome = nome.ljust(30, '%') #ljust serve para justificar a str e preencher com o numero que eu pedi
print(nome)
milho = 'Ervilha'
print(milho.lower()) #tudo minusculo
print(milho.upper()) #tudo maiusculo
print(milho.title()) #primeiras letras maiusculas
