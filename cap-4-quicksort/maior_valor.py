# def maior_valor(lista):
#     maior, i = 0, 0
#     for numero in lista:
#         if numero > maior:
#             maior = lista[i]
#             i += 1
#     return maior
#
#
# print(maior_valor(
#     [37, 52, 11, 8, 96, 24, 73, 40, 15, 67, 29, 85, 91, 3, 56, 72, 19, 42, 88, 33, 64, 45, 21, 76, 58, 90, 27, 46, 55,
#      2]))
#

def maior_valor(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    maior = maior_valor(lista[1:])
    return lista[0] if lista[0] > maior else maior


print(maior_valor(
    [37, 52, 11, 8, 96, 24, 73, 40, 15, 67, 29, 85, 91, 3, 56, 72, 19, 42, 88, 33, 64, 45, 21, 76, 58, 90, 27, 46, 55,
     2]))
