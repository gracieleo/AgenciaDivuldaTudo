# Calculadora/Cadastro de anuncios
# Agencia Divulga Tudo
# Graciele de Oliveira  02/07/2021

# inicia variaveis
total = investimentodia = cont = 0

# dados de inicio
print("Número de visualizações originais: ")
numVisualizaOriginal = 30
print(numVisualizaOriginal)
print("Total investimento: R$ ")
investimento = 100
print(investimento)
print("Novo número de visualizações compartilhadas: ")
numNovaVisulizacao = 40
print(numNovaVisulizacao)


originalTotal = numVisualizaOriginal * 1
totalCompartilhado = numNovaVisulizacao * 3


projecao = originalTotal * investimento * totalCompartilhado
print("A projeção máxima de visualizações é de : ")
print(projecao)

print("Número máximo de cliques: ")
maxClique= (projecao / 100) * 12
print(maxClique)

print("Número máximo de visualizações: ")
maxVisualizacao = originalTotal + totalCompartilhado
print(maxVisualizacao)

print("Número máximo de compartilhamentos:")
maxCompartilhado = (maxVisualizacao /20) * 3
print(maxCompartilhado)


######################## CADASTRO DE ANUNCIOS ##################################

print(" *** Cadastro de Anuncios ***")
while True:
    nome = str(input('Nome: '))
    cliente = str(input('Cliente: '))
    datainicio= int(input('Data de inicio: '))
    datafim= int(input('Data fim: '))
    investimentodia= float(input('Total investido por dia: R$ '))
    total=investimentodia
    cont+=1

    resp=" "
    while resp not in 'SN':
        resp = str(input("Deseja cadastrar mais um anuncio? [S/N]" + " ")).upper()[0]
    if resp =="S":
        print("Informe os dados de cadastro")
        nome = str(input('Nome:'))
        cliente = str(input('Cliente:'))
        datainicio = int(input('Data de inicio:'))
        datafim = int(input('Data fim:'))
        investimentodia = int(input('Total investido por dia:'))

    if resp == 'N':
        print("Obrigada.")
        break

########################## RELATORIO #####################################

    print("*** Relatório *** ")
    print("Valor total investido: ")
    print(total)

    print("Quantidade máxima de visualizações: ")
    print(maxVisualizacao)

    print("Quantidade máxima de cliques: ")
    print(maxClique)

    print("Quantidade máxima de compartilhamentos: ")
    print(maxCompartilhado)









