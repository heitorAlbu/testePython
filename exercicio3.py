listaVendas = []
listaCategorias = [["200-299", 0],["300-399", 0],["400-499", 0],["500-599", 0],["600-699", 0],
                   ["700-799", 0],["800-899", 0],["900-999", 0], ["1000", 0]]


def calcularRemuneracao(vendas):
    remuneracao = vendas*0.09 + 200
    if (remuneracao >= 1000):
        listaCategorias[8][1] += 1
    else:
        for i in range(0, len(listaCategorias) -1):
            if(remuneracao >= int(listaCategorias[i][0][0:3]) and  remuneracao <= int(listaCategorias[i][0][4:7])):
                    listaCategorias[i][1] += 1

    return remuneracao

def abrirPrograma():
    print("----Folha de Pagamento dos funcionários----")
    print("1) Apurar resultado")
    print("2) Cadastrar vendas")
    print("")
    print("ESCOLHA : ")
    escolha = int(input())
    definirEscolha(escolha)

def definirEscolha(escolha):
    while(escolha == 1 or escolha == 2):
        if escolha == 1:
            for i in listaCategorias:
                print("faixa de remuneração : " + i[0] + " -   Nº de funcionários : " + str(i[1]))
            abrirPrograma()
        elif escolha == 2:
            print("digite o total apurado pelo vendedor(a) : ")
            valor = int(input())
            remuneracao = calcularRemuneracao(valor)
            print("A remuneração do funcionário será : R$ " +str(remuneracao))
            abrirPrograma()
        else:
            print("opção inválida ! ")
