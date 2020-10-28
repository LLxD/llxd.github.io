N = int(input())  # entrada de segundos
D = N // (86400)  # calculo de dias
horas_rest = N % (86400)  # horas restantes
H = horas_rest//3600  # calculo de horas
min_rest = horas_rest % 3600  # minutos restantes
M = min_rest//60  # calculo dos minutos
S = min_rest % 60  # segundos restantes
print(D, "dia(s),", H, "hora(s),", M, "minuto(s) e", S, "segundo(s).")
