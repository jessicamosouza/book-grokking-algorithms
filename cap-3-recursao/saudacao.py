def sauda(nome):  # essa função te cumprimenta e chama as outras duas funções
    print("Olá, " + nome + "!")
    sauda2(nome)
    print("praparando para dizer tchau...")
    tchau()


def sauda2(nome):
    print("Como vai, " + nome + "?")


def tchau():
    print("Ok, tchau!")


print(sauda("Jéssica"))
