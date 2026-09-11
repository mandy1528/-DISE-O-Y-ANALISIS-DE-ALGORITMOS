def calcular_pi(n):
    #entrada:el numerador de terminos(n)
    #salida:el valor aproximado(n)
    numerador = 1
    denominador = 1
    signo = 1
    pi = 0

    for i in range(n):
        denominador = denominador + 2
        pi = pi + signo * (numerador / denominador)
        signo = signo * -1
        
    return pi * 4

print(calcular_pi(1000000))
