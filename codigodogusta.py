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
  arquivo = open('aluno.txt','w')
  for i in range(2):
    a = aluno()
    a.ra = input('informe seu RA iniciado em 1: ')
    a.nome = input('informe seu nome: ')
    a.p1 = float(input('informe sua nota p1: '))
    a.p2 = float(input('informe sua nota p2: '))
    a.endereco.rua = input('informe sua rua: ')
    a.endereco.numero = int(input('N°: '))
    vet_cadastrar.append(a)
    arquivo.write(f'{a.ra},{a.nome},{a.p1:.2f},{a.p2:.2f},{a.endereco.rua},{a.endereco.numero}\n')
  arquivo.close()
  return vet_cadastrar

def media_ra(vet_cadastrar):
  ra_pesquisado = input('Insira o RA do aluno que deseja calcular a média: ')
  achei = False
  i = 0
  for i in range(len(vet_cadastrar)):
    if ra_pesquisado == vet_cadastrar[i].ra:
      achei = True
      if achei == True:
        print('RA encontrado.')
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
  arquivo.write(str(vet_cadastrar))
  arquivo.close

def apresentar_arq(vet_cadastrar):
  #PROF N CONSEGUI FAZER ESSE, N SEI PQ TA DANDO ERRO, MAS O RESTO TA TD OK!!
  arquivo = open('aluno.txt', 'r')
  print('')
  print('Apresentação dos dados do arquivo')
  print('')
  for linha in arquivo.readlines():
    ra,nome,p1,p2,rua,numero = linha.strip().split(",") 
    print('ra \t nome \t p1 \t p2 \t rua \t numero')
    print(ra,'\t\t',nome,'\t\t',p1,'\t\t',p2,'\t\t',rua,'\t\t',numero)
  arquivo.close()


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