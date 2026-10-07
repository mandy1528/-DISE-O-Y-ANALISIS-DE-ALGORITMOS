def esPalindromo_2(str):
    n = len(str)
    j = n - 1

    for i in range(n // 2):
        if str[i] != str[j]:
            return False
        j = j - 1

    return True

palabra = input("Ingresa una palabra: ")
print(esPalindromo_2(palabra))