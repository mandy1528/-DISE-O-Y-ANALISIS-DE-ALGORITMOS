def Palindromo (x):
#input: un numero entero
#output: True si es palindromo, False si no lo es
if x < 0: 
    return False
original = x
inv = 0

while x > 0:
        r = x % 10
        x = x // 10
        inv = (inv * 10) + r

return original == inv

numero = int(input("Ingresa un número entero: "))

if Palindromo(numero):
    print("True: es palíndromo")
else:
    print("False: no es palíndromo")
