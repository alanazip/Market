class complemento:
  rua = ''
  numero = 0

class aluno:
  ra = ''
  nome = ''
  p1 = 0.0
  p2 = 0.0
  media = 0.0
  endereco = complemento()

def cadastrar():
  vet_cadastrar=[]
  for i in range(2):
    a = aluno()
    a.ra = input('informe seu RA: ')
    a.nome = input('informe seu nome: ')
    a.p1 = float(input('informe sua nota p1: '))
    a.p2 = float(input('informe sua nota p2: '))
    a.media = float(a.p1 + a.p2 / 2)
    a.endereco.rua = input('informe sua rua: ')
    a.endereco.numero = int(input('N°: '))
    vet_cadastrar.append(a)
  return vet_cadastrar

def media_ra(vet_cadastrar):
  pesq = input('Insira o RA do aluno que deseja calcular a média: ')
  achei = False
  i = 0
  for i in range(len(vet_cadastrar)):
    if pesq == vet_cadastrar[i].ra:
      achei = True
      if achei == True:
        print('RA encontrado.')
        print(vet_cadastrar[i].p1)
        print(vet_cadastrar[i].p2)
        media = (vet_cadastrar[i].p1 + vet_cadastrar[i].p2 ) / 2
        print('media: ',media)
      else:
        print('RA não encontrado.')

def media(vet_cadastrar):
  i = 0
  for i in range(len(vet_cadastrar)):
    media = (vet_cadastrar[i].p1 + vet_cadastrar[i].p2) / 2
    raa = vet_cadastrar[i].ra
    print('RA: ',raa,'media: ',media)


def visualizar(vet_cadastrar):
  for i in range(len(vet_cadastrar)):
    print('Nome:',vet_cadastrar[i].nome,'\tRA:',vet_cadastrar[i].ra,'\tNota - P1:',vet_cadastrar[i].p1,'\tNota - P2:',vet_cadastrar[i].p2,'\tRua:',vet_cadastrar[i].endereco.rua, '\tNúmero:',vet_cadastrar[i].endereco.numero)

def armazenar(vet_cadastrar):
  arquivo = open('aluno.txt','w')
  print('armazenado com sucesso')
  arquivo.write(vet_cadastrar)
  arquivo.close

def apresentar_arq(vet_cadastrar):
  arquivo = open('aluno.txt', 'r')
  print('')
  print('Apresentação dos dados dos produtos')
  print('')
  for linha in arquivo.readlines():
    ra, nome, p1, p2, = linha.strip().split(",")
    print('ra \t nome \t p1 \t p2')
    print(ra,'\t\t',nome,'\t\t',p1,'\t\t',p2)
  arquivo.close


def main():
  op = 1
  while op >= 1 and op <= 7:
    print('MENU')
    print('1. Cadastrar aluno')
    print('2. Calcular média de um aluno por ra')
    print('3. Calcular média de todos os alunos')
    print('4. Visualizar todos os alunos dados')
    print('5. Armazenar todos os campos em um arquivo')
    print('6. Apresentar o conteúdo do arquivo')
    print('7. Sair')
    op=int(input('qual opção? '))
    if op == 1:
      vet_a = cadastrar()
    elif op == 2:
      media_ra(vet_a)
    elif op == 3:
      media(vet_a)
    elif op == 4:
      visualizar(vet_a)
    elif op == 5:
      armazenar(vet_a)
    elif op == 6:
      apresentar_arq(vet_a)
    elif op == 7:
      break
main()