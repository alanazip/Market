produto = []
numero = []
preco = []
print('''<<< Cadastro de produtos - digite exit para sair >>>''')
produto.append(str (input("Nome do Produto: \n")))
numero.append((int(input("Número de série: \n"))))
preco.append((float(input("Valor R$: \n"))))
if produto or numero or preco == "exit":
    print(produto,numero,preco)
else:
    for i in range(1,999):
        print('''<<< Cadastro de produtos - digite exit para sair >>>''')
        produto.append(str (input("Nome do Produto: \n")))
        numero.append((int(input("Número de série: \n"))))
        preco.append((float(input("Valor R$: \n"))))
