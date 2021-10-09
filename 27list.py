lista = [1, 2, 3, 4, 5]
print(lista[-1])  #ordem contraria
# =5
print(lista[-2])
# =4
lista = list('python')
print(lista)
#['p', 'y', 't', 'h', 'o', 'n']

meses = ['Janeiro',	'Fevereiro','Março','Abril','Maio','Junho','Julho',	'Agosto','Setembro'
,'Outubro',	'Novembro',	'Dezembro']
n =	1
while(n	<	4):
    mes	=	int(input("Escolha	um	mês	(1-12):	"))
    if	1	<=	mes	<	13:
        print('O mês é	{}'.format(meses[mes-1]))
    else:
        break
n += 1

