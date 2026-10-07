def esPalindromo(str):
    n = len(str)
    inv = ""

    j = n - 1

    for i in range(n):
        inv = inv + str[j]
        j = j - 1

    if inv == str:
        return True
    else:
        return False


palabra = input("Ingresa una palabra: ")

print(esPalindromo(palabra))