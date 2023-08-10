def busca_menor(arr):
    menor = arr[0]  # armazena o menor valor
    menor_indice = 0  # Armazena o índice correspondente ao menor valor
    for i in range(1, len(arr)):  # função range gera uma sequência de números de 1 até len(arr).
        # Esse loop percorrerá os elementos da lista a partir do segundo elemento até o último (len(arr))
        if arr[i] < menor:
            menor_indice = i
            menor = arr[i]
    return menor_indice


def ordenacao_por_selecao(arr):
    novo_arr = []
    for i in range(len(arr)):  # percorre o array inteiro (0 -> len(arr))
        menor = busca_menor(arr)  # busca pelo menor valor
        novo_arr.append(arr.pop(menor))  # adiciona ao novo_arr
    return novo_arr


result = ordenacao_por_selecao([5, 3, 6, 2, 10])
print(result)