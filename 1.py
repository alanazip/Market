class Cadastros():
    nome = []
def menu():
    print("1. Cadastrar alunos digite 1")
    print("2. Calcular média de um aluno por ra digite 2")
    print("3. Calcular média de todos os alunos digite 3")
    print("4. Visualizar todos os alunos dados digite 4")
    print("5. Armazenar todos os campos em um arquivo digite 5")
    print("6. Apresentar o conteúdo do arquivo digite 6")
    print("7. Sair digite 7")
    resposta = int(input("Digite uma das opções acima -> "))
    return resposta
def calculos():
    resposta = menu()
    if resposta == 1:  
        cadastrar_aluno()
    elif  resposta == 2:
        calcular_media_ra() 
    elif resposta == 3:
        calcular_media_todos()
    elif  resposta == 4:
        visualizar_dados()       
    elif  resposta == 5:
        armazenar()
    elif  resposta == 6:
        conteudo_arquivo()
    elif resposta == 7:
        quit();  
    else:
        print("Opção não existente! \nPor favor digite somente numeros entre 1 a 7 ")
        calculos()
def main():
    menu()

main()