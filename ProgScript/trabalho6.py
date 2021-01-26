def ler(num):  # funcao para leitura de dados, adicionando elas numa lista auxiliar
    values = []
    temp = 0
    for i in range(num):
        temp = int(input())
        values.append(temp)
    return(values)


N = int(input())  # numero de estacoes
C = int(input())  # numero de comandos
S = int(input())  # alvo

array = []
comandos = []

for i in range(N):  # vetor com as bases de carregamento
    array.append(i+1)

comandos = ler(C)  # vetor para a lista de comandos

contador = 0
if S == 1:  # caso a primeira base seja o alvo
    contador += 1
atual = 0
for j in range(C):
    # avance ou retroceda no vetor o valor determinado pelo comando
    atual = atual + comandos[j]
    if atual == N or atual == -N:  # caso seja a ultima posicao, retorne para o inicio
        atual = 0
    if array[atual] == S:
        contador += 1
print(contador)


# Lucas Lima do Nascimento
# 11721EMT014
