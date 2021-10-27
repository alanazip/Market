produto = []
numero = []
preco = []
print('''<<< Cadastro de produtos - digite exit para sair >>>''')
produto.append(str (input("Nome do Produto: \n")))
numero.append((int(input("Número de série: \n"))))
preco.append((float(input("Valor R$: \n"))))
if produto or numero or preco == "exit":
    print("Nome do produto",produto,"Codigo",numero,"Preço R$",preco)
else:
    for i in range(1,4):
        print('''<<< Cadastro de produtos - digite exit para sair >>>''')
        produto.append(str (input("Nome do Produto: \n")))
        numero.append((int(input("Número de série: \n"))))
        preco.append((float(input("Valor R$: \n"))))
print("Nome do produto",produto,"Codigo",numero,"Preço R$",preco)
