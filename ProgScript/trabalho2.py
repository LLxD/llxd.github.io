dias = int(input())  # recebe o numero de dias
i = dias  # salva o numero de dias no contador
temp = 0  # variavel temporaria da soma
add = 0  # variavel que recebe a entrada da soma
res = 0  # salva o numero de dias corridos ate o dia que atingiu o valor necessario
check = 1  # garante que a secao critica vai ser executada apenas uma vez

while (i > 0):  # inicia o loop
    add = int(input())  # le a entrada do usuario
    temp = temp + add  # armazena a entrada
    i = i - 1  # diminui o contador
    if (temp >= 1000000 and check == 1):  # verifica se o valor foi atingido
        res = dias - i  # armazena o dia onde o valor foi atingido
        check = False  # atualiza o valor de checagem para essa secao nao executar mais
print(res)  # printa os resultados

# Lucas Lima do Nascimento
# 11721EMT014
