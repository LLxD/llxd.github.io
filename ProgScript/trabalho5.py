def checaSoma(n1, n2, n3, n4, n5, n6):  # funcao que verifica se a soma eh multipla de 7 ou 13
    soma = n1+n2+n3+n4+n5+n6
    if soma % 7 == 0 or soma % 13 == 0:
        return(True)
    else:
        return(False)


# entradas
n1 = int(input())
n2 = n1 + 1
n3 = int(input())
n4 = int(input())
n5 = n4 + 1
n6 = int(input())

print("Primeiro:", "{:02}".format(n1))
print("Terceiro:", "{:02}".format(n3))
print("Quarto:", "{:02}".format(n4))
print("Sexto:", "{:02}".format(n6))
print("Lista de apostas:")


# loop para o print das listas, iniciando em n1+1 e n4+1
for primeiro in range(n2, n3, 2):
    for segundo in range(n5, n6, 2):
        if checaSoma(n1, primeiro, n3, n4, segundo, n6) == False:
            print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1,
                                                                         primeiro, n3, n4, segundo, n6))


# Lucas Lima do Nascimento
# 11721EMT014
