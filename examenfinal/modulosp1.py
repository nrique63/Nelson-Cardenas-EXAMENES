import random
def aleatorio():
    lista = [random.randint(1,100) for _ in range(10)]
    print("La lista de numeros aleatorios es : {}".format(lista))
    return lista

def no_repetidos(lista):
    norepetidos =list(set(lista))
    print("La lista con los numeros no repetidos es : {}".format(norepetidos))
    return norepetidos

def mayor_menor(lista):
    ascendente = sorted(lista)
    descendente = sorted(lista, reverse=True)
    print("El orden ascendente es : {}".format(ascendente))
    print("El orden descendente es : {}".format(descendente))
    return ascendente, descendente

def mayor_par(lista):
    pares = [num for num in lista if num % 2 == 0]
    mayor = max(pares)
    print("El mayor numero par de la lista es : {}".format(mayor))
    return mayor