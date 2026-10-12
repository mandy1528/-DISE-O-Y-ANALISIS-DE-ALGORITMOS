def fibo(n):
    if n == 1:
        return 0

    if n == 2:
        return 1

    res = fibo(n - 1) + fibo(n - 2)
    return res


n = int(input("Ingresa el término a calcular: "))
print(fibo(n))