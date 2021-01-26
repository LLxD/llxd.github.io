def ler(num):  # funcao para leitura de dados, adicionando elas numa lista auxiliar
    temp = 0
    for i in range(num):
        temp = float(input())
        values.append(temp)
    return(values)


def lucro(acaoinicial, acaofinal):  # funcao para retornar o lucro entre duas acoes a e b
    precofinal = acoes[acaoinicial]*values[acaofinal]
    valorgasto = acoes[acaoinicial]*values[acaoinicial]
    return(precofinal-valorgasto)


def nAcoes(K, list, Q):  # funcao que retorna o numero maximo de acoes para os dias comparados
    acoes = []
    i = 0
    for dia in range(len(list)):
        acoes.append(int(Q/list[dia]))
    return(acoes)


def comparar(K, list, Q):
    i = 0
    j = 0
    acoes_index = []  # lista auxiliar com os indexes
    lucros = []  # lista que vai receber os lucros
    pares = []  # lista que recebe os pares que fazem cada lucro
    lucrototal = 0
    acoes_sort = acoes.copy()  # lista auxiliar para ordenacao
    acoes_sort.sort()
    for dia in range(len(acoes_sort)):
        # adicionar os indexes na lista auxiliar de indexes
        acoes_index.append(acoes.index(acoes_sort[dia]))
    for i in range(len(list)-1):
        while(j < len(list)-1):
            atual = acoes_index[i]  # index atual
            posterior = acoes_index[j+1]  # index posterior
            # se o valor atual for maior que o posterior e a distancia entre eles nao for maior que K, faca as operacoes de lucro
            if ((atual > posterior) and ((atual-posterior) <= K)):
                lucros.append(lucro(posterior, atual))
                pares.extend([posterior, atual])
            j += 1
        j = i
    if (lucros == []):  # casos onde nao ha lucro
        inicial, final, lucrototal = 0, 0, 0
        return(inicial, final, lucrototal)
    # caso haja lucro, localize os pares que o constituem
    inicial = pares[2*lucros.index(max(lucros))]
    final = pares[2*lucros.index(max(lucros))+1]
    lucrototal = max(lucros)
    return(inicial, final, lucrototal)


def printar(inicial, final, lucro):  # funcao para printar formatadamente todas as informacoes
    if inicial >= final:  # cobrindo o caso onde K eh maior que N
        final = inicial
    print("Dia da compra:", inicial+1)
    print("Valor de compra: R$", format(values[inicial], '.2f'))
    print("Dia da venda:", final+1)
    print("Valor de venda: R$", format(values[final], '.2f'))
    print("Quantidade de acoes compradas:", acoes[inicial])
    print("Lucro: R$", format(lucro, '.2f'))
    return()


values = []
acoes = 0

N = int(input())  # numero de dias
values = ler(N)
K = int(input())  # numero de dias entre as compras
Q = float(input())  # quantidade de dinheiro
acoes = nAcoes(K, values, Q)

if K >= N:  # cobrindo o caso onde K eh maior que N
    K = N
inicial, final, lucrototal = comparar(K, values, Q)
printar(inicial, final, lucrototal)

# Lucas Lima do Nascimento
# 11721EMT014
