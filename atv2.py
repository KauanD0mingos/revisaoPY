# Escreva uma função separa_pares_impares(numeros) que recebe uma lista de números inteiros e retorna duas listas: uma contendo os números pares e outra contendo os ímpares.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def separa_pares_impares(lista):
    listaImpar = []
    listaPar = []
    for i in lista:
        if (i % 2 == 1):
            listaImpar.append(i)
        else:
            listaPar.append(i)
            
    print(listaImpar)
    print(listaPar)

separa_pares_impares(numeros)