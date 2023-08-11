def num_items(lista):
    if not lista:
        return 0
    else:
        num = 1 + num_items(lista[1:])
        return num


print("Número de items na lista: ", num_items([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]))
