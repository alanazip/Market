usuario = input("Nome de usuário: \n")
senha = input("Senha: \n")
usuario.lower()
usuarioBD = 'alana'
senhaBD = '1234'

if usuarioBD == usuario and senhaBD == senha:
    print("Você está logado.")
else:
    print("Login ou senha incorretos.")
