def casas(y):  # funcao que retorna o numero de casas do input
    j = 0  # contador
    while(y > 0):  # loop e contagem de casas
        y = y // 10
        j += 1
    return j


def distinct(x, numsize):  # comparador entre o ultimo digito de um numero e os seus antecessores
    ultimo = 0  # declaracao de variaveis
    list = []  # declaracao de uma lista
    for k in range(numsize):
        # insercao na lista de cada digito do numero
        list.insert(k, (x % (10**(k+1)))//(10**k))
    # verificacao se existem numeros iguais na lista
    duplicado = any(list.count(num) > 1 for num in list)
    if duplicado == True:
        return False
    else:
        return True


N = int(input())
M = int(input())
i = 0  # contador de numeros sem digitos iguais

while (N <= M):
    if(distinct(N, casas(N)) == True):
        i += 1
    N += 1
print(i)


# Lucas Lima do Nascimento
# 11721EMT014
