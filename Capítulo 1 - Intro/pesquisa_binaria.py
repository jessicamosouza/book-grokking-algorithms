def binary_search(num_list, item):
    low = 0
    high = len(num_list) - 1

    # acompanha a parte da lista que está procurando
    while low <= high:  # enquanto não chegar no elemento
        middle = (low + high) / 2  # verifica o elemento central
        middle_index = num_list[round(middle)]

        if middle_index == item:  # acha o item
            return round(middle)
        if middle_index > item:  # muito alto
            high = round(middle) - 1
        else:  # muito baixo
            low = round(middle) + 1


print("Posição: ", binary_search([10, 15, 20, 25, 26, 29, 40, 50], 29))  # print posição (= 5)
print("Posição: ", binary_search([10, 15, 20, 25, 26, 29, 40, 50], -1))  # se não encontrar, print None
