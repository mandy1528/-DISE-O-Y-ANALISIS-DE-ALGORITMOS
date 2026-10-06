class Nodo:
    def __init__(self, valor):
        self.value = valor
        self.next = None


def busqueda_lista(head, target):
    actual = head
    encontrado = False

    while actual != None and encontrado == False:

        if actual.value == target:
            encontrado = True
        else:
            actual = actual.next

    return encontrado


nodo1 = Nodo(7)
nodo2 = Nodo(9)
nodo3 = Nodo(1)
nodo4 = Nodo(3)

nodo1.next = nodo2
nodo2.next = nodo3
nodo3.next = nodo4

head = nodo1

resultado = busqueda_lista(head, 11)

print(resultado)