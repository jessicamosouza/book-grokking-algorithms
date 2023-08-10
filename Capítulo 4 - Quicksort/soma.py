def soma(lista):
    total = 0
    for x in lista:
        total += x

    return total


def soma_recursiva(lista):
    if not lista:
        return 0  # caso base
    else:
        total = lista[0] + soma_recursiva(lista[1:])  # caso recursivo
        return total


print("Soma comum: ", soma([1, 2, 3, 4]))
print("Soma usando recursão: ", soma_recursiva([1, 2, 3, 4]))
